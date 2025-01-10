from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any
import flet as ft

@dataclass
class BaseAlertDialog(ABC):
    e: any

    def __post_init__(self):
        self.dialog = self.create_dialog()

    def open_dialog(self) -> None:
        self.e.control.page.overlay.append(self.dialog)
        self.dialog.open = True
        self.e.control.page.update()

    def close_dlg(self, e) -> None:
        self.dialog.open = False
        e.control.page.update()

    @abstractmethod
    def create_dialog(self) -> ft.AlertDialog:
        raise NotImplementedError("Please implement in the service class")
    