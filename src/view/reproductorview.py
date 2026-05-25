import flet as ft

def ReproductorView(page: ft.Page):
    # Configuración de la página específica para el reproductor
    page.bgcolor = "#121212"  # Fondo oscuro estilo Spotify
    
    # 1. Portada del Álbum
    portada = ft.Container(
        content=ft.Icon(ft.icons.MUSIC_NOTE, size=80, color="#ffffff"),
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=["#fe5f75", "#fc9842"],
        ),
        width=280,
        height=280,
        border_radius=30,
    )

    # 2. Información de la Canción
    titulo = ft.Text("Título de la Canción", size=24, weight=ft.FontWeight.BOLD, color="#ffffff")
    artista = ft.Text("Nombre del Artista", size=16, color="#b3b3b3")

    # 3. Barra de Progreso
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

    # 4. Botones de Control
    btn_prev = ft.IconButton(icon=ft.icons.SKIP_PREVIOUS_ROUNDED, icon_color="#ffffff", icon_size=40)
    btn_play = ft.Container(
        content=ft.IconButton(icon=ft.icons.PLAY_ARROW_ROUNDED, icon_color="#121212", icon_size=40),
        bgcolor="#ffffff",
        shape=ft.BoxShape.CIRCLE,
        padding=10
    )
    btn_next = ft.IconButton(icon=ft.icons.SKIP_NEXT_ROUNDED, icon_color="#ffffff", icon_size=40)

    controles = ft.Row(
        controls=[btn_prev, btn_play, btn_next],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    # 5. Tarjeta contenedora
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

    # Retornamos un ft.View para que tu main lo pueda apilar correctamente
    return ft.View(
        route="/reproductor",
        controls=[reproductor_tarjeta],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        bgcolor="#121212"
    )