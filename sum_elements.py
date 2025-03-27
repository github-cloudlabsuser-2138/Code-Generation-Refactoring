# A refactored example of a program in Python. It prompts the user for the number of elements to sum, takes those integers as input, and handles basic error cases.

from typing import List
import sys

MAX = 100
MIN = 1


def calculate_sum(numbers: List[int]) -> int:
    """Calculate the sum of a list of integers."""
    return sum(numbers)


def get_integer_input(prompt: str, error_message: str = "Invalid input. Please enter a valid integer.") -> int:
    """Prompt the user for an integer input, handling invalid inputs."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(error_message)


def get_number_of_elements() -> int:
    """Prompt the user for the number of elements to sum, ensuring it is within the valid range."""
    while True:
        n = get_integer_input(f"Enter the number of elements ({MIN}-{MAX}): ")
        if MIN <= n <= MAX:
            return n
        print(f"Invalid input. Please provide a number between {MIN} and {MAX}.")


def get_elements(n: int) -> List[int]:
    """Prompt the user to input a list of integers."""
    print(f"Enter {n} integers:")
    return [get_integer_input("> ") for _ in range(n)]


def main() -> None:
    """Main function to execute the program."""
    try:
        n = get_number_of_elements()
        elements = get_elements(n)
        total = calculate_sum(elements)
        print("Sum of the numbers:", total)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        sys.exit(1)


if __name__ == "__main__":
    main()
