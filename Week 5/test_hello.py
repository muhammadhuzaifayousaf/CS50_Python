from hello import hello

def test_argument():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello("Huzaifa") == "hello, Huzaifa"


def test_default():
    assert hello() == "hello, world"
