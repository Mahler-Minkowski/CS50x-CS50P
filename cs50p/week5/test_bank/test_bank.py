from cs50p.week5.test_bank.bank import value
def test_U():
    assert value('HELLO')=='0$'
    assert value('HELL')=='20$'
    assert value('ELLO')=='100$'
def test_l():
    assert value('hello')=='0$'
    assert value('hell')=='20$'
    assert value('ello')=='100$'
def test_greeting():
    assert value("hello world") == '0$'
    assert value("HELLO WORLD") == '0$'
    assert value("hi world") == '20$'
    assert value("HI WORLD") == '20$'
    assert value("wassup world") == '100$'
    assert value("WASSUP WORLD") == '100$'
