import flet as ft
from modelo_sqlite import Division
from modelo_airtable import Profesor

def main(page: ft.Page):

    def cerrar_ventana(e: ft.ControlEvent):
        page.window.close()

    def guardar_profesor(e: ft.ControlEvent):
        # Crear una instancia de la clase Profesor
        profe = Profesor(
            num_empleado=txt_clave.value,
            grado = rdo_grado.value,
            nombre = txt_nombre.value,
            apellidos = txt_apellidos.value,
            es_prodep = chk_prodep.value,
            division = drp_division.value
        )
        # Guardar en la nube
        profe.save()
        # Mostrar un mensaje de éxito
        snack_bar = ft.SnackBar(
            content=ft.Text('Registro guardado en la nube'),
            bgcolor='brown',
            show_close_icon=True
        )
        page.overlay.append(snack_bar)
        snack_bar.open = True
        page.update()

    def get_divisiones() -> list:
        lista = []
        for d in Division.select():
            lista.append( ft.dropdown.Option(text=d.clave) )
        return lista

    # Configuración de la página
    page.window.width  = 400
    page.window.height = 480
    page.padding = 25
    page.title = 'Alta de profesores'
    page.theme_mode = 'light'
    
    # Barra de título
    page.appbar = ft.AppBar(
        leading=ft.Icon('person'),
        title=ft.Text('Nuevo profesor'),
        center_title=True,
        bgcolor='blue',
        color='white'
    )

    # Clave del profesor
    txt_clave = ft.TextField(label='Número de empleado', autofocus=True)
    # Nombre del profesor
    txt_nombre = ft.TextField(label='Nombre', width=400)
    # Apellidos
    txt_apellidos = ft.TextField(label='Apellidos', width=400)
    # Grado académico
    rdo_grado = ft.RadioGroup(content=ft.Row([
        ft.Radio(value='Licenciatura', label='Licenciatura'),
        ft.Radio(value='Maestría', label='Maestría'),
        ft.Radio(value='Doctorado', label='Doctorado')
    ]), value='Doctorado')

    # División Académica
    drp_division = ft.Dropdown(
        label='División Académica',
        options=get_divisiones(),
        width=400
    )

    # ¿El profesor cuenta con perfil PRODEP?
    chk_prodep = ft.Checkbox(
        ' ¿Es perfil PRODEP?',
        label_position=ft.LabelPosition.RIGHT,
        value=True,
        width=320
    )

    # Botones
    btn_aceptar  = ft.ElevatedButton(
        text='Guardar',
        icon='save',
        bgcolor='green',
        color='white',
        width=150,
        on_click=guardar_profesor
    )
    btn_cancelar = ft.ElevatedButton(
        text='Cancelar',
        icon='close',
        bgcolor='red',
        color='white',
        width=150,
        on_click=cerrar_ventana
    )

    # Agregar componentes a la UI
    page.add(txt_clave)
    page.add(rdo_grado)
    page.add(txt_nombre)
    page.add(txt_apellidos)
    page.add(chk_prodep)
    page.add(drp_division)
    page.add(ft.Row([btn_aceptar, btn_cancelar], alignment='center'))
    # No olvides actualizar la página
    page.update()


if __name__ == '__main__':
    ft.app(target=main)
