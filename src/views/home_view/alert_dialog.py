from dataclasses import dataclass
import flet as ft
from color import *
from core.views.alert_dialog import BaseAlertDialog


@dataclass
class HomeDialog(BaseAlertDialog):

    def create_dialog(self) -> ft.AlertDialog:
        return ft.AlertDialog(
            modal=True,
            content=self.get_chores_list(),
            actions=[
                ft.TextButton("Close", on_click=self.close_dlg),
            ],
            actions_alignment=ft.MainAxisAlignment.CENTER,
            scrollable=True,
        )

    def get_chores_list(self) -> ft.Container:
        return ft.Container(
            content=ft.Column(
                controls=self._get_chore_item(),
                scroll=ft.ScrollMode.HIDDEN,
            ),
        )

    def _get_chore_item(self, count=22) -> list[ft.Control]:
        items = []
        for i in range(1, count + 1):
            items.append(
                ft.Container(
                    content=ft.Button(
                        text=f"Chore number {i}",
                        icon=ft.icons.HOME,
                        bgcolor=color7,
                    ),
                    width=400,
                    height=50,
                )
            )
        return items
