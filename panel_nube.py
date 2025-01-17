import flet as ft
import componentes as cm

class PanelNube(ft.Pagelet):

    def __init__(self):
        super().__init__(self)
        self.padding = 20
        self.appbar = cm.crear_appbar(ft.icons.CLOUD, 'Base de datos en la nube')

        mkd_texto = cm.crear_texto_markdown_formateado('panel_nube.md', self)

        codigo_vista, mkd_codigo_vista = cm.crear_codigo_markdown('vista_bd_airtable.md', 'python')
        txt_copiar_vista, btn_copiar_vista = cm.crear_boton_copiar('Código fuente de la vista:', codigo_vista, self)

        codigo_modelo, mkd_codigo_modelo = cm.crear_codigo_markdown('modelo_airtable.md', 'python')
        txt_copiar_modelo, btn_copiar_modelo = cm.crear_boton_copiar('Código fuente del modelo:', codigo_vista, self)

        self.content = ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        mkd_texto,
                        ft.Row([txt_copiar_modelo, btn_copiar_modelo]),
                        cm.crear_contenedor_codigo(mkd_codigo_modelo),
                        ft.Row([txt_copiar_vista, btn_copiar_vista]),
                        cm.crear_contenedor_codigo(mkd_codigo_vista),
                    ],
                    scroll=ft.ScrollMode.ALWAYS,
                    expand=True)
            ]
        )

if __name__ == '__main__':

    def main(page: ft.Page):
        page.theme_mode = 'light'
        cnt_principal = ft.Container(content=PanelNube(), expand=True)
        page.add(cnt_principal)

    ft.app(target=main)
