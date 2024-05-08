from main import kangaroo


def test_kangaroo():
    # Test case where kangaroos meet
    assert kangaroo(0, 3, 4, 2) == "YES"
    # Test case where kangaroos don't meet
    assert kangaroo(0, 2, 5, 3) == "NO"
    # Test case where kangaroos start at the same position
    assert kangaroo(0, 3, 2, 2) == "YES"
    # Test case where kangaroos have same speed
    assert kangaroo(0, 2, 10, 2) == "NO"
    # Test case where kangaroos have same speed and position
    assert kangaroo(0, 2, 3, 2) == "NO"
    # Test case where kangaroos start at negative positions
    assert kangaroo(-10, 2, -5, 3) == "NO"
    # Test case where kangaroos have negative speed
    assert kangaroo(0, -3, 5, -2) == "NO"
    # Test case where kangaroos have large positions and speeds
    assert kangaroo(1000000000, 1000000000, 1000000001, 1000000000) == "NO"
    assert kangaroo(0, 1000000000, 1000000000, 1000000000) == "NO"
    assert kangaroo(0, 1, 1000000000, 1000000000) == "NO"

if __name__ == "__main__":
    test_kangaroo()
    print("All tests passed!")
