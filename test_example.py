from team5_mlops.example import greet


def test_greet_returns_name():
    assert greet("Team 5") == "Hello, Team 5!"
