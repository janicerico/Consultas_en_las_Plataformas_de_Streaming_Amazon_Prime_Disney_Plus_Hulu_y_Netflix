## <h1 align=center> Proyecto Individual No. 1. Data Engineering
## <h1 align=center> Etapa de LABs - Carrera: Data Science

<p align="center">
<img src=https://user-images.githubusercontent.com/109157476/213493684-d39b7139-403c-4dac-873f-2505d3ec7fd9.png>

# <h1 align=center> Por: Janice Rico

<p align="center">
<img src=https://user-images.githubusercontent.com/109157476/213494110-56c2db2e-7789-4e59-90ea-9b6bf57196df.jpg>

## <h1 align=center> TEMA:
# <h1 align=center> Consultas en las Plataformas de Streaming: Amazon Prime, Disney Plus, Hulu y Netflix. 

 ## <h1 align=center> INTRODUCCIÓN
 
En este Proyecto se me pidió ser parte del equipo de Data Engineering, para cual nos fue solicitado de parte del área de Data Analytics ciertos requerimientos para el desarrollo óptimo de sus actividades. Éstos fueron realizar en los datos las transformaciones correspondientes y disponibilizarlos mediante la elaboración y ejecución de una API.

# <h1 align=center> DATOS: 
<h1 align=center> 4 tablas en formato .cvs correspondientes a cada plataforma de Streaming.
 
## <h1 align=center> TRANSFORMACIONES REQUERIDAS (Proceso de ETL)

<p align="center">
<img src=https://user-images.githubusercontent.com/109157476/213510702-9b868883-d3d5-4ab2-876a-ef1fc26719b4.png>

<p align="center">
<img src=https://user-images.githubusercontent.com/109157476/213511000-6a4ed6bb-6339-49f5-b615-bdb84676a5ab.png>
 
Se hizo la ingesta de cada base de datos en Python, utilizando la librería de Pandas, así como una exploración de su tamaño, campos, tipo de datos, valores nulos. Luego se realizaron procesos de limpieza y normalización; entre ellas:
 
1. Generar un campo **id** conformado por la primera letra del nombre de la plataforma, seguido del show_id ya presente en el dataset.
2. Reemplazar los valores nulos del campo rating por la string **"G"** (que significa "general for all audiences").
3. Cambiar el formato de campos de fechas a **AAAA-mm-dd**.
4. Convertir todos los campos de texto a **minúsculas**.
5. Convertir el campo **duration** en **duration_int** y **duration_type**.

Finalmente, las 4 tablas se unificaron en una sola llamada **all_streaming.csv** para facilitar las consultas posteriores.

Estas transformaciones se encuentran ejecutadas en el Cuaderno de Jupyter con el nombre: **ETL.ipynb**
 
## <h1 align=center> DESARROLLO DE LA API

<p align="center">
<img src=https://user-images.githubusercontent.com/109157476/213511190-67941f25-3e6e-4e04-ad10-59387b250e63.png>

A través de usar el Framework **FastAPI** se creó el archivo **main.py** donde se pudo disponibilizar de las siguientes consultas:

1. Calcular la cantidad de veces que aparece una keyword en el título de películas y series, por plataforma.</p>
   Parámetros de entrada: Plataforma, keyword.</p>
   Nombre de la consulta: **get_word_count**</p>
2. Calcular la cantidad de películas por plataforma con un puntaje mayor a XX en un determinado año.</p>
   Parámetros de entrada: Plataforma, score, año.</p>
   Nombre de la consulta: **get_score_count**</p>
3. Mostrar la segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.</p>
   Parámetros de entrada: Plataforma.</p>
   Nombre de la consulta: **get_second_score**</p>
4. Mostrar la película que más duró según año, plataforma y tipo de duración.</p>
   Parámetros de entrada: Plataforma, tipo de duración, año.</p>
   Nombre de la consulta: **get_longest**</p>
5. Calcular la cantidad de series y películas por rating.</p>
   Parámetros de entrada: Rating.</p>
   Nombre de la consulta: **get_rating_count**</p>

## <h1 align=center> DEPLOYMENT

<p align="center">
<img src=https://user-images.githubusercontent.com/109157476/213511843-02ce1997-8353-403f-bbf6-c1e926590ae9.png>

Para disponibilizar la Aplicación de Consultas a los miembros del área de Data Analytic se hizo el despliegue a través de la plataforma en la nube Deta. Para ello se utilizó el archivo **main.py** y los requerimientos detallados en **requirements.txt**.
 
Se puede acceder al proyecto completo a través del link: https://858ag3.deta.dev/docs#/
 
## <h1 align=center> VIDEO DEMOSTRATIVO

<p align="center">
<img src=https://user-images.githubusercontent.com/109157476/213512211-8eb8d4fc-b47b-43e2-bb68-423b567889b7.png>

Para ver el funcionamiento de la API, se puede ir al siguiente link: 

Gracias por tomar de su tiempo y llegar hasta acá!
