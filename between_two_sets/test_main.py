from main import getTotalX


def test_getTotalX():
    assert getTotalX([2, 4], [16, 32, 96]) == 3

    assert getTotalX([3, 4], [24, 48]) == 2

    assert getTotalX([3, 4, 6], [24, 36]) == 1

    assert getTotalX([2, 3, 6], [24, 36]) == 2

    assert getTotalX([3, 5, 7], [105, 210, 420]) == 1

    print("All test cases pass")


if __name__ == "__main__":
    test_getTotalX()
