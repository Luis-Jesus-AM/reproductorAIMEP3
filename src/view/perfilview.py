import flet as ft

def PerfilView(page: ft.Page):

    # =========================
    # USUARIO DESDE SESIÓN
    # =========================
    user = page.session.get("user")

    # Si no hay sesión, regresa al login
    if not user:
        page.go("/")
        return ft.View(route="/perfil")

    nombre_usuario = f"{user['nombre']} {user['apellido']}"
    correo_usuario = user["email"]
    inicial_usuario = user["nombre"][0].upper()

    canciones_favoritas = [
        "Blinding Lights",
        "505",
        "Sweater Weather",
        "After Dark"
    ]

    # =========================
    # FUNCIONES
    # =========================
    def mostrar_snackbar(texto, color=ft.Colors.GREEN):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(texto),
            bgcolor=color
        )
        page.snack_bar.open = True
        page.update()

    def editar_perfil(e):
        mostrar_snackbar("✏️ Editar perfil próximamente")

    def cerrar_sesion(e):
        page.session.remove("user")
        page.go("/")
        mostrar_snackbar("👋 Sesión cerrada", ft.Colors.ORANGE)

    # =========================
    # AVATAR
    # =========================
    avatar = ft.Container(
        content=ft.Text(
            inicial_usuario,
            size=42,
            weight=ft.FontWeight.BOLD,
            color="white"
        ),
        width=110,
        height=110,
        alignment=ft.alignment.Alignment(0, 0),
        border_radius=55,
        gradient=ft.LinearGradient(
            begin=ft.alignment.Alignment(-1, -1),
            end=ft.alignment.Alignment(1, 1),
            colors=["#fe5f75", "#fc9842"]
        )
    )

    nombre = ft.Text(
        nombre_usuario,
        size=28,
        weight=ft.FontWeight.BOLD,
        color="white"
    )

    correo = ft.Text(
        correo_usuario,
        size=14,
        color="#b3b3b3"
    )

    # =========================
    # FAVORITAS
    # =========================
    favoritas_lista = ft.Column(
        spacing=10,
        controls=[
            ft.Container(
                bgcolor="#1e1e1e",
                border_radius=15,
                padding=15,
                content=ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.FAVORITE, color="#fe5f75"),
                        ft.Text(cancion, color="white")
                    ]
                )
            )
            for cancion in canciones_favoritas
        ]
    )

    # =========================
    # BOTONES
    # =========================
    botones = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=15,
        controls=[
            ft.ElevatedButton(
                "Editar Perfil",
                icon=ft.Icons.EDIT,
                on_click=editar_perfil,
                style=ft.ButtonStyle(
                    bgcolor="#fe5f75",
                    color="white",
                    padding=20,
                    shape=ft.RoundedRectangleBorder(radius=12)
                )
            ),

            ft.OutlinedButton(
                "Cerrar Sesión",
                icon=ft.Icons.LOGOUT,
                on_click=cerrar_sesion,
                style=ft.ButtonStyle(
                    color="white",
                    side=ft.BorderSide(1, "#ffffff"),
                    padding=20,
                    shape=ft.RoundedRectangleBorder(radius=12)
                )
            )
        ]
    )

    # =========================
    # CARD PRINCIPAL
    # =========================
    perfil_card = ft.Container(
        width=420,
        padding=30,
        border_radius=30,
        bgcolor="#181818",
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=25,
            controls=[

                avatar,

                ft.Column(
                    spacing=5,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        nombre,
                        correo
                    ]
                ),

                ft.Divider(color="#333333"),

                ft.Text(
                    "🎵 Canciones Favoritas",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="white"
                ),

                favoritas_lista,

                ft.Container(height=10),

                botones
            ]
        )
    )

    # =========================
    # VIEW
    # =========================
    return ft.View(
        route="/perfil",
        bgcolor="#121212",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        appbar=ft.AppBar(
            title=ft.Text("Mi Perfil"),
            bgcolor="#1e1e1e",
            center_title=True,
            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                on_click=lambda _: page.go("/reproductor")
            )
        ),
        controls=[
            perfil_card
        ]
    )