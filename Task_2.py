import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Generator function that yields numbers from a string that are separated
    by spaces on both sides and returns them
    """
    pattern = r'(?<=\s)\d+(?:\.\d+)?(?=\s)'  #pattern to search numbers real numbers (including decimal) with spaces on both sides
    for match in re.finditer(pattern, f' {text} '):
        yield float(match.group())

def sum_profit(text: str, func: Callable) -> float:
    """
    Returns the sum of the real numbers from the text
    """
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

