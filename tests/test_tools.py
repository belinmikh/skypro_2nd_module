from typing import Any

import pytest

from src.tools import extract


def test_extract() -> None:

    tale = {
        "Остров Буян": {
            "Дуб 0": None,
            "Дуб 1": "Жёлудь",
            "Дуб 2": {
                "Сундук": {
                    "Заяц": {
                        "Утка": {
                            "Яйцо": {
                                "Игла": "Смерть кощеева"
                            }
                        }
                    },
                    "Бутылка рома": "Смерть (одно и то же)"
                },
                "Сова": "А я думала камера"
            },
            "Дуб 3": "Кот учёный (сказкой ошибся)"
        },
        "Остров Пасхи": {
            "Статуи": [
                "Рожа 0",
                "Рожа 1",
                "Рожа 2"]
        }
    }
    # Wrong path testing
    assert extract(tale, (
        "Остров Буян",
        "Тот берег моря",
        "Хромая блоха",
        "Лужа",
        "Орёл",
        "Птенец",
        "Город",
        "Заяц",
        "Тулуп",
        "Какой заяц?! Какой орёл?!")) is None
    # Not full path testing
    assert extract(tale, (
        "Остров Пасхи",)) == {"Статуи": ["Рожа 0", "Рожа 1", "Рожа 2"]}
    # Full path testing
    assert extract(tale, (
        "Остров Буян",
        "Дуб 2",
        "Сундук",
        "Заяц",
        "Утка",
        "Яйцо",
        "Игла")) == "Смерть кощеева"


@pytest.mark.parametrize("test_input0, test_input1", [
    ("bimbim", ("ye", "yo")),
    ({"lol": "kek"}, 123),
    (321, "bambam")
])
def test_extract_bad_input(test_input0: Any, test_input1: Any) -> None:
    assert extract(test_input0, test_input1) is None
