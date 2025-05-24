import pytest
from src.main import Frame, score


@pytest.mark.parametrize(
    ("score_sheet,expected_score"),
    [
        ("-- -- -- -- -- -- -- -- -- --", 0),
        ("1- -- -- -- -- -- -- -- -- --", 1),
        ("11 -- -- -- -- -- -- -- -- --", 2),
        ("11 1- -- -- -- -- -- -- -- --", 3),
        ("11 5- -- -- -- -- -- -- -- --", 7),
        ("11 11 11 11 11 11 11 11 11 11", 20),
        ("1/ -- -- -- -- -- -- -- -- --", 10),
        ("1/ 5- -- -- -- -- -- -- -- --", 20),
        ("1/ 54 -- -- -- -- -- -- -- --", 24),
        ("4/ 4- -- -- -- -- -- -- -- --", 18),
        ("4/ 4- X -- -- -- -- -- -- --", 28),
        ("4/ 4- X 1- -- -- -- -- -- --", 30),
        ("4/ 4- X 14 -- -- -- -- -- --", 38),
        ("4/ 4- X X X 1- -- -- -- --", 81),
        ("4/ 4- X 4/ X 1- -- -- -- --", 70),
        ("X X X X X X X X X XXX", 300),
        ("6/ 7- -- -4 51 -- -/ 3- -- 9/X", 70),
        ("1/ 27 X X 4/ X 3/ 52 71 0/4", 149),
        ("1/ 27 X X 4/ X 3/ 52 71 XX4", 159),
        ("1/ 27 X X 4/ X 3/ 52 71 X3/", 155),
    ],
)
def test_bowling(score_sheet, expected_score):
    assert score(score_sheet) == expected_score


@pytest.mark.parametrize(
    ("score_sheet,expected_score"),
    [
        ("--", 0),
        ("-1", 1),
        ("11", 2),
        ("1/", 10),
        ("5/", 10),
        ("5/3", 13),
        ("5/32", 13),
        ("X", 10),
        ("X5-", 15),
        ("XXX", 30),
        ("XXXX", 30),
    ],
)
def test_frame(score_sheet, expected_score):
    f = Frame()
    for i in score_sheet:
        f.take_roll(i)
    assert f.score == expected_score
