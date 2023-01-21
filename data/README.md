# DESCRIPCIÓN DEL CONJUNTO DE DATOS

El conjunto de datos empleados en la _RNA_ (Red Neuronal Artificial) se compondrán de las lecturas de los 8 sensores desplegados por el viñedo y del pluviómetro que medidirá las precipitaciones en la zona.

## Parámetros comunes
Tanto los sensores como el pluviómetro cuentan con entradas comunes como:
- Ts: timestamp de lectura de los datos en **segundos** desde ###Introducir Fecha de Inicio###.
- Fecha: fecha de la lectura de los datos en formato **yy/mm/dd, hh:mm:ss**.
- Bateria: nivel de batería del sensor en **mV**.

## Sensores de temperatura y humedad del suelo 
Las lecturas de los sensores se encuentran en los ficheros denominados `sensorx.csv` y cuenta con los siguientes parámetros:
- T_ext:
- H_ext:
- T_C_cal:
- H_C_cal:
- T_L_cal:
- H_L_cal:
- H_C:
- H_L:

## Pluviómetro
En lo que se refiere a los datos del pluviómetro se encuentran en `pluviometro.csv` y cuenta con los siguientes parámetros:
- Pluv:
- Pluv_delta:
- Pluv_delta MM: