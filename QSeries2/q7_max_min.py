def min_max():
    """find out max and min score using lambda function"""
    standard = [("V", 62), ("VI", 68), ("VII", 72), ("VIII", 70), ("IX", 74), ("X", 65)]
    minimum = min(standard, key=lambda x: x[1])[1]
    maximum = max(standard, key=lambda x: x[1])[1]
    print((minimum, maximum))

min_max()
