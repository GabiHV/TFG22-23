# Análisis de datos de temperatura y humedad de suelo procedentes de los sensores IoT desplegados en un viñedo
Repositorio del Trabajo Fin de Grado "Análisis de datos de temperatura y huemedad de suelo procedentes de sensores IoT desplegados en un viñedo".

Estado del proceso de desarrollo del TFG:
- [x] Preprocesamiento de datos 
- [ ] Selección del modelo de RNA :arrow_left:
- [ ] Modelado de la red
- [ ] Entrenamiento de la red
- [ ] Evaluación del modelo

Autor:
- Gabriel Hernábdez Vallejo.

Tutores:
- Rubén Ruiz González
- Alejandro Merino Gómez
---
## Descripción:
En este proyecto se busca analizar los datos de temperatura y humedad a distintas profundidades de sensores IoT repartidos a lo largo de un viñedo. Para ello se realizarán visualizaciones interesentes sobre estos, realizando un análisis, de forma que se puedan buscar correlaciones entre las medidas obtenidas y las diferentes variables ambientales o geológicas del suelo.

## Estructura del proyecto:
El proyecto cuenta con la siguiente estructura de directorios y ficheros:
```
.
|-LICENSE.md -> fichero con licencia de uso de la aplicación.
|-README.md -> fichero con la información del proyecto.
|-data-preprocessing.ipynb -> fichero notebook con el pre-procesamiento del conjunto de datos.
|-graficas_datos.py -> script Python que permite graficar los datos procesados de los sensores.
|-scipts/
|   |-requeriments.txt -> módulos requeridos para ejecutar los scripts de Python
|   |-virtual_env.bat -> script para instalación del entorno virtual de Python junto con los módulos requeridos. 
|   |-virtual_env.sh -> script para instalación del entorno virtual de Python junto con los módulos requeridos.
|-img/
|   |-graphics/ -> directorio que alberga las gráficas de los datos de los diferentes sensores.
|-docs/
|   |-img/ -> directorio que alberga las imágenes empleadas en la memoria del proyecto.
|   |-tex/ -> directorio con las diferentes secciones de la memoria (ficheros LaTeX).
|   |-.gitignore -> fichero con los módulos a ignorar en el control de versiones. 
|   |-anexos.pdf -> PDF de los anexos de la memoria del proyecto.
|   |-anexos.tex -> fichero LaTeX de los anexos de la memoria.
|   |-bibliografia.bib -> fichero con la bibliografía de la memoria.
|   |-bibliografiaAnexos.bib -> fichero con la bibliográfia de los anexos de la memoria.
|   |-memoria.pdf -> PDF de la memoria del proyecto.
|   |-memoria.tex -> fichero LaTeX de la memoria del proyecto.
|   |-README.md -> fichero con la información de la memoria del proyecto.
|-data/
    |-raw_data/
    |   |-sensores/ -> directorio que alberga los muestreos de los diferentes datos.
    |   |-pluviometro/ -> directorio que alberga los muestreos del pluviómetro.
    |-classified_data/ -> directorio con los datos procesados.
```

## Requisitos e instalación:
El proyecto se ha desarrollado y probado en [Python 3.9.13](https://www.python.org/downloads/release/python-3913/).
Para realizar la instalación del entorno virtual es necesario seguir los siguientes pasos.

Primero se deberá abrir una nueva sesión en la consola o terminal de Windows o Linux en el directorio del proyecto.
Posteriormente se deberá ejecutar el siguiente comando:

```cd ./scripts/```

Luego se pasará a ejecutar los scripts correspondientes dependiendo del sistema operativo instalado.

En sistemas Windows:

```./virtual_env.bat```

En sistemas Linux:

```./virtual_env.sh```

Tras la ejecución de los scripts podemos cerrar el terminal y proceder a la ejecución de los programas empleando el entorno virtual generado.