#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Oct 2019
# This program calculates area using multiple functions


def area(base, height):
    # This calculates area based on the base and height parameters

    # process
    area = (base * height) / 2

    # output
    print("The area of your triangle is " + str(area) + " units squared.")


def main():
    try:
        while True:
                # Input
                base = int(input("Input the base of your triangle: "))
                height = int(input("Input the height of your triangle: "))

                # Calls area function
                area(base, height)
                break
    except Exception:
        print("Please input proper numbers")


if __name__ == "__main__":
    main()
