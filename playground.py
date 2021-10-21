x = 2
y = 3

result = x + y

print(result)
print("the final result is " + str(result))
print(f"the final result is {result}")

print("\n" + 30 * "=" + "\n")


def some_function_name(first_number, second_number):
    print("in some_function_name")
    return first_number + second_number


def some_other_function_name(first_number: int, second_number: int) -> int:
    print("in some_other_function_name")
    return first_number + second_number


print(f"result of some_function_name: {some_function_name(4, 8)}")
print()
print(f"result of some_other_function_name: {some_other_function_name(15, 16)}")
