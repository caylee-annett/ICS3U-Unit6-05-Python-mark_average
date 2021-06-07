#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: June 2021
# This program calculates the average of marks in a list


def calculate_average(list_of_marks):
    # This function calculates the average

    sum_of_numbers = 0

    for mark in list_of_marks:
        sum_of_numbers = sum_of_numbers + mark
    average = sum_of_numbers / (len(list_of_marks))
    rounded_average = average * 10
    rounded_average = rounded_average + 0.5
    rounded_average = int(rounded_average)
    rounded_average = rounded_average * 10 ** -1

    return rounded_average


def main():
    # This function gets the marks

    mark_list = []

    # Input & Process
    print("This program calculates the average of your marks.")
    print("")
    print("Enter one mark at a time and -1 to end.")
    mark_input_string = input("Enter a mark (%): ")
    while True:
        try:
            mark_input_integer = int(mark_input_string)

            if mark_input_integer == -1:
                break
            elif mark_input_integer < 0 or mark_input_integer > 100:
                mark_input_string = input("Invalid input. Enter a mark (%): ")
            else:
                mark_input_string = input("Enter a mark (%): ")
                mark_list.append(mark_input_integer)
        except Exception:
            mark_input_string = input("Invalid input. Enter a mark (%): ")

    # Call functions
    answer = calculate_average(mark_list)

    # Output
    print("")
    print("The average is: {}%".format(answer))
    print("\nDone.")


if __name__ == "__main__":
    main()
