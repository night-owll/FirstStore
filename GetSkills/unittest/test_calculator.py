from calculator import Calculator

def test_add():
    c=Calculator(1,2)
    result=c.add()
    assert result==3,"加法验证失败"

def test_mul():
    c=Calculator(3,3)
    result = c.mul()
    assert result==10,"除法验证失败"

if __name__ == "__main__":
    test_mul()
    test_add()