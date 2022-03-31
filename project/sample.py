import pandas as pd
import requests

##GET DATA
#company_a
Headers_a = {"Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtb2R1bGUiOiJhcGkiLCJ1c2VyIjoiNWQ5ZjNmYjgyMDAxNDEwMDA2NDdmNzY4IiwiY3JlYXRpb25EYXRlIjoiMjAyMi0wMy0yNFQyMDo0NTowOC40MDZaIiwiaWF0IjoxNjQ4MTU0NzA4fQ.3Vg39IhsFa2fSywiqc3xGNrIu-ZTpmGSzxrQ00JJxsc"}
url_a = ("https://import-beltra.ozmap.com.br:9994/api/v2/users")
response_a = requests.get(url_a, headers=Headers_a).json()
data_a = response_a.get('rows') #jsons

#company_b
Headers_b = {"Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtb2R1bGUiOiJhcGkiLCJ1c2VyIjoiNWQ5ZjNmYjgyMDAxNDEwMDA2NDdmNzY4IiwiY3JlYXRpb25EYXRlIjoiMjAyMi0wMy0yNFQyMjoyNzowOC44NTdaIiwiaWF0IjoxNjQ4MTYwODI4fQ.Jce1yuBY-k6mK2ywpJlJb3VB5Tn_GCpVH1u7r_Yoxeg"}
url_b = ("https://import-beltra2.ozmap.com.br:9994/api/v2/users")
response_b = requests.get(url_b, headers=Headers_b).json()
data_b = response_b.get('rows') #jsons

#company_c
Headers_c = {"Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtb2R1bGUiOiJhcGkiLCJ1c2VyIjoiNjIyOGRmZmVkMmZlZTYwMDIwZjg0ZmViIiwiY3JlYXRpb25EYXRlIjoiMjAyMi0wMy0yNFQyMjoyNzozNS4zMjBaIiwiaWF0IjoxNjQ4MTYwODU1fQ.F6YuznPvc4sfmEFQCJMf2hMWa4lRxjmPo16UVDqaLC0"}
url_c = ("https://import-beltra3.ozmap.com.br:9994/api/v2/users")
response_c = requests.get(url_c, headers=Headers_c).json()
data_c = response_c.get('rows') #jsons

#company_d
Headers_d = {"Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtb2R1bGUiOiJhcGkiLCJ1c2VyIjoiNWQ5ZjNmYjgyMDAxNDEwMDA2NDdmNzY4IiwiY3JlYXRpb25EYXRlIjoiMjAyMi0wMy0yNFQyMDo0OTo1Ni41OTZaIiwiaWF0IjoxNjQ4MTU0OTk2fQ.U7T6HtrL8dW-rLJO6Us7TKt7MAE2BQfg4cwCo3ZWTmY"}
url_d = ("https://teste.ozmap.com.br:9994/api/v2/users")
response_d = requests.get(url_d, headers=Headers_d).json()
data_d = response_d.get('rows') #jsons


##WRITE DATA
writer = pd.ExcelWriter('final.xlsx')


##FIND MODULES
def find_modules(data, company):
    count_api = 0
    count_ozmob = 0
    count_ozmap = 0
    count_loki = 0
    for modules in range(0, len(data)):
        module = data[modules]['resources']
        if any("API" in s for s in module):
            count_api+=1
        if any("Loki" in s for s in module):
            count_loki+=1
        if any("OZmob" in s for s in module):
            count_ozmob+=1
        if any("OZmap" in s for s in module):
            count_ozmap+=1
    ##SAVE DATA
    df = pd.DataFrame([[count_api], [count_loki], [count_ozmap], [count_ozmob]], index = ['API', 'LOKI', 'OZMAP', 'OZMOB'], columns = ['users'])
    df.to_excel(writer, f'{company}')
    print(df)

find_modules(data=data_a, company='company_a')
find_modules(data=data_b, company='company_b')
find_modules(data=data_c, company='company_c')
find_modules(data=data_d, company='company_d')
writer.save() 
