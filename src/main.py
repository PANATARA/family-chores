import flet as ft
from color import *
from config.database import create_db_and_tables
from views.auth_view.view import AuthView
from views.home_view.view import HomeView 
from views.profile_view.view import ProfileView
from views.shop_view.view import ShopView
from views.stat_view.view import StatView



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
    page.theme = ft.Theme(
        page_transitions=ft.PageTransitionsTheme(
            android=ft.PageTransitionTheme.NONE,
            ios=ft.PageTransitionTheme.NONE,
            macos=ft.PageTransitionTheme.NONE,
            linux=ft.PageTransitionTheme.NONE,
            windows=ft.PageTransitionTheme.NONE
        )
    )
    total_height = page.height
    total_width = page.width
    bottom_appbar_height = total_height * 0.11
    
    bottom_bar = create_bottom_appbar(total_height)


    def profile(e):
        profile_page = ProfileView(page, bottom_bar, total_height-bottom_appbar_height-20)
        profile_page.show()

    def home(e):
        home_page = HomeView(page, bottom_bar, total_height-bottom_appbar_height)
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

    # home_page = HomeView(page, bottom_bar, total_height-bottom_appbar_height)
    # home_page.show()

    auth_page = AuthView(page)
    auth_page.show()

ft.app(main)

