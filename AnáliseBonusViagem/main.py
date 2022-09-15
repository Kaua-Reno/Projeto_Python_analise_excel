import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC0a3073b1b998735d2b83c6938bd01542"
# Your Auth Token from twilio.com/console
auth_token  = "03912b72f1d324f06062610801c7164a"
client = Client(account_sid, auth_token)

# importar o pandas, o openpyxl e o twilio
# pip install -> para instalar
# Passo a passo da solução

# Abrir todos os arquivos Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendas'].values[0]
        print(f'No mês de {mes} o Vendedor {vendedor} bateu a meta com o total de {vendas} reais em vendas')
        message = client.messages.create(
            to="+5512992102543",
            from_="+18086467314",
            body=f'No mês de {mes} o Vendedor {vendedor} bateu a meta com o total de {vendas} reais em vendas')

        print(message.sid)



# Para cada arquivo:

# Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000

# Se for maior do que 55.00 -> Envia um SMS com o Nome, o mês e as vendas do vendedor
# Caso não haja ninguém com mais de 55.000, não vou fazer nada

