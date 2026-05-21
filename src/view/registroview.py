import flet as ft
import re
from model.schemasmodel import UsuarioSchema   # corregido

def RegisterView(page: ft.Page, auth_controller):
    
    nombre = ft.TextField(
        label="Nombre(s)",
        prefix_icon=ft.Icons.PERSON,
        width=350,
        border_radius=8,
        border_color=ft.Colors.BLUE_300
    )
    
    apellido = ft.TextField(
        label="Apellidos",
        prefix_icon=ft.Icons.PERSON,
        width=350,
        border_radius=8,
        border_color=ft.Colors.BLUE_300
    )
    
    email = ft.TextField(
        label="Correo electrónico",
        prefix_icon=ft.Icons.EMAIL,
        width=350,
        border_radius=8,
        border_color=ft.Colors.BLUE_300,
        keyboard_type=ft.KeyboardType.EMAIL
    )
    
    password = ft.TextField(
        label="Contraseña",
        prefix_icon=ft.Icons.LOCK,
        password=True,
        can_reveal_password=True,
        width=350,
        border_radius=8,
        border_color=ft.Colors.BLUE_300
    )
    
    confirm_password = ft.TextField(
        label="Confirmar contraseña",
        prefix_icon=ft.Icons.LOCK,
        password=True,
        can_reveal_password=True,
        width=350,
        border_radius=8,
        border_color=ft.Colors.BLUE_300
    )
    
    mensaje = ft.Text("", color="red", size=12)
    
    def mostrar_snackbar(mensaje_texto, color=ft.Colors.GREEN):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(mensaje_texto, size=16),
            bgcolor=color,
            duration=2500,
        )
        page.snack_bar.open = True
        page.update()
    
    def registrar_click(e):
        if not nombre.value or not apellido.value or not email.value or not password.value or not confirm_password.value:
            mensaje.value = "⚠️ Todos los campos son obligatorios"
            mensaje.color = "red"
            page.update()
            return
        
        if password.value != confirm_password.value:
            mensaje.value = "⚠️ Las contraseñas no coinciden"
            mensaje.color = "red"
            page.update()
            return
        
        if len(password.value) < 6:
            mensaje.value = "⚠️ La contraseña debe tener al menos 6 caracteres"
            mensaje.color = "red"
            page.update()
            return
        
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email.value):
            mensaje.value = "⚠️ Correo electrónico inválido"
            mensaje.color = "red"
            page.update()
            return
        
        usuario_data = UsuarioSchema(
            nombre=nombre.value,
            apellido=apellido.value,
            email=email.value,
            password=password.value
        )
        
        exito, msg = auth_controller.registrar(usuario_data)
        
        if exito:
            mostrar_snackbar("✅ ¡Registro exitoso! Ahora inicia sesión", ft.Colors.GREEN)
            nombre.value = apellido.value = email.value = password.value = confirm_password.value = ""
            mensaje.value = ""
            page.update()
            page.go("/")
        else:
            mensaje.value = msg or "❌ Error al registrar usuario"
            mensaje.color = "red"
            page.update()
    
    btn_registrar = ft.ElevatedButton(
        "Crear cuenta",
        width=200,
        on_click=registrar_click,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.BLUE_400,
            color=ft.Colors.WHITE,
            padding=15,
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
    )
    
    btn_login = ft.TextButton(
        "¿Ya tienes cuenta? Inicia sesión",
        on_click=lambda _: page.go("/"),
        style=ft.ButtonStyle(color=ft.Colors.BLUE_600)
    )
    
    return ft.View(
        route="/register",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        bgcolor=ft.Colors.LIGHT_BLUE_50,
        controls=[
            ft.Card(
                elevation=8,
                content=ft.Container(
                    width=420,
                    padding=25,
                    bgcolor="white",
                    border_radius=15,
                    content=ft.Column(
                        [
                            ft.Text("📝 Registro de Usuario", size=28, weight="bold", color="blue"),
                            ft.Divider(height=20, color="transparent"),
                            nombre,
                            apellido,
                            email,
                            password,
                            confirm_password,
                            mensaje,
                            ft.Container(height=15),
                            ft.Row([btn_registrar], alignment=ft.MainAxisAlignment.CENTER),
                            ft.Container(height=10),
                            btn_login
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=12
                    )
                )
            )
        ]
    )
