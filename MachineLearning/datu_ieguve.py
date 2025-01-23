#iegūt daudzu mašīnu datus no SS.LV
import requests
import os
from bs4 import BeautifulSoup as bs
import csv
import time

URL = "https://www.ss.lv/lv/transport/cars/today-5/sell/"
DATI = "MachineLearning/dati/"
LAPAS = "MachineLearning/lapas/"


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
        dati.append(auto)
    return dati

def saglaba_datus(dati):
    with open(DATI+"sslv.csv", "w", encoding="utf-8")as f:
        lauku_nosaukumi = ['sludinajuma_saite', 'bilde']
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

saglaba_visas_lapas(280)
info = dabut_info_daudz(280)
saglaba_datus(info)
        