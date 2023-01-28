# DESCRIPCIÓN DEL CONJUNTO DE DATOS

El conjunto de datos empleados en la _RNA_ (Red Neuronal Artificial) se compondrán de las lecturas de los 8 sensores desplegados por el viñedo y del pluviómetro que medidirá las precipitaciones en la zona.

## Parámetros comunes
Tanto los sensores como el pluviómetro cuentan con entradas comunes como:
- Ts: timestamp de lectura de los datos en **milisegundos** desde 1 de enero de 1970 (_Unix Epochs_).
- Fecha: fecha de la lectura de los datos en formato **yy/mm/dd, hh:mm:ss**.
- Bateria: nivel de batería del sensor en **V**.

## Sensores de temperatura y humedad del suelo 
Las lecturas de los sensores se encuentran en los ficheros denominados `sensorx.csv` y cuenta con los siguientes parámetros:
- T_ext: temperatura externa en **ºC**, es decir, la temperatura captada por los sensores externos.
- H_ext: humedad externa, es decir, la humedad del ambiente relativa (en **%**).
- T_C_cal: temperatura superficial del suelo en **ºC**.
- H_C_cal: humedad relativa superficial del suelo (a 20 cm).
- T_L_cal: temperatura del suelo a profundidad mayor que T_C_cal en **ºC**.
- H_L_cal: humedad del suelo a profundidad mayor que H_C_cal.
- H_C: humedad superficial sin calibrar (valor entero relacionado con la capacitancia).
- H_L: humedad profunda sin calibrar (valor entero relacionado con la capacitancia).

## Pluviómetro
En lo que se refiere a los datos del pluviómetro se encuentran en `pluviometro.csv` y cuenta con los siguientes parámetros:
- Pluv: contador que indica cuántas veces se ha inclinado el balancín del pluviómetro. 
- Pluv_delta: indica el incremento desde la última lectura hasta la actual (Pluv<sub>actual</sub> - Pluv<sub>anterior</sub>)
- Pluv_delta MM: lluvia en **mm** (litros/m<sup>2</sup>) desde la última lectura hasta la actual.