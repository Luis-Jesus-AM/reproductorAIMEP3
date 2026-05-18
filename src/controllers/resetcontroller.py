import secrets
import bcrypt
from datetime import datetime, timedelta
import smtplib, ssl
from email.message import EmailMessage
from model.databasemodel import Database   # ojo: usa "models", no "model"

class PasswordResetController:
    def __init__(self, db=None):
        self.db = db or Database()

    # ------------------- CREAR TOKEN -------------------
    def crear_token(self, id_usuario):
        token = secrets.token_urlsafe(32)
        expira = datetime.now() + timedelta(minutes=15)
        sql = "INSERT INTO reset_tokens (id_usuario, token, expira) VALUES (%s, %s, %s)"
        self.db.execute_query(sql, (id_usuario, token, expira))
        return token

    # ------------------- VALIDAR TOKEN -------------------
    def validar_token(self, token):
        sql = "SELECT * FROM reset_tokens WHERE token=%s AND expira > %s"
        return self.db.execute_query(sql, (token, datetime.now()), fetchone=True)

    # ------------------- ACTUALIZAR PASSWORD -------------------
    def actualizar_password(self, id_usuario, nueva_password):
        hashed_pw = bcrypt.hashpw(nueva_password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        sql = "UPDATE usuarios SET password=%s WHERE id_usuario=%s"
        self.db.execute_query(sql, (hashed_pw, id_usuario))
        # eliminar token usado
        self.db.execute_query("DELETE FROM reset_tokens WHERE id_usuario=%s", (id_usuario,))
        return True

    # ------------------- ENVIAR CORREO -------------------
    def enviar_correo_reset(self, destinatario, token):
        smtp_server = "smtp.gmail.com"
        port = 465
        remitente = "tucorreo@gmail.com"
        password = "tu_app_password"  # usa App Password si tienes 2FA

        mensaje = EmailMessage()
        mensaje["From"] = remitente
        mensaje["To"] = destinatario
        mensaje["Subject"] = "Recuperación de contraseña - SIGE"

        enlace = f"http://localhost:8000/reset-password?token={token}"
        mensaje.set_content(
            f"""
Hola,

Recibimos una solicitud para restablecer tu contraseña.
Haz clic en el siguiente enlace para continuar:

{enlace}

Este enlace expirará en 15 minutos.

Si no solicitaste el cambio, ignora este correo.
"""
        )

        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(remitente, password)
                server.send_message(mensaje)
            print("✅ Correo de recuperación enviado correctamente")
            return True
        except Exception as e:
            print(f"❌ Error enviando correo: {e}")
            return False
