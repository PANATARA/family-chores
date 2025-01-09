import flet as ft
from color import *
from views.home_view import HomeView
from views.profile_view import ProfileView
from views.shop_view import ShopView
from views.stat_view import StatView


def create_bottom_appbar(total_height):
    return ft.BottomAppBar(
        bgcolor="#6C91C2",
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                
            ],
        ),
        height=total_height * 0.11,
    )


def main(page: ft.Page):
    total_height = page.height
    total_width = page.width
    bottom_appbar_height = total_height * 0.11
    first_card_height = total_width / 2
    main_board_height = total_height - bottom_appbar_height - 20 - total_width / 2

    bottom_bar = create_bottom_appbar(total_height)


    def profile(e):
        profile_page = ProfileView(page, bottom_bar, total_height-bottom_appbar_height-20)
        profile_page.show()

    def home(e):
        home_page = HomeView(page, bottom_bar, first_card_height, main_board_height)
        home_page.show()

    def shop(e):
        shop_page = ShopView(page, bottom_bar)
        shop_page.show()

    def stat(e):
        stat_page = StatView(page, bottom_bar)
        stat_page.show()


    bottom_bar.content.controls.append(
        ft.IconButton(
            icon=ft.icons.HOME, icon_color=ft.colors.WHITE, icon_size=35, 
            on_click=home
        ),
    )
    bottom_bar.content.controls.append(
        ft.IconButton(
            icon=ft.icons.AUTO_GRAPH, icon_color=ft.colors.WHITE, icon_size=35,
            on_click=stat
        ),
    )
    bottom_bar.content.controls.append(
        ft.Container(expand=True),
    )
    bottom_bar.content.controls.append(
        ft.IconButton(
            icon=ft.icons.SHOPPING_CART, icon_color=ft.colors.WHITE, icon_size=35,
            on_click=shop
        ),
    )
    bottom_bar.content.controls.append(
        ft.IconButton(
            icon=ft.icons.PERSON_PIN, icon_color=ft.colors.WHITE, icon_size=35, 
            on_click=profile
        )
    )

    home_page = HomeView(page, bottom_bar, first_card_height, main_board_height)
    home_page.show()

ft.app(main)
