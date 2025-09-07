def remove_odd_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]


def main():
    original_list = [1, 4, 7, 10, 13, 16]  # Example list
    filtered_list = remove_odd_numbers(original_list)

    print(f"Original list: {original_list}")
    print(f"List with odd numbers removed: {filtered_list}")


main()
