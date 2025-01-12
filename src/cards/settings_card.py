import flet as ft
from color import *

def settings_card(height):
    return ft.Card(
        content=ft.Container(
            padding=10,
            alignment=ft.alignment.center,
            height=height,
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.CircleAvatar(
                            foreground_image_src="https://avatars.githubusercontent.com/u/125561357?s=400&u=de22271dd4cb9c6fd6327a5ff8bb420d39297231&v=4",
                            radius=80,
                        ),
                        alignment=ft.alignment.center,
                    ),
                    ft.Row(
                        controls=[
                            ft.Text(
                                value="User",
                                weight="bold",
                                size=24,
                            ),
                            ft.Text(
                                value="User",
                                weight="bold",
                                size=24,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        height=height/10
                    ),
                    ft.Row(
                        controls=[
                            ft.Button(
                                text="PROFILE SETTINGS", 
                                icon=ft.icons.SETTINGS,
                                expand=True,
                                bgcolor=color4,
                                height=height/10
                            )
                        ],
                        height=height/10
                    ),
                    ft.Row(
                        controls=[
                            ft.Button(
                                text="text-text", 
                                icon=ft.icons.SETTINGS,
                                expand=True,
                                bgcolor=color4,
                                height=height/10
                            )
                        ],
                        height=height/10
                    ),
                    ft.Row(
                        controls=[
                            ft.Button(
                                text="FAMILY SETTINGS", 
                                icon=ft.Icons.FAMILY_RESTROOM,
                                expand=True,
                                bgcolor=color4,
                                height=height/10
                            )
                        ],
                        height=height/10
                    ),
                    ft.Row(
                        controls=[
                            ft.Button(
                                text="APP SETTINGS", 
                                icon=ft.icons.SETTINGS,
                                expand=True,
                                bgcolor=color4,
                                height=height/10
                            )
                        ],
                        height=height/10
                    ),
                    
                    ft.Row(
                        controls=[
                            ft.Button(
                                text="LOGOUT FROM ACCOUNT", 
                                icon=ft.icons.LOGOUT,
                                expand=True,
                                bgcolor=ft.colors.RED_400,
                                height=height/10,
                            )
                        ],
                        height=height/10,
                    ),
                ]
            )
        ),
        color=ft.colors.WHITE38,
    )


