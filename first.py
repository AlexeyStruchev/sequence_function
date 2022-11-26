def get_nums(input_number_: range) -> list:
    return [number for number in input_number_ if number % 2 == 0]


# nums_to_print = get_nums(range(-4, 0, 1))
# print(nums_to_print)


# def get_nums_2(length: int = -4) -> list[int]:
#     result: list[int] = []
#     for i in list(range(length, 0)):
#         if not i % 2:
#             result.append(i)
#     return result
input_values = (range(-4, 0), range(10, 0))
expected_values = ([-4, -2], [0, 2, 4, 6, 8])
dict_to_check = dict(map(lambda i, j: (i, j), input_values, expected_values))


def test_function_result(expected_result, actual_result):
    assert expected_result == actual_result, f'Expected {expected_result}, got {actual_result}'
    assert expected_result is not None, f'Expected {expected_result}, got {actual_result}'
    assert expected_result is not [], f'Expected {expected_result}, got {actual_result}'
    print()


for key, value in dict_to_check:
    test_function_result(value, key)

test_function_result([-4, -2], get_nums(range(-4, 0)))
# func_to_check = get_nums_2(10)
#
#
# def test() -> None:
#     print(func_to_check)
#     # assert func_to_check == [0, 2, 4, 6, 8]
#     assert get_nums_2(-4) == [-2]
#
#
# test()
