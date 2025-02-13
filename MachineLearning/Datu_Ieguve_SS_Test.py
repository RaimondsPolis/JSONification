#iegūt daudzu mašīnu datus no SS.LV
import requests
import os
from bs4 import BeautifulSoup as bs
import csv
import time

URL = "https://www.ss.lv/lv/transport/cars/today-5/sell/"
DATI = "MachineLearning/dati/"
LAPAS = "MachineLearning/lapas/"



tilpumsDiesel = "Diesel"
tilpumsGas = "Gasoline"
tilpumsElc = "Electric"
tilpumsHybrid = "Hybrid"


def saglaba_lapu(url, nosaukums):
    iegutais = requests.get(url)
    print(iegutais.status_code)
    if iegutais.status_code == 200:
        with open(nosaukums, "w", encoding="utf-8") as f: #JA OPEN NEATROD FAILU, TAS TO UZTAISA
            f.write(iegutais.text)
    return

#saglaba_lapu(URL, LAPAS+"pirma.html")

def saglaba_visas_lapas(skaits):
    for i in range(1, skaits+1):
        saglaba_lapu(f"{URL}page{i}.html", f"{LAPAS}lapa{i}.html")
        time.sleep(0.5)
    return


def dabut_info(lapa):
    dati = []
    with open(lapa, "r", encoding="utf-8") as f:
        html=f.read()
    zupa = bs(html, "html.parser")
    galvenais = zupa.find(id="page_main")#atrod sadaļu ar id=page_main
    tabulas = galvenais.find_all('table')
    rindas = tabulas[2].find_all('tr')
    for rinda in rindas[1:]:
        lauki = rinda.find_all('td')
        if len(lauki)<8:
            print("dīvaina rinda")
            continue
        auto = {}
        auto['sludinajuma_saite']= lauki[1].find('a')['href']#atrod <a href="..."> sūdus
        auto['bilde'] = lauki[1].find('img')['src']# atrod <img src="..."> sūdus
        auto['marka'] = lauki[3].get_text(strip=True)
        auto['gads'] = lauki[4].get_text(strip=True)
        auto['nobraukums'] = lauki[6].get_text(strip=True)
        auto['cena'] = lauki[7].get_text(strip=True)
        tilpums = lauki[5].get_text(strip=True)

        if tilpums == "E":
            tilpums = "Electric"

        if "D" in tilpums:
            parts = tilpums.split("D")
            if len(parts) > 1 and parts[1] == "":
                tilpums = parts[0] + " Diesel"

        if "H" in tilpums:
            parts = tilpums.split("H")
            if len(parts) > 1 and parts[1] == "":
                tilpums = parts[0] + " Hybrid"

        if not "E" in tilpums and not "D" in tilpums and not "H" in tilpums:
            tilpums = tilpums + " Gasoline"

        auto['tilpums'] = tilpums

        dati.append(auto)
    return dati

def saglaba_datus(dati, tilpums):
    if tilpums.split()[1] == "Gasoline":
        with open(DATI+"sslvGas.csv", "w", encoding="utf-8")as f:
            lauku_nosaukumi = ['sludinajuma_saite', 'bilde','marka','gads','tilpums','nobraukums','cena']
            w = csv.DictWriter(f, fieldnames=lauku_nosaukumi)
            w.writeheader()
            for auto in dati:
                w.writerow(auto)
    
    if tilpums == "Electric":
        with open(DATI+"sslvElc.csv", "w", encoding="utf-8")as f:
            lauku_nosaukumi = ['sludinajuma_saite', 'bilde','marka','gads','tilpums','nobraukums','cena']
            w = csv.DictWriter(f, fieldnames=lauku_nosaukumi)
            w.writeheader()
            for auto in dati:
                w.writerow(auto)
    
    if tilpums.split()[1] == "Diesel":
        with open(DATI+"sslvDsl.csv", "w", encoding="utf-8")as f:
            lauku_nosaukumi = ['sludinajuma_saite', 'bilde','marka','gads','tilpums','nobraukums','cena']
            w = csv.DictWriter(f, fieldnames=lauku_nosaukumi)
            w.writeheader()
            for auto in dati:
                w.writerow(auto)

    if tilpums == "Hybrid":
        with open(DATI+"sslvHyb.csv", "w", encoding="utf-8")as f:
            lauku_nosaukumi = ['sludinajuma_saite', 'bilde','marka','gads','tilpums','nobraukums','cena']
            w = csv.DictWriter(f, fieldnames=lauku_nosaukumi)
            w.writeheader()
            for auto in dati:
                w.writerow(auto)

    return


#saglaba_datus(dabut_info(LAPAS+"pirma.html"))
#saglaba_visas_lapas(10)

def dabut_info_daudz(skaits):
    visi_dati = []
    for i in range(1, skaits+1):
        dati = dabut_info(f"{LAPAS}lapa{i}.html")
        visi_dati += dati #uztaisās kā viens garš saraksts
        #visi_dati, stringu dati pievieno galā
    return visi_dati

saglaba_visas_lapas(1)
info = dabut_info_daudz(280)
saglaba_datus(info, tilpumsDiesel)

        

#marka,gads,tilpums,nobraukums,cena

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

datne1 = "MachineLearning/dati/sslv.csv"
kol_x1=['marka','gads', 'tilpums', 'nobraukums']
kol_y1=['cena']


#sagatavot datus
X_train, x_test, Y_train, y_test = sagatavot_datus(datne1, kol_x1, kol_y1)
#sagatavot modeli
modelis = ensemble.GradientBoostingRegressor()

modelis = trenet_modeli(modelis, X_train, Y_train)
rezultats = parbaudit_modeli(modelis, x_test)

modela_kvalitate(y_test, rezultats)


print(rezultats)


# dati1_x = [1000, 790]
# dati1_rez = 99

# rezultats_1 = parbaudit_modeli(modelis, [dati1_x])
# print(cl(f"sagaidāmais rezultats: {dati1_rez}, MI rezultats: {rezultats}", 'magenta'))