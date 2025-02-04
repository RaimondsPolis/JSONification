import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from PIL import Image


bilzu_adrese = "maju_meklesana/bildes/"

modelis = RandomForestClassifier()

def modela_trenesana(modelis):
    bildes = []
    label = []

    for nosaukums in os.listdir(bilzu_adrese):
        image = Image.open(os.path.join(bilzu_adrese,nosaukums)).resize((200,200), Image.Resampling.NEAREST)
        bildes.append(np.array(image))
        if "maja" in nosaukums:
            label.append(1)
        else:
            label.append(0)
    #datu sakitļu salabošana
    bildes = np.array(bildes)
    label = np.array(label)

    bildes = bildes/255.0 #
    bildes = bildes.reshape(bildes.shape[0], -1)

    X_train, X_test, y_train, y_test = train_test_split(bildes, label, test_size=3)#JA TEST SIZE IR LIELĀKS PAR 1 TAD VIŅŠ SKATĀS NO TĀ CIK FAILI IR PIEEJAMI

    modelis.fit(X_train, y_train) #fit = trennē datoru

    rezultats = modelis.predict(X_test)

    precizitate = accuracy_score(y_test, rezultats)
    print(precizitate)
    return modelis

def majas_noteiksana(bilde, modelis):
    bilde = [Image.open(bilde).resize((200,200), Image.Resampling.NEAREST)]
    bilde = np.array(bilde) 
    bilde = bilde/255.0
    bilde = bilde.reshape(bilde.shape[0], -1)
    rezultats = modelis.predict(bilde)
    if rezultats[0] ==1:
        rezultats = "ir maja"
    if rezultats[0] ==0:
        rezultats = "nav maja"
    print(f"rezultats: {rezultats}")
    return rezultats

modelis = modela_trenesana(modelis)
print("__________________________________________")
majas_noteiksana("maju_meklesana/bildes/download1.jpg", modelis)
print("__________________________________________")