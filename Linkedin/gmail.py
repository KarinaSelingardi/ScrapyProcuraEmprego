import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def enviar_email(como, para, assunto, mensagem, anexo=None):
    # Configuração do servidor SMTP
    smtp_host = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = 'fabianochupasseios2024@gmail.com'
    smtp_password = 'bigtits2024'

    # Cria um objeto MIMEMultipart
    email = MIMEMultipart()
    email['From'] = como
    email['To'] = para
    email['Subject'] = assunto

    # Adiciona o corpo da mensagem
    email.attach(MIMEText(mensagem, 'plain'))

    # Adiciona o anexo, se fornecido
    if anexo:
        with open(anexo, 'rb') as f:
            part = MIMEApplication(f.read(), Name='CurrículodeFabianoChuPasseios.docx')
        part['Content-Disposition'] = f'attachment; filename="{anexo}"'
        email.attach(part)

    # Conecta-se ao servidor SMTP
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        # Envia o e-mail
        server.send_message(email)

# Exemplo de uso
enviar_email('fabianochupasseios2024@gmail.com', 'k.selingardi@gmail.com', 'Minha Vaga', 'Me aceita por favor', '/workspaces/ScrapyProcuraEmprego/Linkedin/CurrículodeFabianoChuPasseios.docx')
