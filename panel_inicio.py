import flet as ft

class PanelInicio(ft.Pagelet):

    def __init__(self):
        super().__init__(self)
        img_ujat = ft.Image(src='img/dacyti.png', width=200, fit=ft.ImageFit.CONTAIN)
        txt_sistema = ft.Text(
            value='Tutorial de programación avanzada en Flet',
            size=30,
            font_family="RobotoSlab",
            weight=ft.FontWeight.W_500,
            color=ft.colors.GREEN_700
        )
        txt_version = ft.Text(
            value='Versión 1.0',
            size=20,
            font_family='RobotoSlab',
            weight=ft.FontWeight.W_500,
            color=ft.colors.GREEN_700
        )
        txt_info = ft.Text(
            value='Desarrollado con ❤️ por:\nOscar Chávez-Bosquez\nBetania Hernández-Ocaña\nJosé Hernández-Torruco',
            theme_style=ft.TextThemeStyle.BODY_LARGE,
            text_align='center'
        )

        self.content=ft.Row(
            controls=[
                ft.Column(
                    controls=[img_ujat, ft.Divider(), txt_sistema, txt_version, txt_info],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )


if __name__ == '__main__':

    def main(page: ft.Page):
        page.theme_mode = 'light'
        cnt_principal = ft.Container(content=PanelInicio(), expand=True)
        page.add(cnt_principal)

    ft.app(target=main)
