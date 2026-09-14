from cs50p.week5.test_fuel.fuel import convert
from cs50p.week5.test_fuel.fuel import gauge
def test_co():
    assert convert('1/2')==50
    assert convert('1/4')==25
def test_gu():
    assert gauge(50)=='50%'
    assert gauge(0)=='E'
    assert gauge(0.03)=='E'
    assert gauge(99.6)=='F'


