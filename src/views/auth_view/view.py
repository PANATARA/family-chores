from dataclasses import dataclass
import flet as ft
from cards.user_auth_card import registration_card
from color import *


@dataclass
class AuthView:
    page: ft.Page

    def show(self):
        self.page.views.clear()
        self.page.views.append(
            ft.View(
                "/auth",
                controls=[
                    self.auth_card()
                ],
                bgcolor=color6,
                padding=ft.Padding(5, 5, 5, 5),
            )
        )
        self.page.update()

    def auth_card(self):
        return registration_card(self.page.height)
