import flet as ft

from controllers.usercontroller import AuthController
from controllers.resetcontroller import PasswordResetController

from view.loginview import LoginView
from view.registroview import RegisterView
from view.forgotpasswordview import forgotpasswordview
from view.resetpasswordview import resetpasswordview
from view.reproductorview import ReproductorView
from view.perfilview import PerfilView
from view.editarperfilview import EditarPerfilView

def start(page: ft.Page):


    page.title = "Reproductor MP3"
    page.window.width = 450
    page.window.height = 700
    page.bgcolor = "#121212"

    page.theme_mode = ft.ThemeMode.DARK

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


    auth_ctrl = AuthController()
    reset_ctrl = PasswordResetController()


    def route_change(e):

        page.views.clear()

        if page.route == "/":
            page.views.append(
                LoginView(page, auth_ctrl)
            )


        elif page.route == "/register":
            page.views.append(
                RegisterView(page, auth_ctrl)
            )

        elif page.route == "/forgot-password":
            page.views.append(
                forgotpasswordview(page, auth_ctrl, reset_ctrl)
            )

        elif page.route.startswith("/reset-password"):

            token = (
                page.route.split("token=")[-1]
                if "token=" in page.route
                else None
            )

            page.views.append(
                resetpasswordview(page, reset_ctrl, token)
            )


        elif page.route == "/reproductor":
            page.views.append(
                ReproductorView(page)
            )


        elif page.route == "/perfil":
            page.views.append(
                PerfilView(page)
            )
            
        elif page.route == "/editar-perfil":
            # Corrección: Se pasa el usuario desde la sesión para el __init__
            usuario = page.session.get("user")
            page.views.append(
                EditarPerfilView(page, usuario)
            )


        else:
            page.views.append(
                ft.View(
                    route=page.route,
                    bgcolor="#121212",
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(
                            ft.Icons.ERROR_OUTLINE,
                            color=ft.Colors.RED_400,
                            size=70
                        ),

                        ft.Text(
                            "Ruta no encontrada",
                            size=24,
                            weight=ft.FontWeight.BOLD,
                            color="white"
                        ),

                        ft.Text(
                            f"La ruta '{page.route}' no existe.",
                            color="#b3b3b3"
                        ),

                        ft.ElevatedButton(
                            "Volver al inicio",
                            icon=ft.Icons.HOME,
                            on_click=lambda _: page.go("/"),
                            style=ft.ButtonStyle(
                                bgcolor="#fe5f75",
                                color="white"
                            )
                        )
                    ]
                )
            )

        page.update()


    def view_pop(e):

        if len(page.views) > 1:

            page.views.pop()

            top_view = page.views[-1]

            page.go(top_view.route)


    page.on_route_change = route_change
    page.on_view_pop = view_pop


    if page.route == "/":
        route_change(None)
    else:
        page.go("/")


def main():
    ft.app(target=start)


if __name__ == "__main__":
    main()