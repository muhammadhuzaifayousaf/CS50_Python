from um import count


def test_um():
    assert count("hello, um, world") == 1
    assert count("Um, um, um, that's interesting") == 3
    assert count("yummy") == 0
    assert count("umbrella") == 0
    assert count("um? UM! Um.") == 3
    assert count("") == 0
    assert count("Um, UM, um") == 3
