- Simulador de Gasto Diario

  El **Simulador de Gasto Diario** es una aplicación de consola diseñada para ayudar a los usuarios a registrar y monitorear sus gastos diarios en diferentes categorías, como comida, transporte, entretenimiento, entre otros. Este simulador permite llevar un control básico de los gastos diarios, semanales o mensuales y obtener un resumen o reporte de los gastos en cada categoría. Toda la información se guarda en un archivo JSON, lo que permite mantener un historial de gastos entre distintas sesiones del programa.

  

  # **Problemática**

  Muchos usuarios desean llevar un registro de sus gastos, pero las aplicaciones de gestión financiera completas pueden ser complicadas y requieren configuraciones avanzadas. Este proyecto ofrece una solución simple y accesible para aquellos que buscan hacer un seguimiento básico de sus gastos en un formato amigable y sin demasiadas complejidades. Con el Simulador de Gasto Diario, los usuarios pueden organizar sus gastos de forma práctica y recibir una visión clara de su situación financiera diaria, semanal o mensual.

  

  # Tecnologías y Herramientas

  - Front-end: 
  - Recursos: 
  - Diseño de los menus: https://gist.github.com/programmersland/cf9362472f1b9f245415d9cee96c7aef
  - Librería para mostrar la información en formato de tablas:  https://pypi.org/project/tabulate/
  - GitHub: Para la gestión de versiones del código en el desarrollo, usando conventional commits.

  # Funcionalidades Principales

  1. Registrar Gasto:

  - Permite al usuario ingresar un nuevo gasto, especificando la cantidad, categoría (como comida, transporte, etc.) y una breve descripción opcional.
  - Guarda esta información en un archivo JSON para conservar el registro entre sesiones.

  1. Listar Gastos:

  - Muestra todos los gastos registrados, con detalles como fecha, categoría, cantidad, y descripción.
  - Filtra los gastos por categoría o rango de fechas (por ejemplo, para ver solo los gastos de "transporte" o solo los del "último mes").

  1. Calcular Gastos Totales y por Categoría:

  - Calcula el total de gastos diarios, semanales o mensuales, y permite ver el gasto acumulado en cada categoría.
  - Proporciona un desglose por categorías para identificar en qué áreas se gasta más.

  1. Generar Reporte:

  - Genera un resumen o reporte de gastos en formato texto, detallando los totales diarios, semanales o mensuales, y los gastos en cada categoría.
  - El reporte puede guardarse en un archivo JSON o mostrarse en pantalla, según la preferencia del usuario.

  1. Guardar y Cargar Datos:

  - Guarda automáticamente los registros en un archivo JSON cada vez que se registra o actualiza un gasto.
  - Carga los datos del archivo JSON al iniciar el programa, permitiendo al usuario retomar desde donde quedó en la última sesión.

Resultado esperado

La entrega de este proyecto se realizará de forma individual (Si el Trainer lo aplica lo podrá hacer en grupo), donde se debe anexar un enlace a un repositorio en GitHub privado (compartido como colaborador  a las cuentas que el trailer indique) llamado “Proyecto_Python_ApellidoNombre” (Proyecto_Python_Apellido1Nombre1Apellido2Nombre2 donde aplique) que contenga el código de la aplicación construida en Python. En este mismo repositorio, debe contener los siguientes archivos:

- Archivo principal de ejecución basado en Python.
- Archivos modularizados que den funcionalidad al programa principal de Python.
- Archivo JSON que almacene la información del programa en sí.