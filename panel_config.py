import flet as ft
#import componentes as cm

def leer_archivo(archivo):
    """"""
    return open(archivo, 'r').read()

def crear_texto_markdown_formateado(archivo, pagelet):
        return ft.Markdown(
            leer_archivo(archivo),
            selectable=True,
            md_style_sheet=ft.MarkdownStyleSheet(p_text_style=ft.TextStyle(size=16)),
            extension_set='gitHubWeb',
            code_theme='atom-one-dark',
            code_style=ft.TextStyle(font_family='RobotoMono', size=16),
            #code_style_sheet=ft.TextStyle(font_family="RobotoMono", size=16),
            on_tap_link=lambda e: pagelet.page.launch_url(e.data)
        )

class PanelConfig(ft.Pagelet):
    def __init__(self):
        super().__init__(self)
        self.padding = 20
        self.appbar = ft.AppBar(
            leading=ft.Icon(ft.icons.SETTINGS),
            title=ft.Text('Configuración', size=26),
            bgcolor=ft.colors.GREEN_200
        )
        mkd_texto = crear_texto_markdown_formateado('assets/config.md', self)

        self.content=ft.Row(
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
        cnt_principal = ft.Container(content=PanelConfig(), expand=True)
        page.add(cnt_principal)

    ft.app(target=main)
