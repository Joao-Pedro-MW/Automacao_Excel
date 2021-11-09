import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("E-mail@gmail.com", "Senha_de_login_de_apps")
server.sendmail(
  "E-mail@gmail.com",
  "E-mail_de_envio@gmail.com",
  "Texto da mensage")
server.quit()
