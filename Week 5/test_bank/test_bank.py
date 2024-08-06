from bank import value


def test_value_hello():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("Hello, Newman") == 0
    assert value("hello there") == 0
    assert value("HELLO") == 0
    assert value("HELLO, newman") == 0


def test_value_h():
    assert value("Hey") == 20
    assert value("howdy") == 20
    assert value("How you doing?") == 20
    assert value("Hi there!") == 20
    assert value("h") == 20
    assert value("H") == 20


def test_value_other():
    assert value("Good morning") == 100
    assert value("What's up?") == 100
    assert value("Greetings") == 100
    assert value("Nice to meet you") == 100
    assert value("good evening") == 100
    assert value("Hi, how are you?") == 20
