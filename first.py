def get_even_nums(input_number_: int) -> list:
    """Create a sequence of even numbers from int number.

    Input number can be positive and negative, but can't be equal zero.
    Input number presents a number sequence from 0 to input number without even numbers.
    """
    if input_number_ == 0:
        print("Input number can't be zero")
        return [0]
    elif input_number_ > 0:
        input_number_ = list(range(input_number_))
        return [number for number in input_number_ if number % 2 == 0]
    else:
        input_number_ = list(range(input_number_, 0))
        return [number for number in input_number_ if number % 2 == 0]


def check_actual_result(expected_result, actual_result):
    assert actual_result == expected_result, f'Expected {expected_result}, got {actual_result}'
    assert actual_result is not None, f'Expected {expected_result}, got {actual_result}'
    assert actual_result != [0], f"Input can't be zero"


check_actual_result([0, 2, 4, 6, 8], get_even_nums(10))
check_actual_result([-4, -2], get_even_nums(-4))
check_actual_result([0], get_even_nums(0))
