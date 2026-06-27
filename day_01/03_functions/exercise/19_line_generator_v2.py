# TODO: Create a function `line_generator` that has a parameter `number` and prints the following:
line_generator_input = int(input("Enter the number of lines: "))

# TODO: Use the function once
def line_generator(line_generator_input):
    for line in range(line_generator_input):
         print(f"Line {line + 1}")
line_generator(line_generator_input)