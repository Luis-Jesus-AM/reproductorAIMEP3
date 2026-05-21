import flet as ft

def forgotpasswordview(page: ft.Page, auth_controller, reset_controller):
    email = ft.TextField(
        label="Correo electrónico",
        prefix_icon=ft.Icons.EMAIL,
        width=350,
        border_radius=8,
        border_color=ft.Colors.BLUE_300,
        keyboard_type=ft.KeyboardType.EMAIL
    )
    mensaje = ft.Text("", color="red")

    def enviar_reset(e):
        if not email.value:
            mensaje.value = "⚠️ Ingresa tu correo"
            mensaje.color = "red"
            page.update()
            return

        usuario = auth_controller.user_ctrl.obtener_usuario_por_email(email.value)
        if not usuario:
            mensaje.value = "⚠️ Correo no registrado"
            mensaje.color = "red"
            page.update()
            return

        token = reset_controller.crear_token(usuario["id_usuario"])
        reset_controller.enviar_correo_reset(email.value, token)
        mensaje.value = "✅ Revisa tu correo. El enlace expira en 5 minutos."
        mensaje.color = "green"
        page.update()

    btn_enviar = ft.ElevatedButton("Enviar enlace", on_click=enviar_reset)

    return ft.View(
        route="/forgot-password",
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
                            ft.Text("🔑 Recuperar contraseña", size=24, weight="bold", color="blue"),
                            email,
                            mensaje,
                            ft.Container(height=15),
                            btn_enviar,
                            ft.TextButton("Volver al login", on_click=lambda _: page.go("/"))
                        ],
                        spacing=12,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    )
                )
            )
        ]
    )
