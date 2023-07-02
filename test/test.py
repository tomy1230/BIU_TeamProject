import pytest
@pytest.fixture
def numbers():
    a = 10
    b = 20
    return [a,b]

class TestApp:
    def test_multiplication(self, numbers):
        res =2*numbers[0]
        assert res == numbers[1]

    def test_division(self, numbers):
        res = numbers[1]//2
        assert res == numbers[0]