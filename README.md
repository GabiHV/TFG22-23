# Análisis de datos de temperatura y humedad de suelo procedentes de los sensores IoT desplegados en un viñedo
Repositorio del Trabajo Fin de Grado _"Análisis de datos de temperatura y humedad de suelo procedentes de sensores IoT desplegados en un viñedo"_.

Estado del proceso de desarrollo del TFG:
- [x] Preprocesamiento de datos 
- [x] Selección del modelo de RNA
- [x] Modelado de la red
- [x] Entrenamiento de la red 
- [x] Evaluación del modelo :arrow_left:

Autor:
- Gabriel Hernández Vallejo.

Tutores:
- Rubén Ruiz González
- Alejandro Merino Gómez
---
## Descripción:
En este proyecto se busca analizar los datos de temperatura y humedad a distintas profundidades de sensores IoT repartidos a lo largo de un viñedo. Para ello se realizarán visualizaciones interesentes sobre estos, realizando un análisis, de forma que se puedan buscar correlaciones entre las medidas obtenidas y las diferentes variables ambientales o geológicas del suelo.

## Estructura del proyecto:
El proyecto cuenta con la siguiente estructura de directorios y ficheros:
<font size="1">
>.</br>
>|-LICENSE.md -> fichero con licencia de uso de la aplicación.</br>
>|-README.md -> fichero con la información del proyecto.</br>
>|-src/ -> Directorio con los codigos fuente</br>
>|&emsp;&emsp;|-data-preprocessing.ipynb -> fichero notebook con el pre-procesamiento del conjunto de datos.</br>
>|&emsp;&emsp;|-ann-modeling.ipynb -> fichero notebook con el modelado de la RNA.</br>
>|&emsp;&emsp;|-env-paths.py -> script Python con los _paths_ de los diferentes recursos.</br>
>|&emsp;&emsp;|-pluviometer-plot.py -> script Python con función para graficar los datos del pluviometro.</br>
>|&emsp;&emsp;|-processed_pluviometer.py -> scripy Python para graficar los datos procesados del pluviómetro.</br>
>|&emsp;&emsp;|-processed_sensor.py -> scripy Python para graficar los datos procesados de los sensores.</br>
>|&emsp;&emsp;|-raw_pluviometer.py -> scripy Python para graficar los datos sin procesar del pluviómetro.</br>
>|&emsp;&emsp;|-raw_sensor.py -> scripy Python para graficar los datos sin procesar de los sensores.</br>
>|&emsp;&emsp;|-raw_pluviometer.py -> scripy Python para graficar los datos sin procesar del pluviómetro.</br>
>|&emsp;&emsp;|-sensor-plot.py -> script Python con función para graficar los datos de los sensores.</br>
>|&emsp;&emsp;|-modelGRU -> directorio con el modelo GRU obtenido.</br>
>|&emsp;&emsp;|-modelLSTM/ -> directorio con el modelo LSTM obtenido.</br>
>|&emsp;&emsp;|-modelMLP/ -> directorio con el modelo MLP obtenido.</br>
>|-scripts/</br>
>|&emsp;&emsp;|-requeriments.txt -> módulos requeridos para ejecutar los scripts de Python</br>
>|&emsp;&emsp;|-requeriments_conda.txt -> módulos requeridos para ejecutar los scripts de Python en Anaconda</br>
>|&emsp;&emsp;|-virtual_env.bat -> script para instalación del entorno virtual de Python junto con los módulos requeridos en CMD. </br>
>|&emsp;&emsp;|-virtual_env.sh -> script para instalación del entorno virtual de Python junto con los módulos requeridos en Bash.</br>
>|&emsp;&emsp;|-Virtual_env.ps1 -> script para instalación del entorno virtual de Python junto con los módulos requeridos en PowerShell.</br>
>|&emsp;&emsp;|-docker-install.sh -> script para instalación de Docker.</br>
>|&emsp;&emsp;|-docker-create.sh -> script para creación de contenedor de Docker para entrenamiento con CUDA y TensorFlow.</br>
>|&emsp;&emsp;|-init.sh -> script para la inicialización de las dependencias adicionales del contenedor.</br>
>|-img/</br>
>|&emsp;&emsp;|-graphics/ -> directorio que alberga diferentes gráficas de los datos.</br>
>|&emsp;&emsp;&emsp;&emsp;|-processed_data/ -> directorio que alberga las gráficas de los datos procesados de los sensores.</br>
>|&emsp;&emsp;&emsp;&emsp;|-raw_data/ -> directorio que alberga las gráficas de los datos _crudos_ de los sensores.</br>
>|-docs/</br>
>|&emsp;&emsp;|-img/ -> directorio que alberga las imágenes empleadas en la memoria del proyecto.</br>
>|&emsp;&emsp;|-tex/ -> directorio con las diferentes secciones de la memoria (ficheros LaTeX).</br>
>|&emsp;&emsp;|-.gitignore -> fichero con los módulos a ignorar en el control de versiones. </br>
>|&emsp;&emsp;|-anexos.pdf -> PDF de los anexos de la memoria del proyecto.</br>
>|&emsp;&emsp;|-anexos.tex -> fichero LaTeX de los anexos de la memoria.</br>
>|&emsp;&emsp;|-bibliografia.bib -> fichero con la bibliografía de la memoria.</br>
>|&emsp;&emsp;|-bibliografiaAnexos.bib -> fichero con la bibliográfia de los anexos de la memoria.</br>
>|&emsp;&emsp;|-memoria.pdf -> PDF de la memoria del proyecto.</br>
>|&emsp;&emsp;|-memoria.tex -> fichero LaTeX de la memoria del proyecto.</br>
>|&emsp;&emsp;|-README.md -> fichero con la información de la memoria del proyecto.</br>
>|-data/</br>
>&emsp;&emsp;|-raw_data/</br>
>&emsp;&emsp;|&emsp;&emsp;|-sensores/ -> directorio que alberga los muestreos de los diferentes sensores.</br>
>&emsp;&emsp;|&emsp;&emsp;|-pluviometro/ -> directorio que alberga los muestreos del pluviómetro.</br>
>&emsp;&emsp;|-classified_data/ -> directorio con los datos procesados.</br>
>&emsp;&emsp;|&emsp;&emsp;|-sensores/ -> directorio que alberga los datos procesados de los diferentes sensores.</br>
>&emsp;&emsp;|&emsp;&emsp;|-pluviometro/ -> directorio que alberga los datos procesados del pluviómetro.</br>
>&emsp;&emsp;|-integrated_data/ -> directorio que alberga un fichero con los datos integrados</br>
</font>

## Requisitos e instalación:

### Instalación de entorno virtual de Python para ejecución con CPU:
El proyecto se ha desarrollado y probado en [Python 3.9.13](https://www.python.org/downloads/release/python-3913/).
Para realizar la instalación del entorno virtual es necesario seguir los siguientes pasos.

Primero se deberá abrir una nueva sesión en la consola o terminal de Windows o Linux en el directorio del proyecto.
Posteriormente se deberá ejecutar el siguiente comando:

```
cd ./scripts/
```

Luego se pasará a ejecutar los scripts correspondientes dependiendo del sistema operativo instalado.

En sistemas Windows:

- PowerShell: La ejecución de scripts debe estar activada. Si no es el caso se debe ejecutar PowerShell como administrador y cambiar la política de ejecución de scripts: `Set-ExecutionPolicy Unrestricted`

&emsp;&emsp;&emsp;Tras esto podemos ejecutar el script:

```
./Virtual_env.ps1
```
- CMD: Para ejecutar el script en CMD basta con introducir:

```
virtual_env.bat
```

En sistemas Linux:

```
chmod +x virtual_env.sh && ./virtual_env.sh
```

Tras la ejecución de los scripts podemos proceder a la ejecución de los programas empleando el entorno virtual generado.

En el caso de los Python Notebook se deberá seleccionar el kernel de ejecución correspondiente. Se ha establecido en la instalación anterior con el nombre de *.venv*.

### Instalación de entorno para ejecución con GPU:
En el caso de disponer de una tarjeta gráfica NVIDIA compatible con la tecnología CUDA >= 11.7 se puede realizar la ejecución de los Python Notebooks empleando
la GPU (se debe contar con los controladores actualizados de la gráfica en cuestión).

Por otro lado, puede emplearse, de igual manera, servicios de terceros que realicen 
el mismo propósito sin la necesidad de la siguiente instalación, como el conocido
Google Colab.

Para la creación del servicio de Jupyter Notebook que permita la ejecución acelerada del entrenamiento de los modelos se disponen de diferentes _scripts_ en el directorio
con el mismo nombre.

Es preciso recalcar que los entornos se han probado en WSL y Ubuntu, de forma que en sistemas Windows será necesario contar con la tecnología mencionada para realizar la 
virtualización del contenedor.

Se proporciona el _script_ para realizar la instalación de Docker, paso que puede 
obviarse en caso de tener el servicio instalado en el sistema, aunque se recomienda 
realizar la instalación
limpia para evitar posibles incompatibilidades. Para comenzar el proceso de 
instalación se deberá situar en el directorio princiapal del proyecto y ejecutar el 
siguiente comando:
```
chmod +x ./scripts/docker-install.sh && ./scripts/docker-install.sh
```  

Una vez instalado Docker en el sistema, se debe comenzar con la instalación del
contenedor que virtualizará el servicio de Jupyter Notebook que permitirá la 
ejecución del entrenamiento con GPU. Para realizar el proceso mencionado se debe ejecutar el siguiente comando:
```
chmod +x ./scripts/docker-create.sh && ./scripts/docker-create.sh
```

Una vez descargado e iniciado el contenedor, se pueden ejecutar los Notebooks de 
creación de los modelos, para ello se debe acceder desde el navegador a la dirección
indicada en la terminal en la que se está ejecutando el servicio:
```
http://localhost:8888/?token=<token>
```
Dónde _\<token>_ se corresponde con el token de acceso (disponible en la localización
indicada).