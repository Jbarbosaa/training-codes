import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

def verificar_chamados():
    # URL da página onde a fila de chamados está localizada
    url = "URL_DA_SUA_EMPRESA_AQUI"

    # Faz a solicitação GET para obter o conteúdo da página
    response = requests.get(url)

    # Verifica se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Analisa o HTML da página
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontra o elemento que contém o número de chamados na fila
        fila_element = soup.find("div", class_="fila-de-chamados")

        # Extrai o número de chamados da fila
        numero_chamados = fila_element.text.strip()

        # Verifica se há novos chamados comparando com a última contagem
        if numero_chamados != verificar_chamados.ultimo_numero_chamados:
            enviar_notificacao(numero_chamados)
        
        # Atualiza o último número de chamados verificado
        verificar_chamados.ultimo_numero_chamados = numero_chamados

def enviar_notificacao(numero_chamados):
    # Configurações do servidor SMTP para envio de e-mails
    servidor_smtp = "smtp.example.com"
    porta_smtp = 587
    email_usuario = "seu_email@example.com"
    senha = "sua_senha"

    # Configuração do e-mail
    destinatario = "destinatario@example.com"
    assunto = "Novo chamado na fila!"
    corpo = f"O número de chamados na fila é agora: {numero_chamados}"

    # Cria o objeto Multipart
    msg = MIMEMultipart()
    msg['From'] = email_usuario
    msg['To'] = destinatario
    msg['Subject'] = assunto

    # Adiciona o corpo do e-mail
    msg.attach(MIMEText(corpo, 'plain'))

    # Inicia uma conexão SMTP segura
    servidor = smtplib.SMTP(servidor_smtp, porta_smtp)
    servidor.starttls()

    # Faça login no servidor SMTP
    servidor.login(email_usuario, senha)

    # Envia o e-mail
    servidor.sendmail(email_usuario, destinatario, msg.as_string())

    # Encerra a conexão com o servidor SMTP
    servidor.quit()

# Define o último número de chamados verificado como vazio inicialmente
verificar_chamados.ultimo_numero_chamados = ""

# Define o intervalo de tempo em segundos para verificar os chamados
intervalo = 60  # Verificar a cada 1 minuto

while True:
    verificar_chamados()
    time.sleep(intervalo)
