## <h1 align=center> Proyecto Individual No. 1. Data Engineering

<p align="center">
<img src=https://github.com/janicerico/PI01_Data-Engineering/blob/main/Images/LOGO-HENRY.png>
</p>

# <h1 align=center> Por: Janice Rico

<p align="center">
<img src=https://github.com/janicerico/PI01_Data-Engineering/blob/main/Images/big%20data.jpg>
</p>

## <h1 align=center> TEMA:
# Consultas en las Plataformas de Streaming: Amazon Prime, Disney Plus, Hulu y Netflix. 

 ## <h1 align=center> INTRODUCCIÓN
 
En este Proyecto se me pidió ser parte del equipo de Data Engineering, para cual nos fue solicitado de parte del área de Data Analytics ciertos requerimientos para el desarrollo óptimo de sus actividades. Éstos fueron realizar en los datos las transformaciones correspondientes y disponibilizarlos mediante la elaboración y ejecución de una API.

# <h1 align=center> DATOS: 
4 tablas en formato .cvs correspondientes a cada plataforma de Streaming.
 
## <h1 align=center> TRANSFORMACIONES REQUERIDAS
 
1. Generar un campo **'id'** conformado por la primera letra del nombre de la plataforma, seguido del show_id ya presente en el dataset.
2. Reemplazar los valores nulos del campo rating por la string "G" (que significa "general for all audiences").
3. Cambiar el formato de campos de fechas a **'AAAA-mm-dd'**.
4. Convertir todos los campos de texto a **'minúsculas'**.
5. Convertir el campo **'duration'** en **'duration_int'** y **'duration_type'**.

Estas transformaciones correspondientes a un proceso de ETL se encuentran ejecutadas en el Cuaderno de Jupyter con el nombre: ETL.ipynb
 
## <h1 align=center> DESARROLLO DE LA API
