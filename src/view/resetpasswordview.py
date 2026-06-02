import flet as ft

def resetpasswordview(page: ft.Page, reset_controller):
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
        # 1. Validaciones básicas
        if not nueva.value or not confirmar.value:
            mensaje.value = "⚠️ Completa ambos campos"
            page.update()
            return
        if nueva.value != confirmar.value:
            mensaje.value = "⚠️ Las contraseñas no coinciden"
            page.update()
            return

        # 2. Obtenemos el ID del usuario guardado en la sesión
        id_usuario = page.session.get("id_usuario")
        
        if not id_usuario:
            mensaje.value = "❌ Sesión expirada. Vuelve a intentar."
            page.update()
            return

        # 3. Actualizamos la contraseña
        # Ya no necesitamos validar el token aquí porque ya se validó en la vista anterior
        if reset_controller.actualizar_password(id_usuario, nueva.value):
            mensaje.value = "✅ Contraseña actualizada. Redirigiendo..."
            mensaje.color = "green"
            page.update()
            
            # Limpiamos sesión
            page.session.clear()
            page.go("/")
        else:
            mensaje.value = "❌ Error al actualizar la base de datos"
            page.update()

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