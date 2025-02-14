from src.mask import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    """
    Проверяет, что функция правильно маскирует номер карты,
    отображая первые 6 цифр и последние 4 цифры.
    """
    assert get_mask_card_number(1111111111111111) == "1111 11** **** 1111"
    assert get_mask_card_number(1000200030004000) == "1000 20** **** 4000"


def test_get_mask_account() -> None:
    """
    Проверяет, что функция правильно маскирует номер счета,
    отображая только последние 4 цифры.
    """
    assert get_mask_account(3693693693693693) == "**3693"
    assert get_mask_account(808080808) == "**0808"
