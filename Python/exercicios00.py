"""
Two red beads are placed between every two blue beads. There are N blue beads. After looking at the arrangement below work out the number of red beads.

@ @@ @ @@ @ @@ @ @@ @ @@ @

Implement count_red_beads(n) (in PHP count_red_beads($n); in Java, Javascript, TypeScript, C, C++ countRedBeads(n)) so that it returns the number of red beads.
If there are less than 2 blue beads return 0.

"""

def count_red_beads(n):
    if n < 3:
        return 0
    else:
        return 2 * (n-1)
    
"""
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.

Don't forget the space after the closing parentheses!
"""

def create_phone_number(numbers):
    # Verificação do tamanho do array
    if len(numbers) != 10:
        raise ValueError("O array deve conter exatamente 10 inteiros")

    # Dividindo o array em partes
    area_code = "".join(map(str, numbers[:3]))
    first_part = "".join(map(str, numbers[3:6]))
    second_part = "".join(map(str, numbers[6:]))

    # Construindo a string final no formato desejado
    phone_number = f"({area_code}) {first_part}-{second_part}"

    return phone_number

"""
There was a test in your class and you passed it. Congratulations!

But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!

Return true if you're better, else false!
"""

def better_than_average(c, yp):
    return sum(c) / len(c) < yp