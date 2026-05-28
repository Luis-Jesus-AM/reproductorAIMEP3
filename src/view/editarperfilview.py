import flet as ft
from controllers.usercontroller import UserController # Importamos el controlador

class EditarPerfilView(ft.View):
    def __init__(self, page, usuario_actual):
        super().__init__(route="/editar-perfil")
        self.page = page
        self.usuario = usuario_actual # Guardamos el usuario para referencia
        self.user_ctrl = UserController() # Instancia del controlador
        
        # Campos de texto aesthetic
        self.input_nombre = ft.TextField(label="Nombre", value=usuario_actual["nombre"], border_radius=15, bgcolor="#1e1e1e")
        self.input_apellido = ft.TextField(label="Apellido", value=usuario_actual["apellido"], border_radius=15, bgcolor="#1e1e1e")
        self.input_email = ft.TextField(label="Email", value=usuario_actual["email"], border_radius=15, bgcolor="#1e1e1e")

        self.controls = [
            ft.Container(
                content=ft.Column([
                    ft.Text("Editar Perfil", size=24, weight="bold", color="white"),
                    self.input_nombre, 
                    self.input_apellido, 
                    self.input_email,
                    ft.ElevatedButton(
                        "Guardar Cambios", 
                        on_click=self.guardar_datos, 
                        bgcolor="#fe5f75", 
                        color="white"
                    )
                ], alignment="center", spacing=20),
                padding=40, width=400, bgcolor="#121212", border_radius=30
            )
        ]

    def guardar_datos(self, e):
        # 1. Llamar al controlador para ejecutar el UPDATE en la base de datos
        exito = self.user_ctrl.actualizar_usuario(
            id_usuario=self.usuario["id_usuario"],
            nombre=self.input_nombre.value,
            apellido=self.input_apellido.value,
            email=self.input_email.value
        )
        
        if exito:
            # 2. ACTUALIZAR LA SESIÓN para que los cambios se vean en el perfil
            usuario_actualizado = self.usuario.copy()
            usuario_actualizado.update({
                "nombre": self.input_nombre.value,
                "apellido": self.input_apellido.value,
                "email": self.input_email.value
            })
            self.page.session.set("user", usuario_actualizado)
            
            # 3. Notificar y regresar
            self.page.snack_bar = ft.SnackBar(ft.Text("✅ Cambios guardados con éxito"))
            self.page.snack_bar.open = True
            self.page.go("/perfil")
            self.page.update()
        else:
            self.page.snack_bar = ft.SnackBar(ft.Text("❌ Error al guardar en la base de datos"))
            self.page.snack_bar.open = True
            self.page.update()