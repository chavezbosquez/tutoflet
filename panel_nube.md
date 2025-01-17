&nbsp;
# 1.  Airtable

Airtable es una plataforma que permite nos permite crear bases de datos basadas en la nube, incluyendo
tablas, formularios y vistas personalizados para administrar y hacer un seguimiento de los datos.

Las principales ventajas de Airtable son su facilidad de uso, flexibilidad y opciones de personalización,
¡además de un fabuloso plan gratuito! Usaremos esta plataforma para guardar nuestros datos. 

**Importante**: Regístrate en https://airtable.com/invite/r/zbo8aKUM
para que me regalen $10 USD de crédito por la invitación 😄

![Registro en Airtable](img/airtable1.png)

**Nota**: El asistente inicial de Airtable puede ser un poco abrumador, así que únicamente dale clic en _Siguiente_
en opción que te presente y listo.

Para crear la base de datos simplemente ingresa a la página principal https://airtable.com y presiona el botón _+ Crear_.

![Crear base de datos](img/airtable2.png)

Ahora selecciona la opción **Empezar desde cero**.

**Nota**: La UI de Airtable cambia a cada rato, así que las siguientes pantallas podrían no ser las mismas.

![Empezar desde cero](img/airtable3.png)

La siguiente figura muestra la vista inicial de nuestra base de datos.
Nota que aparece un asistente en la parte derecha. No lo necesitaremos así que puedes cerrarlo.

![Vista inicial](img/airtable4.png)
 
Ahora vamos a crear los campos necesarios para guardar la información. Como ya 
existen varios campos creados automáticamente por Airtable, simplemente debes hacer
clic derecho sobre cada uno de los campos y seleccionar la opción **Editar campo**.

![Editar campos](img/airtable5.png)

Para el caso de nuestro primer campo, le colocaremos por nombre `num_empleado` y como
tipo le asignaremos `Texto de una sola línea`.

![Campo #1](img/airtable6.png)

El siguiente campo será `grado` con tipo `Selección única`. Después agregar las opciones 
`Licenciatura`, `Maestría` y `Doctorado`.

![Campo #2](img/airtable7.png)

Continuamos con el campo `nombre` de tipo `Texto de una sola línea`.

![Campo #3](img/airtable8.png)

Para el campo `apellidos` hacemos lo mismo.

![Campo #4](img/airtable9.png)

Como ya se acabaron los campos predeterminados de Airtable, presionamos el botón **+ (Add field)** para agregar
un nuevo campo.

![Nuevo campo](img/airtable10.png)

Añadimos el campo `es_prodep` y le asignamos el tipo `Casilla de verificación`.

![Campo #5](img/airtable11.png)

Finalmente, el campo `division` será `Texto de una sola línea`.

![Campo #6](img/airtable12.png)

Ahora vamos a cerrar el panel **Vistas** que se se muestra en la parte derecha de la página 
(de hecho pudimos cerrarlo desde un principio LoL).

![Panel Vistas](img/airtable13.png)

Y vamos a eliminar los registros vacíos que por defecto crea Airtable. Selecciónalos todos y haz clic derecho sobre
los campos para eliminarlos.

![Eliminar registros](img/airtable14.png)

Ah se nos olvidaba algo importante: cambiar el nombre de la base de datos (aunque realmente no
es tan importante porque accederemos a la base de datos a través de su `id` y no por su nombre).

![Nombre de la BD](img/airtable15.png)

¡__Trasque__ el nombre de la tabla sí que es importante! Cambiémosle el nombre también a `profesor`:

![Nombre de la Tabla](img/airtable16.png)

Ahora sí, así debe quedar tu base de datos:

![BD](img/airtable17.png)

# 2.  Conexión a la BD

Para poder acceder a nuestra recién creada base de datos desde nuestra aplicación necesitamos
sí o sí instalar el módulo `pyairtable` (<https://pyairtable.readthedocs.io/en/stable/>).
Se trata de un ORM ((_Object-relational mapping_) que de manera similar a `peewee` permite realizar las operaciones
CRUD de una manera muy sencilla usando el paradigma Orientado a Objetos. 

Así que desde una terminal ejecuta:

~~~
pip install pyairtable
~~~

La instalación debe concluir sin contratiempos.

Ahora vamos a crear un nuevo archivo para hacer la conexión con Airtable. Vamos a nombrarlo `conexion-airtable.py` 
(o como ustedes prefieran, ya que será un script temporal).
En nuestro nuevo archivo vamos a importar la clase `Api` (la más importante de `pyairtable`) y  escribimos
las líneas necesarias para conectarnos a la BD:

~~~python
from pyairtable import Api

api = Api('[]')
table = api.table('[]', '[]')

datos = table.all()
~~~

En el script vemos 3 listas vacías. ¿De dónde vamos a sacar esos 3 datos que faltan?
Bueno pues desde la web de Airtable podemos obtener un _token_, el _id_ de nuestra base de datos y
el nombre de nuestra tabla, los cuales son precisamente los datos que nos faltan.

Comencemos con el _token_. Primero ingresa al Centro de desarrolladores de Airtable:

![Centro de creadores](img/airtable18.png)


Ahora del menú lateral selecciona la opción **Tokens de acceso personal** y
presiona el botón **Crear token**:

![Tokens de acceso personal](img/airtable19.png)

Escribe un nombre para token. Realmente el nombre es irrelevante porque no lo vamos a
utilizar, pero conviene colocar un nombre descriptivo.

Ahora sí viene lo bueno. Configura el **Ámbito de la aplicación**, que básicamente consiste
de los permisos de acceso a nuestra BD. 
Presiona el botón **+ Añadir alcance**  y selecciona las siguientes 2 opciones:

- `data.records.read`
- `data.records.write`

¡Revisa bien ambas opciones porque la mayoría de estudiantes se equivocan en esta parte!

Ahora en la sección **Acceso** presiona el botón **Añadir una base** y selecciona tu base de datos.

Finalmente presiona el botón **Crear token**. Verifica que tu configuración quede de manera similar a la siguiente:

![Configurar token](img/airtable20.png)

El token aparecerá en una ventanita emergente. Copia el código en un lugar seguro ¡y no
lo compartas con nadie!

![Token](img/airtable21.png)

Ya tenemos 1 de 3 datos. Vamos a por el _id_ de la BD. Para ello ingresa a <https://airtable.com/api>
y selecciona tu base de datos favorita (o sea la que acabamos de crear):

![API](img/airtable22.png)

Una vez dentro de la configuración de la API (_Application Programming Interface_), 
busca el _id_ de tu base de datos (comienza con `app`). 

![Id de la base de datos](img/airtable23.png)

Ya tenemos 2 de 3 datos. El único dato que falta es el nombre de la tabla, el cual nosotros mismos definimos como `profesor`.

# 3.  Código

Vamos a empezar por hacer una prueba de conexión. Para ello copia el siguiente código (reemplazando mis datos con los tuyos):

~~~python
from pyairtable import Api

# Conexión a nuestra BD
api = Api('patjXYNaB6OslrJQT.e07924f5190173607585aad092bb5744213a6b9eab.ToKeN.faLSO')
tabla = api.table('appkdrgj9qjMwaTkr', 'profesor')

# Mostrar todos los registros
registros = tabla.all()
for registro in registros:
    print(registro)
~~~

Si no obtuviste ninguna salida entonces ¡felicitaciones! Vamos bien. En caso contrario, puedes obtener el siguiente error:

> requests.exceptions.HTTPError: ('401 Client Error: Unauthorized for url: https://api.airtable.com/v0/appkdrgj9qjMwaTkr/profesor', "{'type': 'AUTHENTICATION_REQUIRED', 'message': 'Authentication required'}")

el cual indica que el token es incorrecto.

Otro error posible es:

> requests.exceptions.HTTPError: ('404 Client Error: Not Found for url: https://api.airtable.com/v0/appkdrgjx9qjMwaTkr/profesor', "'NOT_FOUND'")

el cual indica que el _id_ de la base de datos es incorrecto.

Finalmente el siguiente error:

> requests.exceptions.HTTPError: ('403 Client Error: Forbidden for url: https://api.airtable.com/v0/appkdrgj9qjMwaTkr/profesorx', "{'type': 'INVALID_PERMISSIONS_OR_MODEL_NOT_FOUND', 'message': 'Invalid permissions, or the requested model was not found. Check that both your user and your token have the required permissions, and that the model names and/or ids are correct.'}")

indica que el nombre de la tabla es incorrecto.

Ahora vamos a guardar un registro en nuestra BD. Recuerda que el estándar de intercambio de datos en la nube es el formato JSON
(JavaScript Object Notation), por lo que podemos construir un objeto JSON fácilmente de la siguiente manera:

~~~python
from pyairtable import Api

# Conexión a nuestra BD
api = Api('patjXYNaB6OslrJQT.e07924f5190173607585aad092bb5744213a6b9eab8416f489158220245269fd')
tabla = api.table('appkdrgj9qjMwaTkr', 'profesor')

# Crear un nuevo registro
betania = {'num_empleado': 'BHO04876',
         'grado'       : 'Doctorado',
         'nombre'      : 'Betania',
         'apellidos'   : 'Hernández Ocaña',
         'es_prodep'   : True,
         'division'    : 'DACyTI'}

# Guardar en la nube
tabla.create(betania)

# Mostrar todos los registros
registros = tabla.all()
for registro in registros:
    print(registro)
~~~

Ejecuta el código anterior y _voilà_! Ahora ya tenemos un nuevo registro y la salida debe ser la siguiente:

> {'id': 'reck2uci11qBql6uw', 'createdTime': '2025-01-16T19:16:30.000Z', 'fields': {'num_empleado': 'BHO04876', 'grado': 'Doctorado', 'nombre': 'Betania', 'apellidos': 'Hernández Ocaña', 'es_prodep': True, 'division': 'DACyTI'}}

Como podrás deducir de la salida, Airtable agrega 2 metadatos a cada registro: un identificador único y la fecha de creación.
Si quieres imprimir únicamente tus datos entonces cambia la siguiente instrucción del código anterior

```print(registro)```

por

```print(registro['fields'])```

Ahora mira tu base datos y automágicamente se mostrará el nuevo registro: 

![Datos guardados](img/airtable24.png)

# 4.  Airtable ORM

Vamos a crear un nuevo archivo en el cual haremos el _mapeo objeto-relacional_ de nuestra tabla en Airtable.
Por convención vamos a nombrar  nuestro archivo como `modelo_airtable.py`, siguiendo el patrón de
diseño MVC (Modelo-Vista-Controlador).

Tenemos que implementar una clase con el mismo nombre que nuestra tabla, pero comenzando en mayúsculas por convención
de nombramiento de Python. Esta clase debe heredar de la clase `Model` de `pyairtable`, y vamos a definir como atributos
de la clase todos los campos de nuestra tabla. Revisa bien los tipos de datos predeterminados de `pyairtable`. 
Finalmente, la subclase `Meta` contiene todos los datos necesarios para la conexión con Airtable (estos datos ya los
tenemos en el script anterior).

Ahora viene la prueba de fuego: crearemos un objeto derivado de nuestra clase y le asignaremos los datos que queremos
guardar en la nube. Mira que fácil es esto:

~~~python
from pyairtable.orm import Model
from pyairtable.orm import fields as F

class Profesor(Model):
    num_empleado = F.TextField('num_empleado')
    grado        = F.SelectField('grado')
    nombre       = F.TextField('nombre')
    apellidos    = F.TextField('apellidos')
    es_prodep    = F.CheckboxField('es_prodep')
    division     = F.TextField('division')
    class Meta:
        api_key = 'patjXYNaB6OslrJQT.e07924f5190173607585aad092bb5744213a6b9eab.ToKeN.faLSO'
        base_id = 'appkdrgj9qjMwaTkr'
        table_name = 'profesor'

# Crear una instancia de la clase Profesor
torruco = Profesor(
    num_empleado='JHT01023',
    grado = 'Doctorado',
    nombre = 'José',
    apellidos = 'Hernández Torruco',
    es_prodep = True,
    division = 'DACyTI'
)

# Guardar en la nube
torruco.save()

print('Registro guardado')
~~~

¡Excelente! Revisa tu base de datos y ya debe contener el nuevo registro:

![Airtable ORM](img/airtable25.png)

# 5.  Juntándolo todo

Vamos a incluir la funcionalidad de la nube en nuestra pequeña aplicación. Agrega la dependencia a `modelo_airtable.py`
en el archivo `vista.py`:

~~~python
from modelo_airtable import Profesor
~~~

Ahora crea un nuevo evento para guardar los datos. Esto se realiza declarando una función que será llamada al presionar
el botón **Guardar**:

~~~python
    def guardar_profesor(e: ft.ControlEvent):
        print('Guardar registro')
~~~

Recuerda agregar el nombre de la función al evento `on_click()` del botón.

~~~python
    btn_aceptar  = ft.ElevatedButton(
        text='Guardar',
        icon='save',
        bgcolor='green',
        color='white',
        width=150,
        on_click=guardar_profesor
    )
~~~

Ejecuta el archivo y revisa que al hacer clic al botón te aparezca en la terminal el texto _'Guardar registro'_.
Puedes continuar si todo ha salido bien.

**Importante:** Recuerda eliminar el código de prueba dentro de `modelo_airtable.py` donde guardábamos un registro de
ejemplo. ¡De lo contrario tendrás múltiples registros repetidos!

Ahora vamos a reciclar el código de `modelo_airtable.py` para guardar los datos recopilados desde nuestra UI. El ćodigo
de la función nos queda así:

~~~python
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
~~~

¿Que tal? ¿Funciona? Ejecuta el archivo y rellena con algunos datos realistas:

![UI](img/airtable26.png)

¡Listo! Ya aparecen los datos en Airtable:

![Airtable ORM](img/airtable27.png)

Ahora vamos a detallar un poco nuestra aplicación. En primer lugar vamos a incluir la funcionalidad del botón 
**x Cancelar**. Para ello define la siguiente función:


~~~python
    def cerrar_ventana(e: ft.ControlEvent):
        page.window.close()
~~~

Y por supuesto debes invocarla desde el botón `btn_cancelar`:

~~~python
    btn_cancelar = ft.ElevatedButton(
        text='Cancelar',
        icon='close',
        bgcolor='red',
        color='white',
        width=150,
        on_click=cerrar_ventana
    )
~~~

Ejecuta el archivo y le botón ahora tiene la funcionalidad de cerrar la ventana y terminar la aplicación.

En segundo lugar vamos a desplegar un mensaje al momento de guardar un registro. Agrega este código justo debajo
después de `profe.save()`:

~~~python
        # Mostrar un mensaje de éxito
        snack_bar = ft.SnackBar(
            content=ft.Text('Registro guardado en la nube'),
            bgcolor='brown',
            show_close_icon=True
        )
        page.overlay.append(snack_bar)
        snack_bar.open = True
        page.update()
~~~

¿Qué tal se ve? ¿Elegante verdad?

Pues ya con esto concluimos el tutorial. ¡Esperamos te haya gustado! Solamente te queda de tarea la validación de datos antes
de guardar. ¡Y limpiar los campos después de guardar!