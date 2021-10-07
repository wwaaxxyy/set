# content of set_test.py
def is_set(number):
    if number is not 3:
        return False
    else:
        return True


def test_answer():
    assert is_set(3) == True

def test_wrong():
    assert is_set(2) == False