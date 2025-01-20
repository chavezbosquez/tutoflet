import flet as ft
import componentes as cm

class PanelAyuda(ft.Pagelet):

    def __init__(self):
        super().__init__(self)

        mkd_texto = cm.crear_texto_markdown_formateado('panel_ayuda.md', self)

        self.content = ft.Row(
            controls=[
                ft.Column(
                    controls=[mkd_texto],
                    scroll=ft.ScrollMode.ALWAYS,
                    expand=True)
            ]
        )


if __name__ == '__main__':

    def main(page: ft.Page):
        page.theme_mode = 'light'
        cnt_principal = ft.Container(content=PanelAyuda(), expand=True)
        page.add(cnt_principal)

    ft.app(target=main)
