&nbsp;
# 1.  Airtable

[DESCRIBIR QUE ES AIRTABLE]

**Importante**: Regístrate en https://airtable.com/invite/r/zbo8aKUM
para que me regalen $10 USD de crédito por la invitación 😄

![Registro en Airtable](img/airtable1.png)

## 1.1 Crear la base de datos

Simplemente ingresa a la página principal https://airtable.com
y presiona el botón _+ Crear_.

![Crear base de datos](img/airtable2.png)

Ahora selecciona la opción **Empezar desde cero**.

<mark>Nota:</mark> La UI de Airtable cambia a cada rato,
así que las siguientes pantallas pueden no ser las mismas.

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

Para el campo `apellidos` hacemos lo mismo

![Campo #4](img/airtable9.png)

Como ya se acabaron los campos predeterminados de Airtable, presionamos el botón **+** para agregar
un nuevo campo.

![Nuevo campo](img/airtable10.png)

Añadimos el campo `es_prodep` y le asignamos el tipo `Casilla de verificación`.

![Campo #5](img/airtable11.png)

Finalmente, el campo `division` será `Texto de una sola línea`.

![Campo #6](img/airtable12.png)

Ahora vamos a cerrar el panel **Vistas** que se se muestra en la parte derecha de la página.

![Panel Vistas](img/airtable13.png)

Y vamos a eliminar los registros vacíos que por defecto crea Airtable.

![Eliminar registros](img/airtable14.png)

Ah se nos olvidaba algo importante: cambiar el nombre de la base de datos (aunque realmente no
es tan importante porque accederemos a la base de datos a través de su id y no por su nombre.)

![Nombre de la BD](img/airtable15.png)

¡__Trasque__ el nombre de la tabla sí que es importante! Cambiémosle el nombre también.

![Nombre de la Tabla](img/airtable.png)


## 1.2 Código

Para poder acceder a nuestra recién creada base de datos desde nuestra aplicación necesitamos
sí o sí instalar el módulo `pyairtable`:

~~~
pip install pyairtable
~~~

La instalación debe concluir sin contratiempos.

Ahora vamos a crear un nuevo archivo para hacer la conexión con Airtable. Por convención
vamos a nombrar  nuestro archivo como `modelo.py`, siguiendo la convención del patrón de
diseño MVC (**Modelo-Vista-Controlador**).

En nuestro nuevo archivo vamos a importar la clase más importante de `pyairtable` y  escribimos
las líneas necesarias para conectarnos a la BD:

~~~python
from pyairtable import Api

api = Api('[]')
table = api.table('[]', '[]')

datos = table.all()
~~~

¿De dónde vamos a sacar esos 3 datos que faltan? Bueno pues desde la web de Airtable podemos
obtener un _token_, el _id_ de nuestra base de datos y el nombre de nuestra tabla.

Comencemos con el _token_. Primero ingresa al Centro de desarrolladores de Airtable:

![Centro de creadores](img/airtable.png)


Ahora del menú lateral selecciona la opción **Tokens de acceso personal** y
presiona el botón **Crear token**:

![Tokens de acceso personal](img/airtable.png)

Escribe un nombre para token. Realmente el nombre es irrelevante porque no lo vamos a
utilizar, pero conviene colocar un nombre descriptivo. 

![](img/airtable.png)

Ahora sí viene lo bueno. Configura el **Ámbito de la aplicación**, que básicamente consiste
de los permisos de acceso a nuestra BD. Selecciona las siguientes 2 opciones de la sección **Alcances**:

- `data.records.read`
- `data.records.write`

En la sección **Acceso** selecciona tu base de datos:

![Ámbito de la aplicación](img/airtable.png)

Finalmente presiona el botón **Guardar cambios**.

El token aparecerá en una ventanita emergente. Copia el código en un lugar seguro ¡y no
lo compartas con nadie!

![Token](img/airtable.png)

Ya tenemos 1 de 3 datos. Vamos a por el _id_ de la BD. Para ello ingresa a <https://airtable.com/api>
y selecciona tu base de datos favorita:

![API](img/airtable.png)

Busca el _id_ de tu base de datos (comienza con `app`). 

![Id de la base de datos](img/airtable.png)


