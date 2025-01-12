from dataclasses import dataclass
import flet as ft
from color import *
from cards.settings_card import settings_card


@dataclass
class ProfileView:
    page: ft.Page
    bottom_bar: ft.BottomAppBar
    height: int

    def show(self):
        self.page.views.clear()
        self.page.views.append(
            ft.View(
                "/profile",
                controls=[
                    self.bottom_bar,
                    self.main_board(self.height)
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

    def main_board(self, height):
        return settings_card(height)