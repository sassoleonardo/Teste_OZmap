# Teste técnico para vaga de estágio em análise e manipulação de dados.
#### O teste consiste em gerar, através de um script em python, uma planilha que contém a quantidade de usuários por módulo para 4 empresas. Para isso serão realizadas consultas para a rota "rota" que contém uma lista com os dados de todos os usuários. Os módulos são OZmap, Loki, OZmob e API.

### Lendo os dados via API (são 4 API's diferentes, cada uma referente a uma empresa fictícia):
```python
#company_A
Headers_A = {"Authorization": "access key"}
url_A = ("url/company/A")
response_A = requests.get(url_A, headers=Headers_A).json()
data_A = response_A.get('rows') #jsons 
```
```python
#company_B
Headers_B = {"Authorization": "access key"}
url_B = ("url/company/B")
response_B = requests.get(url_B, headers=Headers_B).json()
data_B = response_B.get('rows') #jsons
```
```python
#company_C
Headers_C = {"Authorization": "access key"}
url_C = ("url/company/C")
response_C = requests.get(url_C, headers=Headers_C).json()
data_C = response_C.get('rows') #jsons

```
```python
#company_D
Headers_D = {"Authorization": "access key"}
url_D = ("url/company/D")
response_D = requests.get(url_D, headers=Headers_D).json()
data_D = response_D.get('rows') #jsons
```

### Criando uma classe para escrever os dados posteriormente.
```python
writer = pd.ExcelWriter('final.xlsx')
```
### Função para encontrar quantos usuários por módulo, e escrever o resultado no arquivo xlsx em 4 planilhas diferentes. Os parâmetros são os dados requisitados via API (data) e o nome da empresa (company).

```python
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
    #SAVING THE OBTAINED DATA IN TO EXCEL FILE
    df = pd.DataFrame([[count_API], [count_Loki], [count_OZmap], [count_OZmob]], index = ['API', 'LOKI', 'OZMAP', 'OZMOB'], columns = ['users'])
    df.to_excel(writer, f'{company}')
    print(df)

```
### Aplcando a função em cada empresa:
```python
find_modules(data=data_A, company='company_A')
find_modules(data=data_B, company='company_B')
find_modules(data=data_C, company='company_C')
find_modules(data=data_D, company='company_D')
```
### Salvando os dados no arquivo xlsx:
```python
writer.save() 
```
