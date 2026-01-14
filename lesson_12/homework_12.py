def calculate_total_sea_area(black_sea: int, azov_sea: int) -> int:
    return black_sea + azov_sea

def calculate_warehouse_goods(total: int, first_plus_second: int, second_plus_third: int) -> tuple[int, int, int]:
    second = first_plus_second + second_plus_third - total
    first = total - second_plus_third
    third = total - first_plus_second


    if first < 0 or second < 0 or third < 0:
        return (0, 0, 0)

    return (first, second, third)

def calculate_total_price(price_per_month: int, months: int) -> int:
    return price_per_month * months

def normalize_spaces(text):
    return " ".join(text.split())


def count_h(text):
    return text.count("h")