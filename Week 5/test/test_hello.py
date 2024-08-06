from hello import hello

def test_argument():
    assert hello("Huzaifa") == "hello, Huzaifa"


def test_default():
    assert hello() == "hello, world"
