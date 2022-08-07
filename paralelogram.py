def repeatChar(numRepeats, outputChar):
    # this function outputs the output char numRepeats times
    output = ""
    for i in range(numRepeats):
        output = output + outputChar
    return output


def main():
    print("This program will output a prallelogram.")

    side = int(input("How long do you want wach side to be? "))
    char = input("Please enter the character you want it to be made of: ")
    output = ""
    # loop to output the top triangle
    for i in range(1, side + 1):
        output = output + repeatChar(i, char) + "\n"
    # loop to output the bottom triangle
    for i in range(1, side + 1):
        # appnds the empty space i times and then appends the char
        output = output + repeatChar(i, " ") + repeatChar((side - i), char) + "\n"
    print(output)


main()