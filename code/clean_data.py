import pandas as pd
import numpy as np
from params import X

df_all = pd.DataFrame()
for y in range(2008,2019):
    print(y)
    df = pd.read_csv('../data/clean/data'+str(y)+'.csv')
    df_all = df_all.append(df)

df_all.to_csv('../data/clean/dataClean.csv')