import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Генератор, який знаходить усі дійсні числа у тексті
    та повертає їх як float.
    """
    
    numbers = re.findall(r'\d+\.\d+|\d+', text)

    for num in numbers:
        yield float(num)


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Обчислює загальну суму чисел, знайдених у тексті.
    Використовує генератор, переданий через параметр func.
    """
    return sum(func(text))

if __name__ == "__main__":
    text = (
        "Загальний дохід працівника складається з декількох частин: "
        "100020.01 як основний дохід, доповнений додатковими надходженнями "
        "227.45 і 3234.00 доларів."
    )

    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income:.2f}")
