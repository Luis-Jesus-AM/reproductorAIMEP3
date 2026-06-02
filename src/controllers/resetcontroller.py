import random
import bcrypt
from datetime import datetime, timedelta
import smtplib, ssl
from email.message import EmailMessage
from model.databasemodel import Database

class PasswordResetController:
    def __init__(self, db=None):
        self.db = db or Database()

  
    def crear_token(self, id_usuario):
      
        self.db.execute_query("DELETE FROM reset_tokens WHERE id_usuario=%s", (id_usuario,))
        
      
        codigo = str(random.randint(100000, 999999))
        expira = datetime.now() + timedelta(minutes=5)
        
        sql = "INSERT INTO reset_tokens (id_usuario, token, expira) VALUES (%s, %s, %s)"
        self.db.execute_query(sql, (id_usuario, codigo, expira))
        return codigo

    
    def validar_token(self, token):
       
        sql = "SELECT * FROM reset_tokens WHERE token=%s AND expira > %s"
        return self.db.execute_query(sql, (token, datetime.now()), fetchone=True)

   
    def actualizar_password(self, id_usuario, nueva_password):
        hashed_pw = bcrypt.hashpw(nueva_password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        sql = "UPDATE usuarios SET password=%s WHERE id_usuario=%s"
        self.db.execute_query(sql, (hashed_pw, id_usuario))
        
     
        self.db.execute_query("DELETE FROM reset_tokens WHERE id_usuario=%s", (id_usuario,))
        return True

   
    def enviar_correo_reset(self, destinatario, codigo):
        smtp_server = "smtp.gmail.com"
        port = 465
        remitente = "shimurat736@gmail.com"
        password = "lpox kwzc ckyd goyx" 

        mensaje = EmailMessage()
        mensaje["From"] = remitente
        mensaje["To"] = destinatario
        mensaje["Subject"] = "Código de recuperación - SIGE"

        mensaje.set_content(
            f"""
Hola,

Hemos recibido una solicitud para restablecer tu contraseña.
Tu código de verificación es: {codigo}

Este código es válido solo por 5 minutos.

Si no solicitaste el cambio, ignora este correo.
"""
        )

        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(remitente, password)
                server.send_message(mensaje)
            print("✅ Código de recuperación enviado correctamente")
            return True
        except Exception as e:
            print(f"❌ Error enviando correo: {e}")
            return False