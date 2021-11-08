from openpyxl import *
from pyautogui import *
from time import sleep
import pyautogui as pgui
#abrir o arquivo
nomes = list()
emails = list()
caminho = "C:/Users/USUARIO/OneDrive/Área de Trabalho/Pycel/Data.xlsx"
planilha = load_workbook(caminho)
planilha = planilha["Nomes"]
for row in planilha.iter_rows(min_row=1, max_row=300, min_col=1, max_col=1,values_only=True):
#este loop acessa os valores na primeira coluna
    for cell in row: 
        # com o parametro FOR CELL IN ROW, convertemos para String os dados
        #sem o parametro os dados são retornados em tuple
        nomes.append(cell)
for col in planilha.iter_cols(min_col= 2, max_col=2, max_row=300, values_only=True):
    #este loop acessa os valores na segunda coluna
    for cell in col:
        emails.append(cell)

#print(emails)
#print(nomes)
#abre o gmail pra enviar o arquivo
pgui.hotkey('win','r')
pgui.write("chrome")
pgui.press("enter")
sleep(2)
#clica no perfil
pgui.click(x=595, y=410)
sleep(2)
pgui.hotkey('ctrl', 't') 
sleep(1)
pgui.write("gmail.com")
sleep(1)
pgui.press("enter")
sleep(6)
pgui.press("c")