import flet as ft

def crear_appbar(icono, texto):
    return ft.AppBar(
        leading=ft.Icon(icono),
        title=ft.Text(texto, size=26),
        bgcolor=ft.colors.GREEN_200
    )


def leer_archivo(archivo):
    try:
        return open(archivo, 'r').read()
    except:
        return '[Error al cargar el archivo]'


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


def crear_codigo_markdown(archivo, lenguaje):
    codigo  = leer_archivo(archivo)
    return codigo, ft.Markdown(f'~~~{lenguaje}\n' + codigo + '\n~~~',
                                selectable=True,
                                extension_set='gitHubWeb',
                                code_theme='atom-one-dark',
                                code_style=ft.TextStyle(font_family='RobotoMono', size=16)
                            )

def crear_boton_copiar(texto, codigo, pagelet):
    txt_copiar = ft.Text(
        value=texto,
        size=20,
        weight=ft.FontWeight.W_500,
        color=ft.colors.BLUE_GREY,
        selectable=True)
    btn_copiar = ft.IconButton(
        ft.icons.COPY,
        tooltip='Copiar código fuente',
        on_click=lambda e: pagelet.page.set_clipboard(codigo)
    )
    return txt_copiar, btn_copiar