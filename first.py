def get_nums(input_number_: int) -> list:
    if input_number_ == 0:
        print("Input number can't be zero")
        return [0]
    elif input_number_ > 0:
        input_number_ = list(range(input_number_))
        return [number for number in input_number_ if number % 2 == 0]
    else:
        input_number_ = list(range(input_number_, 0))
        return [number for number in input_number_ if number % 2 == 0]


def function_result(expected_result, actual_result):
    assert expected_result == actual_result, f'Expected {expected_result}, got {actual_result}'
    assert expected_result is not None, f'Expected {expected_result}, got {actual_result}'
    assert expected_result is not [], f'Expected {expected_result}, got {actual_result}'


function_result([0, 2, 4, 6, 8], get_nums(10))
function_result([-4, -2], get_nums(-4))
function_result([0], get_nums(0))
