import os
import numpy as np
import pickle as pkl
import pandas as pd
from xgboost import XGBRegressor
import lightgbm as lgb
from sklearn.ensemble import RandomForestRegressor
from matplotlib import pyplot as plt
import time
import multiprocessing as mp
import warnings
from models import model
import copy
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

# cut sample
def cutSample(cvgroup, j, K, wte = 0):
    """assigns sample to training/test groups. If wte==1, sample for evaluating h is also provided.
    
    Parameters
    ----
    cvgroup: vector that assigns samples
    j: order of cuts
    K: total number of cuts
    wte: indicator for wte/ate (1/0)

    Returns
    ---
    nii_m, nii_h: indicator for training group for outcome model/ h model
    ii_m, ii_h: indicator for test group for outcome model/ h model
    """
    ii_m = cvgroup == j
    nii_m = cvgroup !=j
    if (wte == 1):
        nx = j+1 if (j!=K-1) else 0 #h eval group
        nii_h = (cvgroup != j) & (cvgroup!=nx)
        ii_h = cvgroup == nx
        return nii_m, ii_m, nii_h, ii_h
    return nii_m, ii_m

# WTE
def wte(data, y, d, x, alpha, K, split, models, args,
        pos = 0, randomized = False, silent=False, pickle=False, tag=""):
    """ this function takes in data, and produes wte estimates

    Parameters
    -------
    data: input dataframe
    y: string of y column name
    d: string of d column name
    x: vector of strings of x coumn names
    alpha: vector of parameter for wte
    K: number of cuts
    split: number of iterations
    model_mu: outcome model
    arg_mu: arguments for outcome model
    model_p: propensity score model
    arg_p: arguments for propensity score model
    pos(optional): 1 if ate is positive, 0(default) if negative

    Returns
    ------
    wte_est: dictionary of aggregated estimate of wte by alpha
    wte_std: dictionary of aggregated estimate of standard deviation of wte by alpha.
    """
    est_store, std_store = {}, {}
    est_med, std_med = {}, {}
    for a in alpha:
        est_store[a], std_store[a] = [], []
    while (split > 0):  # loop through splits
        if (silent == False):
            print("split: ", split)
        np.random.seed(1234)
        cvgroup = np.random.randint(0,K,data.shape[0])
        est, var = {}, {}
        for a in alpha:
            est[a], var[a] = 0, 0
        for j in range(0,K): # loop through cuts
            # calculate wte
            ret_est, ret_var = calculate_wte(cvgroup, j, K, data, y, d, x, models, args,
                                             alpha, pos, silent, pickle,tag, 
                                             randomized = randomized)
            for a in alpha:
                est[a] += (1./K) * ret_est[a]
                var[a] += (1./K) * (1./data.shape[0]) * ret_var[a]
        for a in alpha:
            est_store[a].append(est[a])
            std_store[a].append(np.sqrt(var[a]))
        if (silent==False):
            print(est, np.sqrt(var[a]))
        split -= 1
    # return median of all wte estimates
    for a in alpha:
        est_med[a] = np.median(est_store[a])
        std_med[a] = np.median(std_store[a])
    return est_med, std_med

def geth(alpha, mu0_h, mu1_h, mu0, mu1, pos):
    """gets h vector for wte estimation
    
    Parameters
    ------
    alpha: vector of alpha values for wte estimation (0 < alpha < 1)
    mu: list of arrays of predicted outcomes 
        - mu[0]: model_h outcome for control
        - mu[1]: model_h outcome for treated
        - mu[2]: model outcome for control
        - mu[3]: model outcome for treated
        - mu[4]: propensity score
    pos: 1 if ate is positive; 0 if not.

    Returns
    ------
    dictionary: dictionary of alpha (int): array(1/0) that represent h vectors for each alpha.
    """
    h = {}
    for a in alpha:
        if (pos == 0):
            h[a] =((mu1 - mu0) > np.quantile((mu1_h - mu0_h), 1. - a)) * (a**(-1))
        elif (pos == 1):
            h[a] = ((mu1 - mu0) < np.quantile((mu1_h - mu0_h), a)) *  (a**(-1))
    return h

def calculate_wte(cvgroup, j, K, data, y, d, x, models, args, alpha, pos, silent,pickle,tag, randomized = False):
    """This function trains and estimates elements that go into wte estimator. such as hte, h (minority indicator), and propensity score.
    
    Parameters
    ------
    cvgroup: vector that assigns samples
    j: iterator for cuts (0 <= j <= K)
    K: number of cuts
    data: dataframe to be used for calculating wte
    y: string of y column name
    d: string of d column name
    x: vector of strings of x column names
    model_mu: outcome model
    arg_mu: arguments of outcome model
    model_p: propensity score model
    arg_p: arguments of propensity score model
    alpha: vector of parameter for wte
    pos: 1 if ate is positive; 0 if negative

    Returns
    ------
    ret_est: vector of wte estimates for each alpha for one sample cut
    ret_std: vector of wte standard deviation for each alpha for one sample cut
    """
    # cut sample
    nii_m, ii_m, nii_h, ii_h = cutSample(cvgroup, j, K, wte = 1)
    train = data[nii_m]; test = data[ii_m]
    train_h = data[nii_h]; test_h = data[ii_h]
    
    # train and predict models
    model1_h = models['model1_h']; model0_h = models['model0_h'];
    model1_h.train(train_h[train_h[d]==1],x,y,args['args_mu'])
    model0_h.train(train_h[train_h[d]==0],x,y,args['args_mu'])
    mu1_h = model1_h.predict(test_h)
    mu0_h = model0_h.predict(test_h)
    
    model1 = models['model1']; model0 = models['model0'];
    model1.train(train[train[d]==1],x,y ,args['args_mu'])
    model0.train(train[train[d]==0],x,y,args['args_mu'])
    mu1 = model1.predict(test)
    mu0 = model0.predict(test)
    print(mu1,mu0)
    print('mu trained and predicted')
    
    if randomized == True:
        p = np.ones(test.shape[0])*.5
    else:
        modelp = models['model_p'];
        modelp.train(train,x,d,args['args_p'])
        p = modelp.predict(test)
    
    h = geth(alpha,mu0_h, mu1_h, mu0, mu1,pos)

    # calculate est and std
    ret_est, ret_var = {}, {}
    for a in alpha:
        ret_est[a], ret_var[a] = wte_est(test[y], test[d], mu1, mu0, h[a], p, a, pos, silent)
    return ret_est, ret_var

def wte_est(y, d, mu1, mu0, h, p, alpha, pos, silent):
    """This function buildes wte estimator from elements.
    
    Note
    ------
    wte_est = (1./alpha)* max(mu1-mu0-mperc,0) + mperc 
            + h * d * (y - mu1) / p
            - h* (1 - d) * (y - mu0) / (1 - p)
    where mperc is the (1-alpha)*100 percentile of hte.
   
    Parameters
    ------
    y: string of y column name
    d: string of d column name
    mu1: vector of Y(1) estimates (potential outcome)
    mu0: vector of Y(0) estimates (potential outcome)
    h: vector of minority indicator
    p: vector of propensity scores
    alpha: parameter of wte
    pos: 1 if ate is positive; 0 if negative

    Returns
    ------
    wte_est: float estimate for wte
    """
    if (pos == 0):
        mperc = np.quantile((mu1 - mu0),(1. - alpha))
        te = (1. / alpha) * np.maximum(mu1 - mu0 - mperc, 0) + mperc
    elif (pos == 1):
        mperc = np.quantile((mu1 - mu0), alpha)
        te = (1. / alpha) * np.minimum(mu1 - mu0 - mperc, 0) + mperc
    score1 = h * d * (y - mu1) / p
    score0 = h * (1 - d) * (y - mu0) / (1 - p)
    if (silent==False):
        print("alpha:", alpha, "te :", np.mean(te),", score 1:", np.mean(score1), ", score0:", np.mean(score0))
    return np.mean(te + score1 - score0), np.var(te + score1 - score0)


