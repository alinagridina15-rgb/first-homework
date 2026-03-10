import allure
import pytest


@allure.step("Sum {a} + {b}")
def add(a, b):
    return a + b


@allure.step("Divide {a} / {b}")
def divide(a, b):
    return a / b


@allure.feature("Math operations")
@allure.title("Addition works correctly")
def test_addition():

    with allure.step("Prepare numbers"):
        a = 2
        b = 3

    with allure.step("Calculate result"):
        result = add(a, b)

    with allure.step("Verify result"):
        assert result == 5


@allure.feature("Math operations")
@allure.title("Division works correctly")
def test_division():

    with allure.step("Prepare numbers"):
        a = 10
        b = 2

    with allure.step("Divide numbers"):
        result = divide(a, b)

    with allure.step("Verify result"):
        assert result == 5


@allure.feature("Math operations")
@allure.title("Division by zero throws error")
def test_divide_by_zero():

    with allure.step("Prepare numbers"):
        a = 10
        b = 0

    with allure.step("Verify exception"):
        with pytest.raises(ZeroDivisionError):
            divide(a, b)


@allure.feature("String operations")
@allure.title("String uppercase works")
def test_uppercase():

    with allure.step("Prepare string"):
        text = "python"

    with allure.step("Convert to upper"):
        result = text.upper()

    with allure.step("Verify"):
        assert result == "PYTHON"