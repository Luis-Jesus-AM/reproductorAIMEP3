import bcrypt
from datetime import datetime
from model.databasemodel import Database


def actualizar_usuario(self, id_usuario, nombre=None, apellido=None, email=None, password=None):
        # ... (tu lógica de campos)
        
        # AGREGA ESTO:
        import os
        print(f"Ruta de trabajo actual: {os.getcwd()}")
        # Si usas sqlite, verifica la ruta de conexión en Database()
        
        # ... resto del código

class UserController:
    def __init__(self):
        self.db = Database()

    def registrar_usuario(self, nombre, apellido, email, password):
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")
        sql = """INSERT INTO usuarios (nombre, apellido, email, password, fecha_registro)
                VALUES (%s, %s, %s, %s, %s)"""
        return self.db.execute_query(sql, (nombre, apellido, email, hashed_pw, datetime.now()))

    def obtener_usuario_por_id(self, id_usuario):
        sql = "SELECT * FROM usuarios WHERE id_usuario=%s"
        return self.db.execute_query(sql, (id_usuario,), fetchone=True)

    def obtener_usuario_por_email(self, email):
        sql = "SELECT * FROM usuarios WHERE email=%s"
        return self.db.execute_query(sql, (email,), fetchone=True)

    def validar_login(self, email, password):
        user = self.obtener_usuario_por_email(email)
        if user and bcrypt.checkpw(password.encode("utf-8"), user["password"].encode("utf-8")):
            return user
        return None

    def actualizar_ultimo_acceso(self, id_usuario):
        sql = "UPDATE usuarios SET ultimo_acceso=%s WHERE id_usuario=%s"
        return self.db.execute_query(sql, (datetime.now(), id_usuario))

    def actualizar_usuario(self, id_usuario, nombre=None, apellido=None, email=None, password=None):
        campos, valores = [], []
        if nombre:
            campos.append("nombre=%s")
            valores.append(nombre)
        if apellido:
            campos.append("apellido=%s")
            valores.append(apellido)
        if email:
            campos.append("email=%s")
            valores.append(email)
        if password:
            salt = bcrypt.gensalt()
            hashed_pw = bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")
            campos.append("password=%s")
            valores.append(hashed_pw)


            

        if campos:
            sql = f"UPDATE usuarios SET {', '.join(campos)} WHERE id_usuario=%s"
            valores.append(id_usuario) 

            resultado = self.db.execute_query(sql, tuple(valores))


            return resultado is not False
            # El execute_query DEBE realizar conn.commit() internamente
           
        return False

    def eliminar_usuario(self, id_usuario):
        sql = "DELETE FROM usuarios WHERE id_usuario=%s"
        return self.db.execute_query(sql, (id_usuario,))

class AuthController:
    def __init__(self):
        self.user_ctrl = UserController()

    def login(self, email, password, page=None):
        user_db = self.user_ctrl.validar_login(email, password)
        if not user_db:
            return None, "Correo o contraseña incorrectos"
        self.user_ctrl.actualizar_ultimo_acceso(user_db["id_usuario"])
        user_db_actualizado = self.user_ctrl.obtener_usuario_por_id(user_db["id_usuario"])
        user = {
            "id_usuario": user_db_actualizado["id_usuario"],
            "nombre": user_db_actualizado["nombre"],
            "apellido": user_db_actualizado["apellido"],
            "email": user_db_actualizado["email"],
            "fecha_registro": user_db_actualizado["fecha_registro"],
            "ultimo_acceso": user_db_actualizado["ultimo_acceso"],
        }
        return user, "Login exitoso"

    def registrar(self, usuario_data):
        if self.user_ctrl.obtener_usuario_por_email(usuario_data.email):
            return False, "El correo electrónico ya está registrado"
        exito = self.user_ctrl.registrar_usuario(usuario_data.nombre, usuario_data.apellido, usuario_data.email, usuario_data.password)
        return (True, "Usuario registrado") if exito else (False, "Error al registrar")