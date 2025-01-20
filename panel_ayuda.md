&nbsp;
# AYUDA
&nbsp;

Este tutorial te servirá para aprender a crear una Aplicación con Flet, SQLite y Airtable.
A grandes rasgos aprenderás a:

1. **Preparar el Entorno de desarrollo**:
   - Instalar Python y VS Codium.
    - Configurar un entorno virtual.
2. **Desarrollar una interfaz de usuario (UI) con Flet**:
   - Configurar la ventana principal
   - Usar componentes como AppBar, TextField, RadioGroup, Dropdown, Checkbox, y ElevatedButton.
   - Organizar los elementos en filas.
3. **Crear una base de datos local con SQLite**:
   - Crear una base de datos con DB Browser.
   - Agregar datos desde un archivo CSV.
   - Conectar la aplicación con la BD mediante Peewee ORM.
4. **Integrar una aplicación con Airtable**:
   - Configurar Airtable
   - Crear una conexión con Python
   - Diseñar un modelo ORM con pyairtable
5. **Agregar funcionalidad en la Aplicación**:
    - Eventos de Guardar y Cancelar.
    - Crear notificaciones.

El resultado final será una aplicación funcional con una interfaz moderna, almacenamiento local en SQLite y
sincronización en la nube mediante Airtable. ¡Todo ello usando exclusivamente software libre!

> Descarga el código fuente del proyecto: <https://github.com/chavezbosquez/tutoflet/blob/main/proyecto-final-flet/proyecto-final-flet.zip>

&nbsp;
# Preguntas Frecuentes (FAQ)
&nbsp;

**1. ¿Cómo verifico si Python está instalado en mi equipo?**

Desde la terminal o línea de comandos, ejecuta:
~~~
python --version
~~~

Deberías ver la versión de Python instalada. Si no aparece, instala Python desde [python.org](https://www.python.org).

\
&nbsp;
**2. ¿Qué hacer si no puedo instalar VS Codium?**

Asegúrate de descargar la versión correcta para tu sistema operativo desde [vscodium.com](https://vscodium.com).
Si tienes problemas intenta ejecutar el instalador como administrador o revisa las configuraciones de seguridad
de tu sistema.

\
&nbsp;
**3. ¿Cómo activo el entorno virtual?**

Una vez creado con `python -m venv env-flet`, actívalo así:

- Windows:
~~~
env-flet\Scripts\activate
~~~

- Mac/Linux:
~~~
source env-flet/bin/activate
~~~

\
&nbsp;
**4. ¿Por qué no aparece la ventana al ejecutar mi aplicación con Flet?**

Asegúrate de que el código contenga el siguiente bloque para iniciar la aplicación:

~~~
flet.app(target=main)
~~~

Verifica también que tengas instalado el paquete Flet:

~~~
pip install flet
~~~

\
&nbsp;
**5. Problemas con SQLite: ¿Qué hago si no puedo importar datos?**

- Usa `;` como separador.
- Asegúrate de que los encabezados coincidan con los nombres de los campos en la tabla. 

\
&nbsp;
**6. Errores de conexión con Airtable:**

- _Error 401 (Unauthorized)_: Verifica que el token sea válido y tenga los permisos correctos 
(`data.records.read` y `data.records.write`).
- _Error 404 (Not Found)_: Revisa que el ID de la base sea correcto y que el nombre de la tabla coincida exactamente.
- _Error 403 (Forbidden)_: Asegúrate de haber configurado correctamente los permisos del token.

\
&nbsp;
**7. ¿Cómo limpio los campos del formulario después de guardar?**

Puedes añadir esta lógica al final de la función `guardar_profesor`:

~~~python
txt_clave.value = ""
txt_nombre.value = ""
txt_apellidos.value = ""
rdo_grado.value = None
chk_prodep.value = False
drp_division.value = None
page.update()
~~~

\
&nbsp;
**8. ¿Qué hago si no aparece el mensaje de éxito?**

Verifica que el código para el `SnackBar` esté correctamente implementado y que hayas agregado la barra a la
propiedad `overlay` de la página:

~~~python
page.overlay.append(snack_bar)
~~~

&nbsp;
# ¿A dónde acudir para más ayuda?
&nbsp;

1. Documentación Oficial:
   - **Python**: <https://www.python.org>
   - **VS Codium**: <https://vscodium.com>
   - **Flet**: <https://flet.dev>
   - **Pencil Project**: <https://pencil.evolus.vn>
   - **SQLite**: <https://www.sqlite.org>
   - **Peewee ORM**: <https://docs.peewee-orm.com/en/latest/> 
   - **Airtable**: <https://www.airtable.com>
   - **PyAirtable**: <https://pyairtable.readthedocs.io/en/stable/>

2. Comunidades:
   - **Stack Overflow**: Encuentra soluciones rápidas para errores específicos.
   - **GitHub Issues**: Busca reportes similares en los repositorios de las bibliotecas que estás usando.

3. ¡Contáctanos!
- Si tienes dudas específicas sobre este tutorial, no dudes en contactarnos:
- <oscar.chavez@ujat.mx>
- <betania.hernandez@ujat.mx>
- <jose.hernandezt@ujat.mx>