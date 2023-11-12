# Subnetting Calculator Script

Este repositorio contiene un script de Python diseñado para calcular la máscara de subred necesaria basada en los requisitos de la cantidad de subredes y hosts por subred para direcciones IP de Clase A, B y C.

## Descripción

El script solicita a los usuarios la clase de dirección IP y los requerimientos de subredes y hosts por subred. Luego, realiza cálculos para determinar cuántos bits se deben pedir prestados del espacio de host para cumplir con estos requisitos. El resultado incluye el número de bits para subredes y la máscara de subred total en formatos decimal y binario.

## Ejecución del Script

Para ejecutar este script, necesitarás una versión de Python 3. Se ha probado con Python 3.8.

```bash
python3 IPCalculator.py
```

## Ejemplo para Clase B

```bash
Para la dirección IP de Clase B:
Número de bits para subredes: 4
Máscara de subred total: 255.255.240.0
Máscara de subred en formato binario: 11111111.11111111.11110000.00000000
```

## Ejemplo para Clase C

```bash
Para la dirección IP de Clase C:
Número de bits para subredes: 2
Máscara de subred total: 255.255.255.192
Máscara de subred en formato binario: 11111111.11111111.11111111.11000000
```
