def fibonacci(n):
    """计算第n个斐波那契数（从0开始）"""
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def test_fibonacci():
    assert fibonacci(0) == 0, "fibonacci(0) 应该等于 0"
    assert fibonacci(1) == 1, "fibonacci(1) 应该等于 1"
    assert fibonacci(2) == 1, "fibonacci(2) 应该等于 1"
    assert fibonacci(3) == 2, "fibonacci(3) 应该等于 2"
    assert fibonacci(10) == 55, "fibonacci(10) 应该等于 55"
    print("所有测试通过！")

if __name__ == "__main__":
    test_fibonacci()