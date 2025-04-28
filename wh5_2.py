import re
from typing import Callable


def generator_numbers(text):
    numbers = re.findall(r"\s([-+]?\d*\.\d+|\d+)\s", text)

    for i in numbers:
        yield i

def sum_profit(text: str, func: Callable):
    result = 0.0
    for number in func(text):
        result += float(number)

    return result

input_text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(input_text, generator_numbers)
print(f"Загальний дохід: {total_income}")


