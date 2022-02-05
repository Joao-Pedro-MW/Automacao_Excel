import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import messagebox

def enviar_email(remetente,destinatario,senha_login,assunto,nome_remetente):
  message = MIMEMultipart("alternative")
  message["Subject"] = assunto
  message["From"] = remetente
  message["To"] = destinatario
  # Crie o texto padrão em o texto em HTML
  text = """\
  Olá {nome}, tudo bem?
  Seu cadastro está em análise em noso banco de dados :D"""
  html = """\
  <html>
    <body>
      <p>Olá {nome}, tudo bem?<br>
        Seu cadastro está em análise em nosso banco de dados :D</p>
    </body>
  </html>
  """.format(nome = nome_remetente)
  # Converta para texto normal (plain)  e html
  part1 = MIMEText(text, "plain")
  part2 = MIMEText(html, "html")
  # Anexe as mensagem do e-mail, a ultima parte é renderizada primeiro
  message.attach(part1)
  message.attach(part2)
  # Cria uma conexão segura com o servidor e envia o e-mail
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
      try:
        server.login(remetente, senha_login)
        try:
          server.sendmail(remetente, destinatario, message.as_string())
        except TypeError:
          messagebox.showerror("ERRO NA CÉLULA DA PLANILHA","Verifique se a planilha está preenchida corretamente")
          pass
      except smtplib.SMTPAuthenticationError:
        messagebox.showerror("Erro de login", "Login e/ou senha inválidos")
        pass
