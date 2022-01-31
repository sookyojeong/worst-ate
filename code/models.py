from sklearn.model_selection import GridSearchCV
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import ElasticNet, Lasso, LogisticRegression
from matplotlib import pyplot as plt
import lightgbm as lgb
import xgboost as xgb
import multiprocessing as mp


class model():
    """class for gradient boosting regressor model
    Attributes
    ------
    model: model instance from sklearn
    x: vector of strings with x column names
    args: dictionary of arguments
    """
    def __init__(self):
        self.model_class = 'gbdt'
        self.model = None
        self.x = None
    def train(self, datause, x, y, args , state=524, binary = 0):
        """trains model using cross validated (or default) parameters
        
        Parameters
        ------
        datause: dataframe to be used for training
        x: vector of strings of x column names
        y: string of outcome name
        state (optional): random state seed for building trees
        """
        if self.model_class == 'gbdt':
            dtrain = xgb.DMatrix(datause[x],datause[y])
            self.model = xgb.train(args, dtrain)
        elif self.model_class == 'rf':
            dtrain = lgb.Dataset(datause[x], label = datause[y])
            self.model = lgb.train(args, dtrain)
        elif self.model_class == 'enet':
            self.model = ElasticNet(random_state=0,
                                   alpha = args['alpha'],
                                   l1_ratio = args['l1_ratio']).fit(datause[x], datause[y])
        elif self.model_class == 'scikit_rf':
            self.model=RandomForestRegressor(n_estimators = args['n_estimators'],
                                            min_samples_leaf = args['min_samples_leaf'],
                                            max_depth = args['max_depth'],
                                            min_samples_split = args['min_samples_split'],
                                            max_features = args['max_features'],
                                            random_state = 0).fit(datause[x],datause[y])
        elif self.model_class == 'scikit_gb':
            self.model = GradientBoostingRegressor(n_estimators = args['n_estimators'],
                                                   min_samples_leaf = args['min_samples_leaf'],
                                                   max_depth = args['max_depth'],
                                                   min_samples_split = args['min_samples_split'],
                                                   learning_rate = args['learning_rate'],
                                                   max_features = args['max_features'],
                                                   subsample = args['subsample'],
                                                   random_state = 0).fit(datause[x], datause[y])
        else:
            raise ValueError('model class is not recognized.')
            
        self.x = x
    def predict(self, dataout):
        """predict outcome using trained model
        Parameters
        ------
        dataout: dataframe used for predictiong outcome
        Returns
        ------
        array: array of predicted outcomes
        """
        if self.model_class=='gbdt':
            return self.model.predict(xgb.DMatrix(dataout[self.x]))
        elif self.model_class == 'rf':
            return self.model.predict(dataout[self.x])
        elif self.model_class=='enet':
            return self.model.predict(dataout[self.x])
        elif self.model_class == 'scikit_rf':
            return self.model.predict(dataout[self.x])
        elif self.model_class == 'scikit_gb':
            return self.model.predict(dataout[self.x])
        else:
            raise ValueError('model class is not recognized.')
        return None