import flet as ft
import componentes as cm

class PanelUI(ft.Pagelet):

    def __init__(self):
        super().__init__(self)
        self.padding = 20
        self.appbar = cm.crear_appbar(ft.icons.GRID_VIEW_SHARP, 'UI (User Inteface)')

        mkd_texto = cm.crear_texto_markdown_formateado('panel_ui.md', self)

        codigo, mkd_codigo = cm.crear_codigo_markdown('vista.md', 'python')
        txt_copiar, btn_copiar = cm.crear_boton_copiar('Código fuente de la vista:', codigo, self)

        self.content = ft.Column(
            controls=[
                mkd_texto,
                ft.Row([txt_copiar, btn_copiar]),
                ft.Container(
                    mkd_codigo,
                    margin=ft.margin.only(right=50),
                    padding=ft.padding.only(right=50),
                    clip_behavior='antiAlias'
                )
            ],
            scroll='always'
        )

if __name__ == '__main__':

    def main(page: ft.Page):
        page.theme_mode = 'light'
        cnt_principal = ft.Container(content=PanelUI(), expand=True)
        page.add(cnt_principal)

    ft.app(target=main)
