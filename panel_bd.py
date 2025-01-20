import flet as ft
import componentes as cm

class PanelBD(ft.Pagelet):
 
    def __init__(self):
        super().__init__(self)
        self.padding = 20
        self.appbar = cm.crear_appbar(ft.icons.FOLDER, 'Base de datos')

        mkd_texto = cm.crear_texto_markdown_formateado('panel_bd.md', self)

        codigo_vista, mkd_codigo_vista = cm.crear_codigo_markdown('vista_bd.md', 'python')
        txt_copiar_vista, btn_copiar_vista = cm.crear_boton_copiar('Código fuente de la vista:', codigo_vista, self)

        codigo_modelo, mkd_codigo_modelo = cm.crear_codigo_markdown('modelo_sqlite.md', 'python')
        txt_copiar_modelo, btn_copiar_modelo = cm.crear_boton_copiar('Código fuente del modelo:', codigo_modelo, self)

        self.content = ft.Column(
            controls=[
                mkd_texto,
                ft.Row([txt_copiar_modelo, btn_copiar_modelo]),
                cm.crear_contenedor_codigo(mkd_codigo_modelo),
                ft.Row([txt_copiar_vista, btn_copiar_vista]),
                cm.crear_contenedor_codigo(mkd_codigo_vista)
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
