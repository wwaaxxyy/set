# content of set_test.py
def is_set():
    return True


def test_answer():
    assert is_set() == True

def test_wrong():
    assert is_set() is not 42