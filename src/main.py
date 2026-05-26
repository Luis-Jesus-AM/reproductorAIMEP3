import flet as ft

from controllers.usercontroller import AuthController
from controllers.resetcontroller import PasswordResetController

from view.loginview import LoginView
from view.registroview import RegisterView
from view.forgotpasswordview import forgotpasswordview
from view.resetpasswordview import resetpasswordview
from view.reproductorview import ReproductorView
from view.perfilview import PerfilView


def start(page: ft.Page):

    # =========================
    # CONFIGURACIÓN GENERAL
    # =========================
    page.title = "Reproductor MP3"
    page.window_width = 450
    page.window_height = 700
    page.bgcolor = "#121212"

    page.theme_mode = ft.ThemeMode.DARK

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # =========================
    # CONTROLADORES
    # =========================
    auth_ctrl = AuthController()
    reset_ctrl = PasswordResetController()

    # =========================
    # ROUTER
    # =========================
    def route_change(e):

        page.views.clear()

        # LOGIN
        if page.route == "/":
            page.views.append(
                LoginView(page, auth_ctrl)
            )

        # REGISTRO
        elif page.route == "/register":
            page.views.append(
                RegisterView(page, auth_ctrl)
            )

        # RECUPERAR PASSWORD
        elif page.route == "/forgot-password":
            page.views.append(
                forgotpasswordview(page, auth_ctrl, reset_ctrl)
            )

        # RESET PASSWORD
        elif page.route.startswith("/reset-password"):

            token = (
                page.route.split("token=")[-1]
                if "token=" in page.route
                else None
            )

            page.views.append(
                resetpasswordview(page, reset_ctrl, token)
            )

        # REPRODUCTOR
        elif page.route == "/reproductor":
            page.views.append(
                ReproductorView(page)
            )

        # PERFIL
        elif page.route == "/perfil":
            page.views.append(
                PerfilView(page)
            )

        # 404
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

    # =========================
    # BOTÓN ATRÁS
    # =========================
    def view_pop(e):

        if len(page.views) > 1:

            page.views.pop()

            top_view = page.views[-1]

            page.go(top_view.route)

    # =========================
    # EVENTOS
    # =========================
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # =========================
    # INICIO
    # =========================
    if page.route == "/":
        route_change(None)
    else:
        page.go("/")


def main():
    ft.app(target=start)


if __name__ == "__main__":
    main()