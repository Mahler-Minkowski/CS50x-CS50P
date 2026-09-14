from cs50p.week5.test_plate.plates import is_valid
def test():
    assert is_valid('REFDE')==False
    assert is_valid('REFDE5')==True
    assert is_valid('33333')==False
    assert is_valid('2333ER')==False
    assert is_valid('RFD45T')==False
    assert is_valid('EDFG05')==False
    assert is_valid('EDFG?5')==False
