from numb3rs import validate
def test_v():
    assert validate('127.1.1.0')==True
    assert validate('127.254.1.0')==True
    assert validate('127.1.37.0')==True
    assert validate('66.1.1.0')==True
    assert validate('123.45.67.98')==True
def test_zero():
    assert validate('001.002.003.004')==False
