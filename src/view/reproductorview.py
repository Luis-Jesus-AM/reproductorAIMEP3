import flet as ft

def ReproductorView(page: ft.Page):
    nombre_usuario = "Usuario"
    inicial_usuario = "U"

    def confirmar_eliminar_click(e):
        dialogo_confirmacion.open = False
        page.update()
        page.go("/")
        page.snack_bar = ft.SnackBar(
            content=ft.Text("🔥 Cuenta eliminada (Simulación de diseño)"), 
            bgcolor=ft.Colors.RED_400
        )
        page.snack_bar.open = True
        page.update()

    def cancelar_eliminar_click(e):
        dialogo_confirmacion.open = False
        page.update()

    dialogo_confirmacion = ft.AlertDialog(
        modal=True,
        title=ft.Text("⚠ ¿Eliminar tu cuenta?"),
        content=ft.Text("Esta acción es permanente. Se borrarán todos tus datos de usuario del sistema."),
        actions=[
            ft.TextButton("Cancelar", on_click=cancelar_eliminar_click),
            ft.TextButton("Sí, eliminar", icon=ft.Icons.DELETE_FOREVER, icon_color="red", on_click=confirmar_eliminar_click),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    def menu_item_click(e):
        if e.control.data == "eliminar":
            page.dialog = dialogo_confirmacion
            dialogo_confirmacion.open = True
            page.update()

    portada = ft.Container(
        content=ft.Icon(ft.Icons.MUSIC_NOTE, size=80, color="#ffffff"),
        gradient=ft.LinearGradient(
            begin=ft.alignment.Alignment(-1, -1),
            end=ft.alignment.Alignment(1, 1),
            colors=["#fe5f75", "#fc9842"],
        ),
        width=280,
        height=280,
        border_radius=30,
    )

    titulo = ft.Text("Título de la Canción", size=24, weight=ft.FontWeight.BOLD, color="#ffffff")
    artista = ft.Text("Nombre del Artista", size=16, color="#b3b3b3")

    progreso = ft.Slider(
        min=0, max=100, value=30,
        active_color="#fe5f75",
        inactive_color="#333333",
    )
    
    tiempos = ft.Row(
        controls=[
            ft.Text("0:45", color="#b3b3b3", size=12),
            ft.Text("3:20", color="#b3b3b3", size=12),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        width=300
    )

    btn_prev = ft.IconButton(icon=ft.Icons.SKIP_PREVIOUS_ROUNDED, icon_color="#ffffff", icon_size=40)
    btn_play = ft.Container(
        content=ft.IconButton(icon=ft.Icons.PLAY_ARROW_ROUNDED, icon_color="#121212", icon_size=40),
        bgcolor="#ffffff",
        shape=ft.BoxShape.CIRCLE,
        padding=10
    )
    btn_next = ft.IconButton(icon=ft.Icons.SKIP_NEXT_ROUNDED, icon_color="#ffffff", icon_size=40)

    controles = ft.Row(
        controls=[btn_prev, btn_play, btn_next],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    reproductor_tarjeta = ft.Container(
        content=ft.Column(
            controls=[
                portada,
                ft.Container(height=10),
                titulo,
                artista,
                ft.Container(height=10),
                progreso,
                tiempos,
                ft.Container(height=10),
                controles
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        bgcolor="#1e1e1e",
        padding=30,
        border_radius=35,
    )

    perfil_menu = ft.PopupMenuButton(
        content=ft.CircleAvatar(
            content=ft.Text(inicial_usuario, color="white", weight="bold"),
            bgcolor="#fe5f75",
            radius=18
        ),
        items=[
                        ft.PopupMenuItem(
                content=ft.Row([
                    ft.Icon(ft.Icons.PERSON),
                    ft.Text("Ver Perfil")
                ]),
                on_click=lambda e: page.go("/perfil")
            ),
            ft.PopupMenuItem(ft.Divider()),
            ft.PopupMenuItem(
                content=ft.Row([
                    ft.Icon(ft.Icons.DELETE_OUTLINED, color=ft.Colors.RED),
                    ft.Text("Eliminar Cuenta", color=ft.Colors.RED)
                ]),
                data="eliminar",
                on_click=menu_item_click
            ),
        ]
    )

    return ft.View(
        route="/reproductor",
        controls=[reproductor_tarjeta],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        bgcolor="#121212",
        appbar=ft.AppBar(
            leading=ft.Container(
                content=perfil_menu, 
                padding=ft.Padding(left=15, top=5, right=0, bottom=0)
            ),
            title=ft.Text("Mi Reproductor"), 
            bgcolor="#1e1e1e",
            center_title=True
        )
    )
