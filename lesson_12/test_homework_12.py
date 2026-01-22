import pytest
from lesson_12.homework_12 import (
    calculate_total_sea_area,
    calculate_warehouse_goods,
    calculate_total_price,
    normalize_spaces,
    count_h
)


# ---------- calculate_total_sea_area ----------
def test_calculate_total_sea_area_positive():
    assert calculate_total_sea_area(436000, 39000) == 475000


def test_calculate_total_sea_area_zero():
    assert calculate_total_sea_area(0, 0) == 0


# ---------- calculate_warehouse_goods ----------
def test_calculate_warehouse_goods_normal():
    assert calculate_warehouse_goods(100, 70, 60) == (40, 30, 30)


def test_calculate_warehouse_goods_equal():
    assert calculate_warehouse_goods(60, 40, 40) == (20, 20, 20)


# ---------- calculate_total_price ----------
def test_calculate_total_price_positive():
    assert calculate_total_price(500, 6) == 3000


def test_calculate_total_price_zero_months():
    assert calculate_total_price(500, 0) == 0


# ---------- normalize_spaces ----------
def test_normalize_spaces_multiple():
    assert normalize_spaces("hello     world") == "hello world"


def test_normalize_spaces_leading_trailing():
    assert normalize_spaces("   hello world   ") == "hello world"


def test_normalize_spaces_single_word():
    assert normalize_spaces("hello") == "hello"


# ---------- count_h ----------
def test_count_h_multiple():
    assert count_h("hhhello h") == 4


def test_count_h_none():
    assert count_h("abcde") == 0

