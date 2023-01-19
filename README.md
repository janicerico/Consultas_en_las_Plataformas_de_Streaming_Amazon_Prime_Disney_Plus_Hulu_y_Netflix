## <h1 align=center> Proyecto Individual No. 1. Data Engineering

<p align="center">
<img src=https://user-images.githubusercontent.com/109157476/213493684-d39b7139-403c-4dac-873f-2505d3ec7fd9.png>

# <h1 align=center> Por: Janice Rico

<p align="center">
<img src=https://user-images.githubusercontent.com/109157476/213494110-56c2db2e-7789-4e59-90ea-9b6bf57196df.jpg>
</p>

## <h1 align=center> TEMA:
# <h1 align=center> Consultas en las Plataformas de Streaming: Amazon Prime, Disney Plus, Hulu y Netflix. 

 ## <h1 align=center> INTRODUCCIÓN
 
En este Proyecto se me pidió ser parte del equipo de Data Engineering, para cual nos fue solicitado de parte del área de Data Analytics ciertos requerimientos para el desarrollo óptimo de sus actividades. Éstos fueron realizar en los datos las transformaciones correspondientes y disponibilizarlos mediante la elaboración y ejecución de una API.

# <h1 align=center> DATOS: 
<h1 align=center> 4 tablas en formato .cvs correspondientes a cada plataforma de Streaming.
 
## <h1 align=center> TRANSFORMACIONES REQUERIDAS (Proceso de ETL)
 
Se hizo la ingesta de cada base de datos y una exploración de su tamaño, campos, tipo de datos, valores nulos. Luego se realizaron procesos de limpieza y normalización; entre ellas:
 
1. Generar un campo **id** conformado por la primera letra del nombre de la plataforma, seguido del show_id ya presente en el dataset.
2. Reemplazar los valores nulos del campo rating por la string **"G"** (que significa "general for all audiences").
3. Cambiar el formato de campos de fechas a **AAAA-mm-dd**.
4. Convertir todos los campos de texto a **minúsculas**.
5. Convertir el campo **duration** en **duration_int** y **duration_type**.

Finalmente, las 4 tablas se unificaron en una sola llamada **all_streaming.csv** para facilitar las consultas posteriores.

Estas transformaciones se encuentran ejecutadas en el Cuaderno de Jupyter con el nombre: **ETL.ipynb**
 
## <h1 align=center> DESARROLLO DE LA API

A través de usar el Framework **FastAPI** se creó el archivo **main.py** donde se pudo disponibilizar de las siguientes consultas:

1. Calcular la cantidad de veces que aparece una keyword en el título de películas y series, por plataforma.
   Parámetros de entrada: Plataforma, keyword.
   Nombre de la consulta: **get_word_count**
2. Calcular la cantidad de películas por plataforma con un puntaje mayor a XX en un determinado año.
   Parámetros de entrada: Plataforma, score, año.
   Nombre de la consulta: **get_score_count**
3. Mostrar la segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.
   Parámetros de entrada: Plataforma.
   Nombre de la consulta: **get_second_score**
4. Mostrar la película que más duró según año, plataforma y tipo de duración.
   Parámetros de entrada: Plataforma, tipo de duración, año.
   Nombre de la consulta: **get_longest**
5. Calcular la cantidad de series y películas por rating.
   Parámetros de entrada: Rating.
   Nombre de la consulta: **get_rating_count**

## <h1 align=center> DEPLOYMENT

Para disponibilizar la Aplicación de Consultas a los miembros del área de Data Analytic se utilizó la plataforma en la nube Deta. Para ello se utilizó el archivo **main.py** y los requerimientos detallados en **requirements.txt**.
 
Se puede acceder al proyecto completo a través de link: https://858ag3.deta.dev/docs#/
 
## <h1 align=center> VIDEO DEMOSTRATIVO

Para ver el funcionamiento de la API, se puede ir al siguiente link: 

Gracias por tomar de su tiempo y llegar hasta acá!
