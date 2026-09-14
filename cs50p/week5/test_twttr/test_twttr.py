from cs50p.week5.test_twttr.twttr import shorten
def test_sentence():
    assert shorten('YOU ARE my')=='Y R my'
def test_voc():
    assert shorten('suckmydick')=='sckmydck'
