import flet as ft
import componentes as cm

class PanelBD(ft.Pagelet):
 
    def __init__(self):
        super().__init__(self)
        self.padding = 20
        # self.bgcolor='#f5f5f5'
        self.appbar = cm.crear_appbar(ft.icons.FOLDER, 'Base de datos')

        mkd_texto = cm.crear_texto_markdown_formateado('panel_bd.md', self)

        codigo, mkd_codigo = cm.crear_codigo_markdown('vista_bd.md', 'python')

        txt_copiar, btn_copiar = cm.crear_boton_copiar('Código fuente completo:', codigo, self)

        self.content = ft.Column(
            controls=[
                ft.Container(mkd_texto, bgcolor='#f5f5f5', padding=10, clip_behavior='antiAlias'),
                ft.Row([txt_copiar, btn_copiar]),
                ft.Container(mkd_codigo, margin=ft.margin.only(right=50), padding=ft.padding.only(right=50), clip_behavior='antiAlias')
            ],
            scroll='always'
        )


if __name__ == '__main__':
    pnl_bd = PanelBD()

    def main(page: ft.Page):
        page.theme_mode = 'light'
        cnt_principal = ft.Container(content=pnl_bd, expand=True)
        page.add(cnt_principal)

    ft.app(target=main)
