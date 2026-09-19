import unit_converter
import logging
import pytest

logging.basicConfig(
    level=logging.DEBUG,
    filemode='w',
    filename='test.log'
)


@pytest.fixture
def system():
    return unit_converter.UnitConverter()


# ---------------------- PRUEBAS UNITARIAS ----------------------

@pytest.mark.parametrize("celsius, expected", [
    (0, 32.00),
    (100, 212.00),
    (-40, -40.00),
    (37, 98.60)
])
@pytest.mark.unit
def test_celsius_to_fahrenheit(system, celsius, expected):
    """TC01 - RF01"""
    result = system.celsius_to_fahrenheit(celsius)
    assert result == expected


@pytest.mark.parametrize("fahrenheit, expected", [
    (32, 0.00),
    (212, 100.00),
    (-40, -40.00),
    (98.6, 37.00)
])
@pytest.mark.unit
def test_fahrenheit_to_celsius(system, fahrenheit, expected):
    """TC02 - RF02"""
    result = system.fahrenheit_to_celsius(fahrenheit)
    assert result == expected


@pytest.mark.parametrize("km, expected", [
    (0, 0.00),
    (1, 0.62),
    (10, 6.21),
    (42.195, 26.22)
])
@pytest.mark.unit
def test_km_to_miles(system, km, expected):
    """TC03 - RF03"""
    result = system.km_to_miles(km)
    assert result == expected


@pytest.mark.parametrize("miles, expected", [
    (0, 0.00),
    (1, 1.61),
    (10, 16.09),
    (26.2, 42.16)
])
@pytest.mark.unit
def test_miles_to_km(system, miles, expected):
    """TC04 - RF04"""
    result = system.miles_to_km(miles)
    assert result == expected


@pytest.mark.parametrize("mxn, expected", [
    (0, 0.00),
    (17.5, 1.00),
    (175, 10.00),
    (100, 5.71)
])
@pytest.mark.unit
def test_mxn_to_usd(system, mxn, expected):
    """TC05 - RF05 (tasa fija 17.50)"""
    result = system.mxn_to_usd(mxn)
    assert result == expected


@pytest.mark.parametrize("usd, expected", [
    (0, 0.00),
    (1, 17.50),
    (10, 175.00),
    (0.5, 8.75)
])
@pytest.mark.unit
def test_usd_to_mxn(system, usd, expected):
    """TC06 - RF06 (tasa fija 17.50)"""
    result = system.usd_to_mxn(usd)
    assert result == expected


@pytest.mark.parametrize("value, expected", [
    (5, True),
    (-3.2, True),
    ("abc", False),
    (None, False),
    (True, False),
    (float("nan"), False)
])
@pytest.mark.unit
def test_validate_number(system, value, expected):
    """TC07 - RF07"""
    result = system.validate_number(value)
    assert result == expected


@pytest.mark.parametrize("value", [1, 3, 7.777, 36.6666])
@pytest.mark.unit
def test_precision_two_decimals(system, value):
    """TC08 - RNF01"""
    results = [
        system.celsius_to_fahrenheit(value),
        system.km_to_miles(value),
        system.mxn_to_usd(value),
    ]
    for result in results:
        decimals = str(result).split(".")[1]
        assert len(decimals) <= 2


# ---------------------- PRUEBAS DE SISTEMA ----------------------

@pytest.mark.system
def test_system_celsius_full_flow(system):
    logging.info('TC09 RF01, RF07, RNF01')
    result = system.convert("1", "100")
    assert '212.00' in result
    logging.info(f'The conversion result is: {result}')
    logging.info('Test case finished')


@pytest.mark.system
def test_system_negative_distance(system):
    logging.info('TC10 RF07, RNF03')
    result = system.convert("3", "-5")
    assert 'negativo' in result
    logging.info(f'The conversion result is: {result}')
    logging.info('Test case finished')


@pytest.mark.system
def test_system_non_numeric_input(system):
    logging.info('TC11 RF07, RNF03')
    result = system.convert("5", "abc")
    assert 'número válido' in result
    logging.info(f'The conversion result is: {result}')
    logging.info('Test case finished')


@pytest.mark.system
def test_system_invalid_option(system):
    logging.info('TC12 RF08, RNF03')
    result = system.convert("9", "10")
    assert 'opción no válida' in result
    logging.info(f'The conversion result is: {result}')
    logging.info('Test case finished')


@pytest.mark.system
def test_system_fixed_rate(system):
    logging.info('TC13 RF05, RNF02')
    assert system.mxn_per_usd == 17.50
    result = system.convert("5", "175")
    assert '10.00 USD' in result
    logging.info(f'The conversion result is: {result}')
    logging.info('Test case finished')


if __name__ == '__main__':
    test_system_celsius_full_flow(unit_converter.UnitConverter())