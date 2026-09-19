# Actividad Integradora – Conversor de Unidades

**Nombre:** [Tu nombre completo]
**Repositorio:** https://github.com/emilianogalaviz/actividadIntegradoraP1

Programa de consola en Python que solicita un valor numérico y realiza conversiones de temperatura, distancia y moneda. Las pruebas se implementan con **pytest** (fixture, `assert`, markers y `parametrize`).

## Estructura del repositorio

```
.
├── unit_converter.py      # Software: clase UnitConverter + menú de consola
├── test_converter.py      # Casos de prueba con pytest
├── pytest.ini             # Configuración de pytest (markers y log)
├── test.log               # Log generado por la ejecución de las pruebas
└── README.md
```

## Ejecución

```bash
pip install pytest

python unit_converter.py      # Ejecutar el programa
pytest                        # Ejecutar todas las pruebas
pytest -v                     # Detalle por prueba
pytest -m unit                # Solo pruebas unitarias
pytest -m system              # Solo pruebas de sistema
```

## Conversiones

| Opción | Conversión |
|---|---|
| 1 | Celsius → Fahrenheit |
| 2 | Fahrenheit → Celsius |
| 3 | Kilómetros → Millas |
| 4 | Millas → Kilómetros |
| 5 | Pesos Mexicanos → Dólares |
| 6 | Dólares → Pesos Mexicanos |

Tasa fija definida en el programa: **1 USD = 17.50 MXN** (`UnitConverter.MXN_PER_USD`).

## Requerimientos

| ID | Tipo | Requerimiento |
|---|---|---|
| RF01 | Funcional | El sistema deberá permitir convertir Celsius a Fahrenheit. |
| RF02 | Funcional | El sistema deberá permitir convertir Fahrenheit a Celsius. |
| RF03 | Funcional | El sistema deberá permitir convertir Kilómetros a Millas. |
| RF04 | Funcional | El sistema deberá permitir convertir Millas a Kilómetros. |
| RF05 | Funcional | El sistema deberá permitir convertir Pesos Mexicanos a Dólares. |
| RF06 | Funcional | El sistema deberá permitir convertir Dólares a Pesos Mexicanos. |
| RF07 | Funcional | El sistema deberá solicitar un valor numérico y rechazar entradas que no sean números válidos (texto, vacío, NaN) o negativas en distancia y moneda. |
| RF08 | Funcional | El sistema deberá mostrar un menú y rechazar opciones que no existan. |
| RNF01 | No funcional | El sistema deberá mostrar los resultados con una precisión de al menos dos decimales. |
| RNF02 | No funcional | El sistema deberá utilizar una tasa de cambio fija definida dentro del programa. |
| RNF03 | No funcional | El sistema deberá mostrar mensajes de error claros en español sin cerrarse ante una entrada inválida. |
| RNF04 | No funcional | El sistema deberá ejecutarse desde consola con Python 3.8+ sin dependencias externas (pytest solo para pruebas). |

## Casos de prueba

Los casos TC01–TC08 son pruebas unitarias (`@pytest.mark.unit`) y TC09–TC13 son pruebas de sistema (`@pytest.mark.system`). Los casos unitarios están parametrizados con `@pytest.mark.parametrize`.

| ID | Descripción | Req. | Entradas | Resultado esperado | Resultado obtenido |
|---|---|---|---|---|---|
| TC01 | Convertir Celsius a Fahrenheit | RF01 | 0, 100, -40, 37 °C | 32.00, 212.00, -40.00, 98.60 °F | ✅ Pasó (4/4) |
| TC02 | Convertir Fahrenheit a Celsius | RF02 | 32, 212, -40, 98.6 °F | 0.00, 100.00, -40.00, 37.00 °C | ✅ Pasó (4/4) |
| TC03 | Convertir Kilómetros a Millas | RF03 | 0, 1, 10, 42.195 km | 0.00, 0.62, 6.21, 26.22 mi | ✅ Pasó (4/4) |
| TC04 | Convertir Millas a Kilómetros | RF04 | 0, 1, 10, 26.2 mi | 0.00, 1.61, 16.09, 42.16 km | ✅ Pasó (4/4) |
| TC05 | Convertir Pesos a Dólares (tasa 17.50) | RF05 | 0, 17.5, 175, 100 MXN | 0.00, 1.00, 10.00, 5.71 USD | ✅ Pasó (4/4) |
| TC06 | Convertir Dólares a Pesos (tasa 17.50) | RF06 | 0, 1, 10, 0.5 USD | 0.00, 17.50, 175.00, 8.75 MXN | ✅ Pasó (4/4) |
| TC07 | Validar que la entrada sea un número real | RF07 | 5, -3.2, "abc", None, True, NaN | True, True, False, False, False, False | ✅ Pasó (6/6) |
| TC08 | Verificar precisión de 2 decimales | RNF01 | 1, 3, 7.777, 36.6666 | Resultados con máximo 2 decimales | ✅ Pasó (4/4) |
| TC09 | Flujo completo Celsius → Fahrenheit | RF01, RF07, RNF01 | Opción 1, valor 100 | `Celsius a Fahrenheit: 100.00 °C = 212.00 °F` | ✅ Pasó |
| TC10 | Distancia negativa | RF07, RNF03 | Opción 3, valor -5 | Mensaje de error por valor negativo | ✅ Pasó |
| TC11 | Entrada no numérica | RF07, RNF03 | Opción 5, valor "abc" | Mensaje de error por número inválido | ✅ Pasó |
| TC12 | Opción de menú inexistente | RF08, RNF03 | Opción 9, valor 10 | Mensaje de error por opción no válida | ✅ Pasó |
| TC13 | Tasa fija definida en el programa | RF05, RNF02 | Opción 5, valor 175 | `10.00 USD` con tasa 17.50 | ✅ Pasó |

## Evidencia de ejecución

Salida de `pytest -v` (el log completo queda en `test.log`):

```
collected 39 items
...
============================== 39 passed in 0.04s ==============================
```
