import bcrypt
from datetime import datetime
from model.databasemodel import Database  

class UsuarioModel:
    def __init__(self):
        self.db = Database()

    def _execute_query(self, query, params=None, fetchone=False, fetchall=False):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(query, params or ())
            if fetchone:
                result = cursor.fetchone()
            elif fetchall:
                result = cursor.fetchall()
            else:
                conn.commit()
                result = True
            return result
        except Exception as e:
            print(f"Error en consulta: {e}")
            return None
        finally:
            cursor.close()
            conn.close()

    def email_existe(self, email):
        query = "SELECT id_usuario FROM usuarios WHERE email=%s"
        result = self._execute_query(query, (email,), fetchone=True)
        return result is not None

    def registrar(self, usuario_data):
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(usuario_data.password.encode("utf-8"), salt).decode("utf-8")

        query = """INSERT INTO usuarios (nombre, apellido, email, password, fecha_registro)
                VALUES (%s, %s, %s, %s, %s)"""
        params = (usuario_data.nombre, usuario_data.apellido,
                usuario_data.email, hashed_pw, datetime.now())
        return self._execute_query(query, params)

    def validar_login(self, email, password):
        query = "SELECT * FROM usuarios WHERE email=%s"
        user = self._execute_query(query, (email,), fetchone=True)

        if user and bcrypt.checkpw(password.encode("utf-8"), user["password"].encode("utf-8")):
            return user
        return None

    def actualizar_ultimo_acceso(self, id_usuario):
        query = "UPDATE usuarios SET ultimo_acceso=%s WHERE id_usuario=%s"
        params = (datetime.now(), id_usuario)
        return self._execute_query(query, params)

    def obtener_por_id(self, id_usuario):
        query = "SELECT * FROM usuarios WHERE id_usuario=%s"
        return self._execute_query(query, (id_usuario,), fetchone=True)

    def obtener_todos(self):
        query = "SELECT id_usuario, nombre, apellido, email, fecha_registro, ultimo_acceso FROM usuarios"
        return self._execute_query(query, fetchall=True)

    def eliminar(self, id_usuario):
        query = "DELETE FROM usuarios WHERE id_usuario=%s"
        return self._execute_query(query, (id_usuario,))
    
    def actualizar_perfil(self, id_usuario, nombre, apellido, email):
        query = "UPDATE usuarios SET nombre=%s, apellido=%s, email=%s WHERE id_usuario=%s"
        return self._execute_query(query, (nombre, apellido, email, id_usuario))
