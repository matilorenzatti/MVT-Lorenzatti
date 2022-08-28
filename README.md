# MVT-Lorenzatti

## Primer MVT - Django

Hola a todos, este es mi primer MTV (Model Template View) en Django.

El objetivo de este entregable, es crear una app en la cual se creen y muestren los registros correspondientes a familiares. En este caso, se eligieron los campos:

- Nombre
- Edad
- Fecha de nacimiento

Se crearon 2 templates, uno llamado "inicio" y otro llamado "familia".

Una vez que se corra el servidor, se debe acceder a la siguiente URL: http://127.0.0.1:8000/inicio/

Esta URL, corresponde al template "inicio", que se creo como pagina de bienvenida, el mismo se ve asi:

![img_inicio](https://raw.githubusercontent.com/matilorenzatti/MVT-Lorenzatti/main/img_read/1.png)

Dentro de dicho template, contamos con un **link** que nos permite acceder a otro template, el cual esta vinculado a una view que crea los registros correspondientes de mis familiares, y los muestra en pantalla. El mismo se ve de la siguiente forma: http://127.0.0.1:8000/familia/

![img_familia](https://raw.githubusercontent.com/matilorenzatti/MVT-Lorenzatti/main/img_read/2.png)

Si abrimos el "DB Browser for SQLite", y arrastramos nuestro archivo .sqlite, podemos ver que la DB esta creada con éxito, y en ella nuestra tabla (o modelo) creado en Django, con los campos que nosotros mismos indicamos que se creen, mas el tipo de dato correcto.

![img_db](https://raw.githubusercontent.com/matilorenzatti/MVT-Lorenzatti/main/img_read/3.png)

Cuando accedemos a nuestra tabla **familia_app_familia**, podemos observar que los registros se crean automaticamente y de forma exitosa.

![img_registros](https://raw.githubusercontent.com/matilorenzatti/MVT-Lorenzatti/main/img_read/4.png)

Al ser el primer MVT con Django, solamente se contemplo en la view la creación de los registros en la tabla cada vez que se acceda al recurso (URL), de esta forma, si la pagina se recarga 10 veces, se van a insertar 10 veces los mismos registros. Esto se tiene en cuenta para futuras entregas, creando una view mas compleja que permita realizar un CRUD con los datos, mas un template diseñado para tal fin (que permita gestionar campos), en el cual, haya código dedicado a la verificación del tipo de dato ingresado, la integridad de la información, y la consulta previa a la DB para verificar si dicho registro (en su totalidad) existe o no en la DB.
