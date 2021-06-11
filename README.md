# examenB2

Este proyecto como examen de prueba de conocimientos, contiene lo siguiente:

1. Template realizado con bootstrap.



2. Para ejecutar la base de datos se deben ejecutar los siguientes comandos desde la consola:
   python manage.py makemigrations
   python manage.py migrate


3. Para correr el proyecto se debe ejecutar el siguiente comando desde la consola:
   python manage.py runserver



4. La url principal para listar los empleados es:
   /empleados



5. La url del login para poder accesar al sistema administrativo en donde se podran registrar,modificar y eliminar los usuarios es:
   /admin/login



6. El usuario por default para poder ingresar al sistema es:
   Usuario : admin
   Contraseña : 123
 
 

7. En caso de que el usuario proporcionado no funcione para poder accesar al sistema, puede crear uno con el siguiente comando desde la consola:
   python manage.py createsuperuser
 
 
 
8. En caso de que el usuario quiera realizar alguna acción en el template de empleados primero tendra que estar
   logueado, en caso contrario sera redireccionado al login.
