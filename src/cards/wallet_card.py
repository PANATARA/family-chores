import flet as ft

def wallet_card() -> ft.Card:
    return ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Icon(name=ft.icons.STAR, color="yellow", size=24),
                            ft.Text("42", size=24, color=ft.colors.WHITE),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        controls=[
                            ft.Icon(name=ft.icons.MONEY, color="green", size=24),
                            ft.Text("118", size=24, color=ft.colors.WHITE),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=10,
            alignment=ft.alignment.center,
        ),
        color=ft.colors.WHITE38,
    )