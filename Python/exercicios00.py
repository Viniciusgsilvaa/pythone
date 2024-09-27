"""
Two red beads are placed between every two blue beads. There are N blue beads. After looking at the arrangement below work out the number of red beads.

@ @@ @ @@ @ @@ @ @@ @ @@ @ def

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

"""
Write a function, isItLetter or is_it_letter or IsItLetter, which tells us if a given character is a letter or not.
"""

def is_it_letter(s):
    return s.isalpha()

"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

Find the unique number (this kata)
Find the unique string
Find The Unique
"""

def find_uniq(arr):
    for n in arr:
        if arr.count(n) == 1:
            return n

"""
Well met with Fibonacci bigger brother, AKA Tribonacci.

As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(

So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this sequence:

[1, 1 ,1, 3, 5, 9, 17, 31, ...]
But what if we started with [0, 0, 1] as a signature? As starting with [0, 1] instead of [1, 1] basically shifts the common Fibonacci sequence by once place, you may be tempted to think that we would get the same sequence shifted by 2 places, but that is not the case and we would get:

[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a signature array/list, returns the first n elements - signature included of the so seeded sequence.

Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, then return an empty array (except in C return NULL) and be ready for anything else which is not clearly specified ;)
"""

def tribonacci(s, n):
    if n == 0:
        return []
    elif n <= 3:
        return s[:n]
    
    a = s
    for x in range(3, n):
        next = sum(a[-3:])
        a.append(next)
    return a

"""
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.
"""

def disemvowel(string):
    a = string
    for n in 'aeiouAEIOU':
        a = a.replace(n, '')
    return a

"""
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#, empty table in COBOL) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

Example:
divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"
"""

def divisors(integer):
    div = []
    for n in range(2, integer):
        if integer % n == 0:
            div.append(n)
    if len(div) > 0:
        return div
    else:
        return f'{integer} is prime'

"""
Complete the function which returns the weekday according to the input number:

1 returns "Sunday"
2 returns "Monday"
3 returns "Tuesday"
4 returns "Wednesday"
5 returns "Thursday"
6 returns "Friday"
7 returns "Saturday"
Otherwise returns "Wrong, please enter a number between 1 and 7"
"""

def whatday(num):
    days = ["Wrong, please enter a number between 1 and 7", "Sunday", "Monday", 
          "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if num > 7:
        return "Wrong, please enter a number between 1 and 7"
    return days[num]

"""
A cake is sliced with n straight lines. Your task is to calculate the maximum number of pieces the cake can have.

Example
For n = 0, the output should be 1.

For n = 1, the output should be 2.

For n = 2, the output should be 4.

For n = 3, the output should be 7.

Input/Output
[input] integer n
0 ≤ n ≤ 10000

[output] an integer
The maximum number of pieces the sliced cake can have.
"""

def cake_slice(n):
    return n*(n+1)/2 +1

"""
Write a function named first_non_repeating_letter† that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("");

† Note: the function is called firstNonRepeatingLetter for historical reasons, but your function should handle any Unicode character.
"""

def first_non_repeating_letter(s):
    a = list(s.lower())
    x = 0
    c = 0
    for n in a:
        c += 1
        if a.count(n) == 1:
            x+=1
            break
    if x== 0:
        return ''
    return s[c-1]

"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 
"""

def move_zeros(lst):
    nz = [n for n in lst if n != 0]
    cz = lst.count(0)
    nz.extend([0] * cz)
    return nz


def verificar_numero(n):
    if n == 0:
        return 'Zero'
    elif n % 2 == 0:
        return 'Par'
    return 'Impar'


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num_par_mult = [numero * 2 for numero in numeros if numero % 2 == 0]

"""
. Verificação de Palíndromos
Escreva uma função chamada verificar_palindromo que recebe uma string e retorna True se ela for um palíndromo (a string lida de trás para frente é igual à string original) e False caso contrário.
"""

def verificar_palindromo(string):
    return string == string[::-1]

print(verificar_palindromo("recrinircer"))


"""
2. Soma Recursiva
Implemente uma função recursiva chamada soma_recursiva que recebe uma lista de números e retorna a soma de todos os elementos da lista. Não use loops!
"""

def soma_recursiva(lista):
    return sum(lista)

"""3. Remover Duplicatas de uma Lista
Crie uma função chamada remover_duplicatas que recebe uma lista de números e retorna uma nova lista sem elementos duplicados, mantendo a ordem original.
"""


def remover_duplicatas(lista):
    lista1 = []

    for n in lista:
        if n not in lista1:
            lista1.append(n)
    return lista1

print(remover_duplicatas([1, 2, 3, 1, 2, 4, 5]))  # Saída: [1, 2, 3, 4, 5]
print(remover_duplicatas([7, 6, 5, 8, 10, 7, 7, 8, 9]))  # Saída: [7, 8, 9]