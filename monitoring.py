import os
import hashlib
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client

# Configurações de e-mail
EMAIL_FROM = "seu_email@gmail.com"
EMAIL_PASSWORD = "sua_senha"
EMAIL_TO = "destinatario@example.com"
EMAIL_SUBJECT = "Alerta: Mudança de Integridade de Arquivo"

# Configurações do Twilio
TWILIO_SID = "your_twilio_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE_NUMBER = "your_twilio_phone_number"
DESTINATION_PHONE_NUMBER = "destination_phone_number"

# Configurações de log
LOG_FILE = "integrity_log.txt"
MAX_LOG_ENTRIES = 100

def send_email(subject, body):
    """Envia um e-mail de alerta."""
    msg = MIMEMultipart()
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL_FROM, EMAIL_PASSWORD)
    server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    server.quit()

def send_sms(message):
    """Envia uma mensagem de texto usando o Twilio."""
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,
        to=DESTINATION_PHONE_NUMBER
    )

def calculate_hash(file_path):
    """Calcula o hash MD5 de um arquivo."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def log_change(file_path):
    """Registra uma alteração no log."""
    with open(LOG_FILE, "a") as log:
        log.write(f"{time.ctime()}: Arquivo {file_path} foi alterado.\n")

    # Limita o número de entradas no log
    with open(LOG_FILE, "r") as log:
        lines = log.readlines()
        if len(lines) > MAX_LOG_ENTRIES:
            with open(LOG_FILE, "w") as log:
                log.writelines(lines[-MAX_LOG_ENTRIES:])

def generate_html_report(file_changes):
    """Gera um relatório HTML das alterações."""
    report = """
    <html>
    <head><title>Relatório de Alterações de Integridade de Arquivo</title></head>
    <body>
    <h1>Relatório de Alterações de Integridade de Arquivo</h1>
    <ul>
    """

    for file_path, timestamp in file_changes.items():
        report += f"<li>{time.ctime(timestamp)}: Arquivo {file_path} foi alterado.</li>"

    report += """
    </ul>
    </body>
    </html>
    """

    return report

def monitor_directory(directory_path, interval):
    """Monitora um diretório em busca de alterações em arquivos."""
    file_hashes = {}
    file_changes = {}

    while True:
        for root, _, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_hash = calculate_hash(file_path)

                if file_path in file_hashes:
                    if file_hashes[file_path] != file_hash:
                        print(f"Alerta: Arquivo {file_path} foi alterado!")
                        send_email(EMAIL_SUBJECT, f"O arquivo {file_path} foi alterado.")
                        send_sms(f"Alerta: Arquivo {file_path} foi alterado!")
                        log_change(file_path)
                        file_changes[file_path] = time.time()
                        file_hashes[file_path] = file_hash
                else:
                    file_hashes[file_path] = file_hash

        # Gera um relatório HTML das alterações
        report = generate_html_report(file_changes)

        # Salva o relatório em um arquivo
        with open("integrity_report.html", "w") as report_file:
            report_file.write(report)

        time.sleep(interval)

if __name__ == "__main__":
    monitored_directory = "/path/to/your/directory"
    check_interval = 5  # Intervalo de verificação em segundos

    print(f"Monitorando diretório: {monitored_directory}")
    monitor_directory(monitored_directory, check_interval)
