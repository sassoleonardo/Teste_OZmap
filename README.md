# Teste técnico para vaga de estágio em análise e manipulação de dados.
#### O teste consiste em gerar, através de um script em python, uma planilha que contém a quantidade de usuários por módulo para 4 empresas. Para isso serão realizadas consultas para a rota "rota" que contém uma lista com os dados de todos os usuários. Os módulos são OZmap, Loki, OZmob e API.

#### Para rodar o código bastar executar o comando sample.py dentro da pasta do programa. Ele vai gerar um arquivo xlsx contendo as informações requisitadas.


### Libs:
```python
import pandas as pd
import requests
```
### Lendo os dados via API:
```python
#company_a
Headers_a = {"Authorization": "access key"}
url_a = ("url/company/A")
response_a = requests.get(url_a, headers=Headers_a).json()
data_a = response_A.get('rows') #jsons 
```
```python
#company_b
Headers_b = {"Authorization": "access key"}
url_b = ("url/company/B")
response_b = requests.get(url_b, headers=Headers_b).json()
data_b = response_b.get('rows') #jsons
```
```python
#company_c
Headers_c = {"Authorization": "access key"}
url_c = ("url/company/C")
response_c = requests.get(url_C, headers=Headers_C).json()
data_c = response_c.get('rows') #jsons

```
```python
#company_d
Headers_d = {"Authorization": "access key"}
url_d = ("url/company/D")
response_d = requests.get(url_d, headers=Headers_d).json()
data_d = response_d.get('rows') #jsons
```

### Criando uma classe para escrever os dados posteriormente:
```python
writer = pd.ExcelWriter('final.xlsx')
```
### Função para encontrar quantos usuários por módulo, e escrever o resultado no arquivo xlsx em planilhas diferentes. Os parâmetros são os dados requisitados via API (data) e o nome da empresa (company):

```python
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
    #SAVE DATA
    df = pd.DataFrame([[count_api], [count_loki], [count_ozmap], [count_ozmob]], index = ['API', 'LOKI', 'OZMAP', 'OZMOB'], columns = ['users'])
    df.to_excel(writer, f'{company}')
    print(df)

```
### Aplicando a função em cada empresa:
```python
find_modules(data=data_a, company='company_a')
find_modules(data=data_b, company='company_b')
find_modules(data=data_c, company='company_c')
find_modules(data=data_d, company='company_d')
```
### Salvando os dados no arquivo xlsx:
```python
writer.save() 
```
