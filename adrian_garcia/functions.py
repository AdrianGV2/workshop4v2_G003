def add(a, b):
    return a + b


def divide(a, b):
    return a / (b if b != 0 else 1)


def get_element(list_, index):
    return list_[index]

def convert_to_integer(value):
    return int(float(value))