import flet as ft
from color import *
from service.auth.registration import RegisterUser


def custom_text_field(label: str, is_pass: bool) -> ft.TextField:
    return ft.TextField(
        hint_text=label,
        password=is_pass,
        border=ft.InputBorder.UNDERLINE,
    )


username_field = custom_text_field("username", False)
first_name_field = custom_text_field("first name", False)
last_name_field = custom_text_field("last_name", False)
password_field = custom_text_field("password", True)
password_again_field = custom_text_field("password again", True)


def sign_up(e):
    username = username_field.value
    password = password_field.value
    password_again = password_again_field.value
    first_name = first_name_field.value
    last_name = last_name_field.value

    if password != password_again:
        print("REGISTRATION FAILED")

    RegisterUser(
        username=username,
        password=password,
        first_name=first_name,
        last_name=last_name,
    )()


def registration_card():
    return ft.Card(
        content=ft.Container(
            padding=10,
            alignment=ft.alignment.center,
            content=ft.Column(
                controls=[
                    ft.Text(value="Sign Up"),
                    username_field,
                    first_name_field,
                    last_name_field,
                    password_field,
                    password_again_field,
                    ft.Button(text="Sign Up", on_click=sign_up),
                ]
            ),
        ),
        color=ft.colors.WHITE38,
    )


def sign_in(e):
    pass

def authorization_card():
    return ft.Card(
        content=ft.Container(
            padding=10,
            alignment=ft.alignment.center,
            content=ft.Column(
                controls=[
                    ft.Text(value="Sign in"),
                    username_field,
                    password_field,
                    ft.Button(
                        text="Sign in",
                        on_click=sign_in,
                    ),
                ]
            ),
        ),
        color=ft.colors.WHITE38,
    )
