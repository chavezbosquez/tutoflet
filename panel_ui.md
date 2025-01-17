&nbsp;
# 1.  Diseño

¡Ahora sí vamos a ensuciarnos las manos! Comenzaremos creando la siguiente interfaz de usuario:

![UI en Pencil](img/ui-pencil.png)

Utilizaremos los siguientes componentes:

- `flet.AppBar`
- `flet.Text`
- `flet.TextField`
- `flet.Radio`
- `flet.Dropdown`
- `flet.Checkbox`
- `flet.ElevatedButton`

Y para organizar los componentes usaremos:

- `flet.Row`

# 2.  Configuración de la ventana

En primer lugar, vamos a personalizar el objeto `page` que define nuestro formulario o ventana. Para ello crea un
archivo llamado `vista.py`,  de acuerdo al patrón de diseño MVC (Modelo-Vista-Controlador).
MVC es un patrón de arquitectura de software que separa la lógica de la aplicación de la interfaz de usuario y del
mecanismo de persistencia (generalmente una base de datos) en una aplicación.

Para definir el tamaño de la ventana tenemos el objeto `window`. Para dejar un espacio entre los componentes y el borde
de la ventana tenemos la propiedad `padding`. Finalmente, en Flet tenemos 2 temas disponibles para nuestra aplicación:
tema claro (`light`) y tema oscuro (`dark`).

```python
    page.window.width  = 400
    page.window.height = 480
    page.title = 'Alta de profesores'
    page.padding = 25
    page.theme_mode = 'light'
```

Ahora vamos a crear una barra de título con el componente `AppBar`. Vean que podemos asignar un icono, podemos centrar
el título y asignar cualquier color de fondo y de texto que queramos.

```python
    page.appbar = ft.AppBar(
        leading=ft.Icon('person'),
        title=ft.Text('Nuevo profesor'),
        center_title=True,
        bgcolor='blue',
        color='white'
    )
```

Ahora bien, vamos a crear los componentes. Una caja de texto con una etiqueta se crea de la siguiente forma.
Ve que le asignamos el foco de manera predeterminada para que el cursor aparezca dentro de este componente nada más
se inicie la aplicación.

```python
    txt_clave = ft.TextField(label='Número de empleado', autofocus=True)
```

El caso de los botones de radio (_radio buttons_) es un poco más elaborado, puesto que es necesario crear un objeto 
de tipo `ft.RadioGroup` y dentro de este colocar componentes `ft.Radio`. Observen que podemos hacer que un radio botón
aparezca seleccionado de manera predeterminada mediante la propiedad `value`.

```python
    rdo_grado = ft.RadioGroup(content=ft.Row([
        ft.Radio(value='Licenciatura', label='Licenciatura'),
        ft.Radio(value='Maestría', label='Maestría'),
        ft.Radio(value='Doctorado', label='Doctorado')
    ]), value='Doctorado')
```

Toca turno de un cuadro combinado, que en Flet se llama _Dropdown_. En este caso dejaremos las opciones vacías porque
las cargaremos desde nuestra base de datos.

```python
    drp_division = ft.Dropdown(label='División Académica', options=None, width=400)
```

La caja de selección se crea de la siguiente manera. Nota que lo seleccionamos por defecto.

```python
    chk_prodep = ft.Checkbox(
        ' ¿Es perfil PRODEP?',
        label_position=ft.LabelPosition.RIGHT,
        value=True,
        width=320
    )
```

Flet tiene varias clases disponibles para crear botones. Aquí usaremos un botón personalizable llamado
_Elevated button_. Observa lo fácil que es configurar un botón con colores, iconos y tamaño personalizados.
La propiedad `on_click` la dejamos pendiente para la última sección del tutorial.

```python
    btn_aceptar  = ft.ElevatedButton(
        text='Guardar',
        icon='save',
        bgcolor='green',
        color='white',
        width=150,
        on_click=None
)
```

Para agregar nuestros componentes a la ventana (objeto `page`) es tan sencillo como esto:

```python
    page.add(txt_clave)
    page.add(rdo_grado)
    page.add(txt_nombre)
    page.add(txt_apellidos)
    page.add(chk_prodep)
    page.add(drp_division)
```

Flet apila los componentes en la ventana de manera natural. Sin embargo, queremos que los botones aparezcan uno
delante del otro horizontalmente. Es entonces que necesitamos usar un componente `Row` para crear este efecto:

```python
    page.add(ft.Row([btn_aceptar, btn_cancelar], alignment='center'))
```

El objeto `Row` lo creamos 'al vuelo' y le enviamos de párametro al constructor una lista con los componentes que
queremos que se organicen de manera horizontal. ¡Igual lo podemos centrar en una sola línea!

Al final, no olvides algo súper importante: hay que actualizar el objeto `page` para que refleje los cambios realizados:

```python
    page.update()
```

¡Listo! A continuación te presentamos la interfaz terminada en Flet 😎

![UI en Flet](img/ui-flet.png)
