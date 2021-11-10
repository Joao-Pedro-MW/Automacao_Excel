# Excel para Email
#### Oque o programa faz? <br>
Ele "lê" todos os dados nas colunas A e B (fiz em minha planilha de testes) e conforme nome e e-mail informados, faz o envio automático de um rementente para os e-mails, informando em um texto o nome do destinatário :) <br>
* Arquivos necessários: <br>
Uma planilha Excel (formato xlsx/xlsm/xltx/xltm), todas as linhas devem estar preenchidas (as que tiverem dados), pois uma é para o nome do destinatário e 
a outra fica com o e-mail sem o arquivo SMPT.py o programa Excel.py não irá funcionar.
* Mensagem no e-mail: <br>
A mensagem deve ser editada no arquivo SMTP, nos dois campos (o de texto comum e o HTML), o HTML é apenas necessário para deixar mais bonito visualmente
### ! Observações importantes !
Não modifique o código para manter a senha sempre nele (ou faça, a segurança é sua). <br>
O sistema usa o protocolo SMTP com criptografia TLS, então ele é bem seguro. <br>
Caso você queira testá-lo, você tem 2 opções: <br>
Ativar o acesso não seguro à apps (Não recomendado) <br>
ou <br>
Usar sua conta com autenticação de dois fatores e criar uma senha para aplicativos
<br>
<br>
<br>
NÃO USE MAIS DE 100 DESTINATÁRIOS (Sua conta Gmail pode ser bloqueada por políticas de spam que a Google usa)
