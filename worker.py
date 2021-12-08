from main import Money, Methods


def main_func():
    first_value = Money()
    second_value = Money()
    first_value.read()
    second_value.read()
    full = Methods()
    return full.sub(first_value.to_string(), second_value.to_string()), full.mul(first_value.to_string()), \
           full.compere(first_value.to_string(), second_value.to_string()), full.increment(first_value.to_string()), \
           full.decrement(first_value.to_string())


print(main_func())
