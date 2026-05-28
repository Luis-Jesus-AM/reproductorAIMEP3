import flet as ft

def ReproductorView(page: ft.Page):
    nombre_usuario = "Usuario"
    inicial_usuario = "U"

    # --- LÓGICA DE FUNCIONES ---
    def confirmar_eliminar_click(e):
        dialogo_confirmacion.open = False
        page.update()
        page.go("/")
        page.snack_bar = ft.SnackBar(content=ft.Text("🔥 Cuenta eliminada"), bgcolor=ft.Colors.RED_400)
        page.snack_bar.open = True
        page.update()

    def cancelar_eliminar_click(e):
        dialogo_confirmacion.open = False
        page.update()

    dialogo_confirmacion = ft.AlertDialog(
        modal=True,
        title=ft.Text("⚠ ¿Eliminar tu cuenta?"),
        content=ft.Text("Esta acción es permanente."),
        actions=[
            ft.TextButton("Cancelar", on_click=cancelar_eliminar_click),
            ft.TextButton("Sí, eliminar", icon=ft.Icons.DELETE_FOREVER, icon_color="red", on_click=confirmar_eliminar_click),
        ],
    )

    def menu_item_click(e):
        if e.control.data == "eliminar":
            page.dialog = dialogo_confirmacion
            dialogo_confirmacion.open = True
            page.update()

    # --- MENÚ PERFIL ---
    perfil_menu = ft.PopupMenuButton(
        content=ft.CircleAvatar(
            content=ft.Text(inicial_usuario, color="white", weight="bold"),
            bgcolor="#fe5f75",
            radius=18
        ),
        items=[
            ft.PopupMenuItem(
                content=ft.Row([ft.Icon(ft.Icons.PERSON), ft.Text("Ver Perfil")]),
                on_click=lambda e: page.go("/perfil")
            ),
            ft.PopupMenuItem(ft.Divider()),
            ft.PopupMenuItem(
                content=ft.Row([ft.Icon(ft.Icons.DELETE_OUTLINED, color="red"), ft.Text("Eliminar Cuenta", color="red")]),
                data="eliminar",
                on_click=menu_item_click
            ),
        ]
    )

    # --- ELEMENTOS DEL REPRODUCTOR ---
    portada = ft.Container(
        content=ft.Icon(ft.Icons.MUSIC_NOTE_ROUNDED, size=80, color="#ffffff"),
        gradient=ft.LinearGradient(begin=ft.alignment.top_left, end=ft.alignment.bottom_right, colors=["#fe5f75", "#fc9842"]),
        width=260, height=260, border_radius=35,
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=20, color=ft.Colors.with_opacity(0.4, "#fe5f75")),
    )

    reproductor_tarjeta = ft.Container(
        content=ft.Column([
            portada,
            ft.Column([
                ft.Text("Midnight City", size=26, weight="bold", color="white"), 
                ft.Text("M83", size=16, color="#b3b3b3")
            ], spacing=2, horizontal_alignment="center"),
            
            # --- Tiempos ajustados a 0:00 ---
            ft.Column([
                ft.Slider(min=0, max=100, value=0, active_color="#fe5f75", inactive_color="#333333"), 
                ft.Row([
                    ft.Text("0:00", color="#b3b3b3", size=12), 
                    ft.Text("0:00", color="#b3b3b3", size=12)
                ], alignment="spaceBetween", width=280)
            ], spacing=-10, horizontal_alignment="center"),
            
            ft.Row([
                ft.IconButton(ft.Icons.SKIP_PREVIOUS_ROUNDED, icon_color="white", icon_size=35),
                ft.Container(ft.IconButton(ft.Icons.PLAY_ARROW_ROUNDED, icon_color="#121212", icon_size=40), bgcolor="white", shape=ft.BoxShape.CIRCLE, padding=5),
                ft.IconButton(ft.Icons.SKIP_NEXT_ROUNDED, icon_color="white", icon_size=35)
            ], alignment="center", spacing=20)
        ], horizontal_alignment="center", spacing=25),
        bgcolor="#1e1e1e", padding=35, border_radius=40, width=360,
    )

    # --- PLAYLIST CON SCROLL ---
    def item_cancion(nombre, autor, duracion):
        return ft.ListTile(
            leading=ft.Container(ft.Icon(ft.Icons.PLAY_CIRCLE_FILL, color="#fe5f75", size=30), bgcolor="#2a2a2a", padding=5, border_radius=12),
            title=ft.Text(nombre, color="white", weight="w500"),
            subtitle=ft.Text(autor, color="#b3b3b3", size=13),
            trailing=ft.Text(duracion, color="#b3b3b3"),
        )

    playlist_container = ft.Container(
        content=ft.Column([
            ft.Text("Siguiente en la lista", size=18, weight="bold", color="white"),
            ft.ListView(
                controls=[
                    item_cancion("Starboy", "The Weeknd", "3:50"), 
                    item_cancion("Blinding Lights", "The Weeknd", "3:20"), 
                    item_cancion("Levitating", "Dua Lipa", "3:23"), 
                    item_cancion("Save Your Tears", "The Weeknd", "3:35")
                ],
                height=360, spacing=10
            )
        ], spacing=15),
        bgcolor="#1e1e1e", padding=25, border_radius=40, width=360,
    )

    # --- VISTA FINAL ---
    return ft.View(
        route="/reproductor",
        controls=[
            ft.ResponsiveRow([
                ft.Column([reproductor_tarjeta], col={"md": 4}, horizontal_alignment="center"),
                ft.Column([playlist_container], col={"md": 4}, horizontal_alignment="center"),
            ], alignment="center", vertical_alignment="center", spacing=10),
        ],
        bgcolor="#121212", padding=20,
        appbar=ft.AppBar(
            leading=ft.Container(content=perfil_menu, padding=ft.padding.only(left=15)),
            title=ft.Text("Aesthetic Player", weight="bold"), 
            bgcolor="#1e1e1e",
            center_title=True
        )
    )