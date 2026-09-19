import math


class UnitConverter:
    """Conversor de unidades: temperatura, distancia y moneda."""

    # Tasa fija definida en el programa (RNF02)
    MXN_PER_USD = 17.50
    KM_PER_MILE = 1.609344
    DECIMALS = 2

    def __init__(self, mxn_per_usd=MXN_PER_USD):
        self.mxn_per_usd = mxn_per_usd
        # opcion: (descripcion, unidad origen, unidad destino, funcion, permite negativos)
        self.options = {
            "1": ("Celsius a Fahrenheit", "°C", "°F", self.celsius_to_fahrenheit, True),
            "2": ("Fahrenheit a Celsius", "°F", "°C", self.fahrenheit_to_celsius, True),
            "3": ("Kilómetros a Millas", "km", "mi", self.km_to_miles, False),
            "4": ("Millas a Kilómetros", "mi", "km", self.miles_to_km, False),
            "5": ("Pesos a Dólares", "MXN", "USD", self.mxn_to_usd, False),
            "6": ("Dólares a Pesos", "USD", "MXN", self.usd_to_mxn, False),
        }

    # ---------- Validaciones ----------
    def validate_number(self, value):
        """True si value es un número real finito (bool no cuenta como número)."""
        return (
            isinstance(value, (int, float))
            and not isinstance(value, bool)
            and math.isfinite(value)
        )

    def parse_value(self, raw):
        """Convierte la entrada (str o número) a float. Regresa None si no es válida."""
        if isinstance(raw, str):
            try:
                raw = float(raw.strip())
            except ValueError:
                return None
        if not self.validate_number(raw):
            return None
        return float(raw)

    # ---------- Conversiones ----------
    def celsius_to_fahrenheit(self, celsius):
        return round(celsius * 9 / 5 + 32, self.DECIMALS)

    def fahrenheit_to_celsius(self, fahrenheit):
        return round((fahrenheit - 32) * 5 / 9, self.DECIMALS)

    def km_to_miles(self, km):
        return round(km / self.KM_PER_MILE, self.DECIMALS)

    def miles_to_km(self, miles):
        return round(miles * self.KM_PER_MILE, self.DECIMALS)

    def mxn_to_usd(self, mxn):
        return round(mxn / self.mxn_per_usd, self.DECIMALS)

    def usd_to_mxn(self, usd):
        return round(usd * self.mxn_per_usd, self.DECIMALS)

    # ---------- Flujo completo ----------
    def convert(self, option, raw_value):
        if option not in self.options:
            return "Error: opción no válida. Elige un número del 1 al 6."

        label, unit_from, unit_to, func, allow_negative = self.options[option]

        value = self.parse_value(raw_value)
        if value is None:
            return "Error: el valor ingresado no es un número válido."
        if value < 0 and not allow_negative:
            return "Error: el valor no puede ser negativo para esta conversión."

        result = func(value)
        return f"{label}: {value:.2f} {unit_from} = {result:.2f} {unit_to}"


MENU = """
===== CONVERSOR DE UNIDADES =====
1. Celsius a Fahrenheit
2. Fahrenheit a Celsius
3. Kilómetros a Millas
4. Millas a Kilómetros
5. Pesos Mexicanos a Dólares
6. Dólares a Pesos Mexicanos
0. Salir
"""


def main():
    converter = UnitConverter()
    print(f"Tasa fija: 1 USD = {converter.mxn_per_usd:.2f} MXN")
    while True:
        print(MENU)
        option = input("Selecciona una opción: ").strip()
        if option == "0":
            print("Hasta luego.")
            break
        if option not in converter.options:
            print(converter.convert(option, ""))
            continue
        raw_value = input("Ingresa el valor a convertir: ")
        print(converter.convert(option, raw_value))


if __name__ == "__main__":
    main()