from dataclasses import dataclass
import flet as ft
from cards.user_auth_card import authorization_card, registration_card
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
                    self.get_auth_card(),
                    ft.TextButton(
                        text="I don't have an account yet",
                        on_click=self.show_reg_page,
                    ),
                ],
                bgcolor=color6,
                padding=ft.Padding(5, 5, 5, 5),
            )
        )
        self.page.update()

    def get_auth_card(self):
        return authorization_card()
    
    def show_reg_page(self, e):
        RegView(e.page).show()


@dataclass
class RegView:
    page: ft.Page

    def show(self):
        self.page.views.clear()
        self.page.views.append(
            ft.View(
                "/auth",
                controls=[
                    self.reg_card(),
                    ft.TextButton(
                        text="I already have an account",
                        on_click=self.show_auth_page,
                    ),
                ],
                bgcolor=color6,
                padding=ft.Padding(5, 5, 5, 5),
            )
        )
        self.page.update()

    def reg_card(self):
        return registration_card()
    
    def show_auth_page(self, e):
        AuthView(e.page).show()