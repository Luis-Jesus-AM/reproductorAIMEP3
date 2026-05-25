import flet as ft

def LoginView(page: ft.Page, auth_controller):

    correo = ft.TextField(
        label="Correo electrónico",
        prefix_icon=ft.Icons.EMAIL,
        width=350,
        border_radius=8,
        border_color=ft.Colors.BLUE_300,
        keyboard_type=ft.KeyboardType.EMAIL,
    )

    contraseña = ft.TextField(
        label="Contraseña",
        prefix_icon=ft.Icons.LOCK,
        password=True,
        can_reveal_password=True,
        width=350,
        border_radius=8,
        border_color=ft.Colors.BLUE_300,
    )

    mensaje = ft.Text("", color="red")

    def mostrar_snackbar(mensaje_texto, color=ft.Colors.GREEN):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(mensaje_texto, size=16),
            bgcolor=color,
            duration=2500,
        )
        page.snack_bar.open = True
        page.update()

    def login_click(e):
        if not correo.value or not contraseña.value:
            mensaje.value = "⚠️ Por favor, llena todos los campos"
            mensaje.color = "red"
            page.update()
            return
        
        # 1. Llamamos al controlador pasándole 'page'
        user, msg = auth_controller.login(correo.value, contraseña.value, page)
        
        if user:
            page.user_data = user
            mostrar_snackbar("✅ Sesión iniciada correctamente", ft.Colors.GREEN)
            
            # 2. 🚨 ¡CORREGIDO AQUÍ! 
            # Cambiamos /dashboard por /reproductor para que coincida con tu nueva vista.
            # (Nota: Si ya pusiste page.go en el AuthController, puedes borrar o comentar esta línea de abajo)
            page.go("/reproductor")
        else:
            mensaje.value = msg
            mensaje.color = "red"
            page.update()

    iniciar_sesion = ft.ElevatedButton(
        "Ingresar",
        width=200,
        on_click=login_click,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.BLUE_400,
            color=ft.Colors.WHITE,
            padding=15,
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
    )
    
    btn_registro = ft.TextButton(
        "¿No tienes cuenta? Regístrate aquí",
        on_click=lambda _: page.go("/register"),
        style=ft.ButtonStyle(color=ft.Colors.BLUE_600)
    )

    btn_reset = ft.TextButton(
        "¿Olvidaste tu contraseña?",
        on_click=lambda _: page.go("/forgot-password"),
        style=ft.ButtonStyle(color=ft.Colors.BLUE_600)
    )
    
    contraseña.on_submit = login_click

    # Diseño con tarjeta central
    return ft.View(
        route="/",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        bgcolor=ft.Colors.LIGHT_BLUE_50,
        controls=[
            ft.Card(
                elevation=8,
                content=ft.Container(
                    width=400,
                    padding=25,
                    bgcolor="white",
                    border_radius=15,
                    content=ft.Column(
                        [
                            ft.Text("🔐 Iniciar Sesión", size=28, weight="bold", color="blue"),
                            ft.Divider(height=20, color="transparent"),
                            correo,
                            contraseña,
                            mensaje,
                            ft.Container(height=15),
                            ft.Row([iniciar_sesion], alignment=ft.MainAxisAlignment.CENTER),
                            ft.Container(height=10),
                            btn_registro,
                            btn_reset
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=12
                    )
                )
            )
        ]
    )