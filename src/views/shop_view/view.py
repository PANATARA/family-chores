from dataclasses import dataclass
import flet as ft
from color import *


@dataclass
class ShopView:
    page: ft.Page
    bottom_bar: ft.BottomAppBar

    def show(self):
        self.page.views.clear()
        self.page.views.append(
            ft.View(
                "/shop",
                controls=[
                    ft.Text("Welcome to the Shop Page!"),
                    self.bottom_bar,
                ],
                bgcolor=color6,
                floating_action_button=ft.FloatingActionButton(
                    icon=ft.icons.ADD, bgcolor=color5
                ),
                floating_action_button_location=ft.FloatingActionButtonLocation.CENTER_DOCKED,
                padding=ft.Padding(5, 5, 5, 5),
            )
        )
        self.page.update()
