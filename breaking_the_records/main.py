#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#


def breakingRecords(scores):
    minimum = scores[0]
    maximum = scores[0]
    min_breaks = 0
    max_breaks = 0

    for score in scores:
        if score > maximum:
            maximum = score
            max_breaks += 1
        elif score < minimum:
            minimum = score
            min_breaks += 1

    return max_breaks, min_breaks


if __name__ == "__main__":
    result = breakingRecords([0, 10, 12, 6, 50, 1])

    print(result)
