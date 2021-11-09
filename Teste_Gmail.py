import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("jpedro01230@gmail.com", "ggcurgnzefufudqo")
server.sendmail(
  "jpedro01230@gmail.com",
  "wilges.joao@escola.pr.gov.br",
  "teste")
server.quit()


"""from pyautogui import *
from time import sleep
import pyautogui as pgui
# clica no chrome
pgui.click(x=737, y=751)
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
pgui.press("c")"""