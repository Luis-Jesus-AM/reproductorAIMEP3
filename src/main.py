import flet as ft
from controllers.usercontroller import AuthController
from view.loginview import LoginView
from view.registroview import RegisterView  

def start(page: ft.Page):
    # Configuración de la ventana
    page.title = "Sistema SIGE"
    page.window_width = 450
    page.window_height = 700
    page.bgcolor = ft.Colors.LIGHT_BLUE_50
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Controlador de autenticación
    auth_ctrl = AuthController()

    # ------------------- Navegación -------------------
    def route_change(e):
        page.views.clear()

        if page.route == "/":
            page.views.append(LoginView(page, auth_ctrl))
        elif page.route == "/register": 
            page.views.append(RegisterView(page, auth_ctrl))
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

    # Eventos de navegación
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # Ruta inicial
    if page.route == "/":
        route_change(None)
    else:
        page.go("/")

# ------------------- Entry Point -------------------
def main():
    ft.app(target=start)

if __name__ == "__main__":
    main()
