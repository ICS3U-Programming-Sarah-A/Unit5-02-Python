#!/usr/bin/env python3

# Created by: Sarah
# Created on: May 6th, 2022.
# This program asks the user to enter a base & height of a triangle.
# It then calculates the area of the triangle and displays it to the user.


def calculate_area(base, height):
    # calculate the area of the triangle.
    area = (base * height)/2

    # displays area
    print("The area of the triangle is {:,.2f} cm^2.".format(area))
    


def main():
    # get user input from user
    base_user_str = input("Enter the base of the triangle (cm): ")
    height_user_str = input("Enter the height of the triangle (cm): ")
    print("")

    try:
        # convert string into a float.
        base_user_float = float(base_user_str)

        try:
            # converts string into float
            height_user_float = float(height_user_str)

            # sets a range
            if base_user_float > 0 and height_user_float > 0:
                # calls function
                calculate_area(base_user_float, height_user_float)
            else:
                print("The base and height must be greater than 0.")

        # handles error case
        except Exception:
            print("{} is not a valid number.".format(height_user_str))

    # handles error case.
    except Exception:
        print("{} is not a valid number.".format(base_user_str))


if __name__ == "__main__":
    main()
