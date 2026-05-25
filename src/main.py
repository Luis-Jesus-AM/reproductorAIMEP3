import flet as ft
from controllers.usercontroller import AuthController
from controllers.resetcontroller import PasswordResetController 
from view.loginview import LoginView
from view.registroview import RegisterView  
from view.forgotpasswordview import forgotpasswordview
from view.resetpasswordview import resetpasswordview
from view.reproductorview import  ReproductorView

def start(page: ft.Page):
    
    page.title = "Reproductor MP3"
    page.window_width = 450
    page.window_height = 700
    page.bgcolor = ft.Colors.LIGHT_BLUE_50
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # 🔹 Inicializar controladores (solo una vez)
    auth_ctrl = AuthController()
    reset_ctrl = PasswordResetController()

    def route_change(e):
        page.views.clear()

        if page.route == "/":
            page.views.append(LoginView(page, auth_ctrl))
        elif page.route == "/register": 
            page.views.append(RegisterView(page, auth_ctrl))
        elif page.route == "/forgot-password":
            page.views.append(forgotpasswordview(page, auth_ctrl, reset_ctrl))
        elif page.route.startswith("/reset-password"):
            token = page.route.split("token=")[-1] if "token=" in page.route else None
            page.views.append(resetpasswordview(page, reset_ctrl, token))
        else:
            page.views.append(
                ft.View("/", [
                    ft.Text("⚠️ Error: Ruta no encontrada", color="red", size=18)
                ])
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
