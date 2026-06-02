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
    
    # Campo nuevo para el código
    codigo_input = ft.TextField(
        label="Código de verificación",
        prefix_icon=ft.Icons.LOCK_CLOCK,
        width=350,
        border_radius=8,
        visible=False # Inicialmente oculto
    )
    
    mensaje = ft.Text("", color="red")

    def enviar_reset(e):
        # ESTADO 1: Enviar código
        if btn_enviar.text == "Enviar código":
            if not email.value:
                mensaje.value = "⚠️ Ingresa tu correo"
                page.update()
                return

            usuario = auth_controller.user_ctrl.obtener_usuario_por_email(email.value)
            if not usuario:
                mensaje.value = "⚠️ Correo no registrado"
                page.update()
                return

            # Generamos el token (código)
            token = reset_controller.crear_token(usuario["id_usuario"])
            reset_controller.enviar_correo_reset(email.value, token)
            
            # Cambiamos la interfaz para pedir el código
            mensaje.value = "✅ Código enviado. Revísalo en tu correo."
            mensaje.color = "green"
            codigo_input.visible = True
            btn_enviar.text = "Validar código"
            page.update()

        # ESTADO 2: Validar código
        else:
            token_data = reset_controller.validar_token(codigo_input.value)
            if token_data:
                # Guardamos el ID en la sesión para usarlo en la siguiente vista
                page.session.set("id_usuario", token_data["id_usuario"])
                page.session.set("token_valido", codigo_input.value)
                
                # Navegamos a la vista de reset
                page.go("/reset-password")
            else:
                mensaje.value = "❌ Código inválido o expirado"
                mensaje.color = "red"
                page.update()

    btn_enviar = ft.ElevatedButton("Enviar código", on_click=enviar_reset)

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
                            codigo_input, # El campo nuevo
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