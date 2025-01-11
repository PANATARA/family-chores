import flet as ft

def rating_card():

        leaderboard = [
            {"name": "Alice", "stars": 42},
            {"name": "Bob", "stars": 3},
            {"name": "Charlie", "stars": 4},
        ]

        leaderboard.sort(key=lambda x: x["stars"], reverse=True)

        rating_list = [
            ft.Row(
                controls=[
                    ft.Text(f"{index + 1}. {entry['name']}", size=16),
                    ft.Row(
                        controls=[
                            ft.Text(f"{entry['stars']}", size=16),
                            ft.Icon(name=ft.icons.STAR, color="yellow", size=16),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            )
            for index, entry in enumerate(leaderboard)
        ]

        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Column(
                            controls=rating_list,
                            alignment=ft.MainAxisAlignment.START,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
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