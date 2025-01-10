from dataclasses import dataclass
import flet as ft
from color import *
from views.home_view.alert_dialog import HomeDialog


@dataclass
class HomeView:
    page: ft.Page
    bottom_bar: ft.BottomAppBar
    first_card_height: int
    main_board_height: int

    def show(self):
        self.page.views.clear()
        self.page.views.append(
            ft.View(
                "/home",
                controls=[
                    ft.GridView(
                        controls=[
                            self.wallet_card(),
                            self.rating_card(),
                        ],
                        max_extent=self.first_card_height,
                    ),
                    self.main_board(self.main_board_height),
                    self.bottom_bar,
                ],
                bgcolor=color6,
                floating_action_button=ft.FloatingActionButton(
                    icon=ft.icons.ADD, bgcolor=color5, on_click=self.open_dlg_modal
                ),
                floating_action_button_location=ft.FloatingActionButtonLocation.CENTER_DOCKED,
                padding=ft.Padding(5, 5, 5, 5),
            )
        )
        self.page.update()

    def main_board(self, height):
        return ft.Card(
            content=ft.Container(
                padding=10,
                alignment=ft.alignment.center,
                height=height,
            ),
            color=ft.colors.WHITE38,
        )

    def rating_card(self):

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

    def wallet_card(self):
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

    def open_dlg_modal(self, e):
        HomeDialog(e).open_dialog()
