import flet as ft

def resetpasswordview(page: ft.Page, reset_controller, token):
    nueva = ft.TextField(
        label="Nueva contraseña",
        prefix_icon=ft.Icons.LOCK,
        password=True,
        can_reveal_password=True,
        width=350,
        border_radius=8,
        border_color=ft.Colors.BLUE_300
    )
    confirmar = ft.TextField(
        label="Confirmar contraseña",
        prefix_icon=ft.Icons.LOCK,
        password=True,
        can_reveal_password=True,
        width=350,
        border_radius=8,
        border_color=ft.Colors.BLUE_300
    )
    mensaje = ft.Text("", color="red")

    def cambiar_password(e):
        if not nueva.value or not confirmar.value:
            mensaje.value = "⚠️ Completa ambos campos"
            mensaje.color = "red"
            page.update()
            return
        if nueva.value != confirmar.value:
            mensaje.value = "⚠️ Las contraseñas no coinciden"
            mensaje.color = "red"
            page.update()
            return

        token_data = reset_controller.validar_token(token)
        if not token_data:
            mensaje.value = "❌ Token inválido o expirado"
            mensaje.color = "red"
            page.update()
            return

        reset_controller.actualizar_password(token_data["id_usuario"], nueva.value)
        mensaje.value = "✅ Contraseña actualizada correctamente. Ahora puedes iniciar sesión."
        mensaje.color = "green"
        page.update()
        page.go("/")

    btn_cambiar = ft.ElevatedButton("Cambiar contraseña", on_click=cambiar_password)

    return ft.View(
        route="/reset-password",
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
                            ft.Text("🔒 Nueva contraseña", size=24, weight="bold", color="blue"),
                            nueva,
                            confirmar,
                            mensaje,
                            ft.Container(height=15),
                            btn_cambiar
                        ],
                        spacing=12,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    )
                )
            )
        ]
    )
