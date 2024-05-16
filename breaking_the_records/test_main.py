from main import breakingRecords


def testBreakingRecords():
    assert breakingRecords([10, 12, 2, 5, 56]) == (2, 1)

    assert breakingRecords([0, 10, 12, 6, 50, 1]) == (3, 0)

    print("All test cases pass")


if __name__ == "__main__":
    testBreakingRecords()
