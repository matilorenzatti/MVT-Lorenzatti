
---
# Primer MVT | Django |
---

Hola a todos, este es mi primer MTV (Model Template View) en Django.

El objetivo de este entregable, es crear una app en la cual se creen y muestren los registros correspondientes a familiares. En este caso, se eligieron los campos:

- Nombre
- Edad
- Fecha de nacimiento

Se crearon 4 templates, simples, pero que cumplen con lo solicitado. Se muestran a continuación.

Una vez que se corra el servidor, se debe acceder a la siguiente URL: http://127.0.0.1:8000/inicio/

Esta URL, corresponde al template "inicio", que se creo como pagina de bienvenida, el mismo se ve asi:

![img_inicio](https://raw.githubusercontent.com/matilorenzatti/MVT-Lorenzatti/main/img_read/1.png)

Dentro del template inicio, contamos con 3 **links** que nos permiten acceder a distintas URLS, asociadas a distintos templates y views. De esta forma, tenemos las siguientes opciones:
- **Agregar familiares:** Si quisieramos agregar los registros correspondientes a mis familiares (los cuales están seteados y no se pueden modificar) tenemos que hacer clic en "Agregar familiares". Debemos tener en cuenta, que cada vez que se accede a este link se agregaran los mismos datos (con distintos ID) a la base de datos.
- **Listar familiares:** Si quisieramos listar los familiares registrados en la base de datos, tenemos que hacer clic en este link.
- **Consulta puntual:** Si quisieramos consultar un registro puntual, tenemos que modificar el nombre del familiar a consultar en la URL. Por defecto, esta seteado Matias, pero modificando el mismo podemos acceder al registro puntual.

En todos los templates, tenemos la opción de volver al inicio, para poder seguir utilizando el programa sin problemas.

### Agregar familiares:

![img_agregar](https://raw.githubusercontent.com/matilorenzatti/MVT-Lorenzatti/main/img_read/2.png)

Podemos ver que al acceder al link, se agregan los familiares a la DB y nos da 3 opciones, las cuales nos permiten volver al inicio, agregar nuevamente a los familiares, o listar los familiares registrados en la DB hasta el momento.

Si abrimos el "DB Browser for SQLite", y arrastramos nuestro archivo .sqlite, podemos ver que la DB esta creada con éxito, y en ella nuestra tabla (o modelo) creado en Django, con los campos que nosotros mismos indicamos que se creen, mas el tipo de dato correcto.

![img_db](https://raw.githubusercontent.com/matilorenzatti/MVT-Lorenzatti/main/img_read/3.png)

Cuando accedemos a nuestra tabla **familia_app_familia**, podemos observar que los registros se crean automaticamente y de forma exitosa.

![img_registros](https://raw.githubusercontent.com/matilorenzatti/MVT-Lorenzatti/main/img_read/4.png)


### Listar familiares:

![img_listar](https://raw.githubusercontent.com/matilorenzatti/MVT-Lorenzatti/main/img_read/5.png)

Podemos ver como se listan todos los registros de la tabla "familia".

### Consulta puntual:

![img_registros](https://raw.githubusercontent.com/matilorenzatti/MVT-Lorenzatti/main/img_read/6.png)

Podemos ver como se consulta con éxito un registro puntual, ingresando su nombre en la URL. En caso de ingresar un nombre que no exista en la DB, nos mostrara un error en pantalla. Si quisieramos consultar otro registro puntual, tenemos que modificar la URL, agregando el nombre de interés.


---

