
import calculator as cal

class TestCalculator():
    

    def test_add(a,b):
        return cal.Calculator.add(a,b)==5
    def sub(a,b):
        return cal.Calculator.sub(a,b)==2
    


if __name__ == "__main__":
    TestCalculator.test_add(2,3)
    TestCalculator.sub(5,3)
