from src.widget import mask_account_card


def test_mask_account_card() -> None:
    """Тест маскировки номера карты и счета.
    Проверяет корректность маскировки."""

    input_string: str = "Visa Platinum 1111222233334444"
    expected_output: str = "Visa Platinum 1111 22** **** 4444"
    result: str = mask_account_card(input_string)

    if result != expected_output:
        print(f"Ошибка: Ожидаемый результат '{expected_output}', " f"получено '{result}'")

    input_string = "Счет 9999888877776666"
    expected_output = "Счет **6666"
    result = mask_account_card(input_string)

    if result != expected_output:
        print(f"Ошибка: Ожидаемый результат '{expected_output}', " f"получено '{result}'")


if __name__ == "__main__":
    test_mask_account_card()
