import requests
import json
import os
import time

datosPRED=[]
err=0

dir="/your/leafmet/location/"

#API Key
ak="YOUR-API-KEY"

with open(dir+'municipios.json', encoding='ISO-8859-1') as file:
    data = json.load(file)
    
for i, x in enumerate(data):
    try:
        print(x["id_old"])
        #Delay request to avoid API limit
        time.sleep(0.8)
        mUrl=requests.get("https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/diaria/"+x["id_old"]+"?api_key="+ak).json()
        mData=requests.get(mUrl["datos"]).json()
        #datosPRED.append(mData)
        datos=[]
        datos.append(x["id_old"])
        datos.append(x["nombre"])
        datos.append(x["latitud_dec"])
        datos.append(x["longitud_dec"])
        datos.append(mData)
        datosPRED.append(datos)
        print(str(i)+"/"+str(len(data))+" ("+str(int(i/len(data)*100))+"%)")
    except:
        err=err+1
        print("---ERROR "+str(err))
#Write to file
datosPRED="var predData="+str(datosPRED)+";"
datafile=open(dir+'predData.js', 'w')
datafile.write(str(datosPRED))
datafile.close()
print(str(int(err/len(data)*100))+"% datos")
