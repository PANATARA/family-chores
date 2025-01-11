from dataclasses import dataclass
import flet as ft
from cards.recent_activities_card import recent_activities_card
from color import *
from views.home_view.alert_dialog import HomeDialog
from cards.wallet_card import wallet_card
from cards.rating_card import rating_card


@dataclass
class HomeView:
    page: ft.Page
    bottom_bar: ft.BottomAppBar
    height: int

    def show(self):
        self.page.views.clear()
        self.page.views.append(
            ft.View(
                "/home",
                controls=[
                    ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                col={"xs": 6},  # Занимает половину экрана
                                height=self.height*0.25,
                                content=self.get_wallet_card(),
                            ),
                            ft.Container(
                                col={"xs": 6},  # Занимает вторую половину экрана
                                height=self.height*0.25,
                                content=self.rating_card(),
                            ),
                            ft.Container(
                                col={"xs": 12},  # Занимает всю ширину экрана
                                height=self.height*0.72,
                                content=self.recent_activities_card(),
                            ),
                        ],
                        height=self.height,
                    ),
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

    def recent_activities_card(self):
        return recent_activities_card()

    def rating_card(self):
        return rating_card()

    def get_wallet_card(self):
        return wallet_card()

    def open_dlg_modal(self, e):
        HomeDialog(e).open_dialog()
