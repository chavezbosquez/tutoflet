import flet as ft
from panel_inicio import PanelInicio
from panel_config import PanelConfig
from panel_ui import PanelUI
from panel_bd import PanelBD
from panel_nube import PanelNube
from panel_ayuda import PanelAyuda

def main(page: ft.Page):

    def set_pantalla(e: ft.ControlEvent):
        cnt_principal.content = lst_pantallas[e.control.selected_index]
        cnt_principal.update()

    # Configuración de la página
    page.fonts = {
        'RobotoMono': 'font/RobotoMono-VariableFont_wght.ttf',
        'RobotoSlab': 'font/RobotoSlab.ttf',
        'Caecilia'  : 'font/CaeciliaLTStd-Roman.otf'
    }
    page.title = 'Tutorial de programación avanzada en Flet'
    page.theme_mode = 'light'
    page.window.height = 850

    # Pantalla principal
    pnl_inicio = PanelInicio()
    cnt_principal = ft.Container(content=pnl_inicio, expand=True)

    lst_pantallas = [
        pnl_inicio,
        PanelConfig(),
        PanelUI(),
        PanelBD(),
        PanelNube(),
        PanelAyuda(),
    ]

    nav_rail = ft.NavigationRail(
        bgcolor=ft.colors.GREEN_200,
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        group_alignment=-1,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.HOME_OUTLINED,
                selected_icon=ft.icons.HOME,
                label='Inicio'
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon=ft.icons.SETTINGS,
                label='Configuración'
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.GRID_VIEW_OUTLINED,
                selected_icon=ft.icons.GRID_VIEW_SHARP,
                label='UI'
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.FOLDER_OUTLINED,
                selected_icon=ft.icons.FOLDER,
                label='Base de datos'
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.CLOUD_OUTLINED,
                selected_icon=ft.icons.CLOUD,
                label='En la nube'
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.HELP_OUTLINE,
                selected_icon=ft.icons.HELP,
                label='Ayuda'
            )
        ],
        on_change=set_pantalla
    )

    page.add(
        ft.Row(
            controls=[
                nav_rail,
                ft.VerticalDivider(width=1),
                ft.Column(
                    controls=[cnt_principal],
                    alignment=ft.MainAxisAlignment.START,
                    expand=True
                )
            ],
            expand=True
        )
    )

if __name__ == '__main__':
    ft.app(target=main) # web_renderer=ft.WebRenderer.HTML
