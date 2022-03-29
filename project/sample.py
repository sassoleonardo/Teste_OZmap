import pandas as pd
import requests

###GET THE DATA VIA API
#company_A
Headers_A = {"Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtb2R1bGUiOiJhcGkiLCJ1c2VyIjoiNWQ5ZjNmYjgyMDAxNDEwMDA2NDdmNzY4IiwiY3JlYXRpb25EYXRlIjoiMjAyMi0wMy0yNFQyMDo0NTowOC40MDZaIiwiaWF0IjoxNjQ4MTU0NzA4fQ.3Vg39IhsFa2fSywiqc3xGNrIu-ZTpmGSzxrQ00JJxsc"}
url_A = ("https://import-beltra.ozmap.com.br:9994/api/v2/users")
response_A = requests.get(url_A, headers=Headers_A).json()
data_A = response_A.get('rows') #jsons

#company_B
Headers_B = {"Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtb2R1bGUiOiJhcGkiLCJ1c2VyIjoiNWQ5ZjNmYjgyMDAxNDEwMDA2NDdmNzY4IiwiY3JlYXRpb25EYXRlIjoiMjAyMi0wMy0yNFQyMjoyNzowOC44NTdaIiwiaWF0IjoxNjQ4MTYwODI4fQ.Jce1yuBY-k6mK2ywpJlJb3VB5Tn_GCpVH1u7r_Yoxeg"}
url_B = ("https://import-beltra2.ozmap.com.br:9994/api/v2/users")
response_B = requests.get(url_B, headers=Headers_B).json()
data_B = response_B.get('rows') #jsons

#company_C
Headers_C = {"Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtb2R1bGUiOiJhcGkiLCJ1c2VyIjoiNjIyOGRmZmVkMmZlZTYwMDIwZjg0ZmViIiwiY3JlYXRpb25EYXRlIjoiMjAyMi0wMy0yNFQyMjoyNzozNS4zMjBaIiwiaWF0IjoxNjQ4MTYwODU1fQ.F6YuznPvc4sfmEFQCJMf2hMWa4lRxjmPo16UVDqaLC0"}
url_C = ("https://import-beltra3.ozmap.com.br:9994/api/v2/users")
response_C = requests.get(url_C, headers=Headers_C).json()
data_C = response_C.get('rows') #jsons

#company_D
Headers_D = {"Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtb2R1bGUiOiJhcGkiLCJ1c2VyIjoiNWQ5ZjNmYjgyMDAxNDEwMDA2NDdmNzY4IiwiY3JlYXRpb25EYXRlIjoiMjAyMi0wMy0yNFQyMDo0OTo1Ni41OTZaIiwiaWF0IjoxNjQ4MTU0OTk2fQ.U7T6HtrL8dW-rLJO6Us7TKt7MAE2BQfg4cwCo3ZWTmY"}
url_D = ("https://teste.ozmap.com.br:9994/api/v2/users")
response_D = requests.get(url_D, headers=Headers_D).json()
data_D = response_D.get('rows') #jsons


###CREATE A XLSX FILE TO WRITE IT LATER
writer = pd.ExcelWriter('final.xlsx')


###FIND HOW MANY MODULES ARE IN EACH COMPANY
def find_modules(data, company):
    count_API = 0
    count_OZmob = 0
    count_OZmap = 0
    count_Loki = 0
    for modules in range(0, len(data)):
        module = data[modules]['resources']
        if any("API" in s for s in module):
            count_API+=1
        if any("Loki" in s for s in module):
            count_Loki+=1
        if any("OZmob" in s for s in module):
            count_OZmob+=1
        if any("OZmap" in s for s in module):
            count_OZmap+=1
    ###SAVING THE OBTAINED DATA IN TO EXCEL FILE
    df = pd.DataFrame([[count_API], [count_Loki], [count_OZmap], [count_OZmob]], index = ['API', 'LOKI', 'OZMAP', 'OZMOB'], columns = ['users'])
    df.to_excel(writer, f'{company}')
    print(df)

find_modules(data=data_A, company='company_A')
find_modules(data=data_B, company='company_B')
find_modules(data=data_C, company='company_C')
find_modules(data=data_D, company='company_D')
writer.save() 
