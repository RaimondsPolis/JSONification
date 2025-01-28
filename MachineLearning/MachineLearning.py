import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import pickle

from termcolor import colored as cl
#pip install -U scikit-learn
from sklearn.model_selection import train_test_split

#modeļi
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import BayesianRidge
from sklearn.linear_model import ElasticNet
from sklearn import ensemble #Labāki modeļi/ algoritmi






#modeļu analīze
from sklearn.metrics import explained_variance_score as evs
from sklearn.metrics import r2_score as r2

def sagatavot_datus(fails, kolonna_x, kolonna_y):
    datu_fails = pd.read_csv(fails)
    datu_fails.dropna(inplace=True)
    X_var = datu_fails[kolonna_x]
    Y_var = datu_fails[kolonna_y]

    X_train, x_test, Y_train, y_test = train_test_split(X_var, Y_var, test_size=0.2, random_state=0) 

    return (X_train, x_test, Y_train, y_test)  #maybe vajag iekavās visu, nezinu

def modela_kvalitate(y_test, results):
    print(cl(f'Dispersija: {evs(y_test, results)}', 'red', attrs=['bold']))
    print(cl(f'Kvadrātiskā novirze: {r2(y_test, results)}', 'blue', attrs=['bold']))


def trenet_modeli(modelis, X_train, Y_train):
    modelis.fit(X_train, Y_train)
    return modelis

def parbaudit_modeli(modelis, x_test):
    results = modelis.predict(x_test)
    return results

datne1 = "MachineLearning/auto_simple.csv"
kol_x1=['Volume','Weight']
kol_y1=['CO2']

#sagatavot datus
X_train, x_test, Y_train, y_test = sagatavot_datus(datne1, kol_x1, kol_y1)
#sagatavot modeli
modelis = ensemble.GradientBoostingRegressor()

modelis = trenet_modeli(modelis, X_train, Y_train)
rezultats = parbaudit_modeli(modelis, x_test)

modela_kvalitate(y_test, rezultats)


dati1_x = [1000, 790]
dati1_rez = 99

rezultats_1 = parbaudit_modeli(modelis, [dati1_x])
print(cl(f"sagaidāmais rezultats: {dati1_rez}, MI rezultats: {rezultats}", 'magenta'))