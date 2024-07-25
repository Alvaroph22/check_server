import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os


load_dotenv()

def check_server_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"El servidor en {url} está activo y respondió con el código de estado 200.")
        else:
            print(f"El servidor en {url} respondió con el código de estado {response.status_code}.")
            send_email_notification(url, response.status_code)
    except requests.exceptions.RequestException as e:
        print(f"No se pudo conectar al servidor en {url}. Error: {e}")
        send_email_notification(url, e)

def send_email_notification(url, error):
    sender_email = os.getenv("EMAIL_SENDER")
    sender_password = os.getenv("EMAIL_PASSWORD")
    recipient_email = os.getenv("EMAIL_RECICPIENT")

    subject = f"Problema con el servidor: {url}"
    body = f"El servidor en {url} no respondió correctamente.\n\nError: {error}"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())
        server.quit()
        print(f"Notificación de correo enviada a {recipient_email}.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

if __name__ == "__main__":
    url = "https://recibeypaga.com.co"
    check_server_status(url)
