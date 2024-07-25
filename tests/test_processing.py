from typing import Any

import pytest

from src.processing import filter_by_state, sort_by_date

nonsense_as_arr = [None, 123, 1.2, "123", "bimbim", "bambam", "1234567123567123567123567123567123567123567"]


def test_filter_by_state_nonsense(nonsense: Any) -> None:
    for test_case in nonsense:
        assert filter_by_state(test_case) is None
        assert filter_by_state(test_case, test_case) is None
        assert filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            test_case,
        ) in [
            None,
            [],
        ]  # some nonsense is string


@pytest.mark.parametrize(
    "test_input, expected_result",
    [
        (nonsense_as_arr, []),  # just demonstrating correct work with list of strange things,
        # none of which is agreed operation
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
    ],
)
def test_filter_by_state_default(test_input: Any, expected_result: Any) -> None:
    assert filter_by_state(test_input) == expected_result


@pytest.mark.parametrize(
    "test_input, additional_parameter, expected_result",
    [
        (nonsense_as_arr, "CANCELED", []),  # just demonstrating correct work with list of strange things,
        # none of which is agreed operation
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
    ],
)
def test_filter_by_state_with_parameter(test_input: Any, additional_parameter: Any, expected_result: Any) -> None:
    assert filter_by_state(test_input, additional_parameter) == expected_result


def test_sort_by_date_nonsense(nonsense: Any) -> None:
    for test_case in nonsense:
        assert sort_by_date(test_case) is None
        assert sort_by_date(test_case, test_case) is None
        assert (
            sort_by_date(
                [
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                ],
                test_case,
            )
            is None
        )  # there is no bool in nonsense
        assert (
            sort_by_date([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03, 18:35:29"}]) is None
        )  # wrong date format


@pytest.mark.parametrize(
    "test_input, expected_result",
    [
        (nonsense_as_arr, None),  # just demonstrating correct work with list of strange things,
        # none of which is agreed operation
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
    ],
)
def test_sort_by_date_default(test_input: Any, expected_result: Any) -> None:
    assert sort_by_date(test_input) == expected_result


@pytest.mark.parametrize(
    "test_input, additional_parameter, expected_result",
    [
        (nonsense_as_arr, False, None),  # just demonstrating correct work with list of strange things,
        # none of which is agreed operation
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date_with_parameter(test_input: Any, additional_parameter: Any, expected_result: Any) -> None:
    assert sort_by_date(test_input, reverse=additional_parameter) == expected_result
