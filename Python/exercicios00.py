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


"""
Criar um dicionário de frutas e preços
Crie um dicionário onde as chaves são os nomes de frutas e os valores são seus preços. Escreva uma função que recebe o nome de uma fruta e retorna seu preço. Se a fruta não estiver no dicionário, retorne uma mensagem dizendo que a fruta não foi encontrada.
"""

frutas = {'banana': 1.75, 'laranja': 2.99, 'pesego': 1.99}

def preco_fruta(fruta):
    if fruta in frutas:
        return frutas[fruta]
    return "fruta nao encontrada"
    

"""
Dada uma lista de palavras, crie um dicionário que conta quantas vezes cada palavra aparece.
"""

palavras = ["gato", "cachorro", "gato", "pássaro", "gato", "cachorro"]

def contador(lista):
    valores_contados = {}
    for dado in lista:
        if dado in valores_contados:
            valores_contados[dado] += 1
        else:
            valores_contados[dado] = 1

    return valores_contados

"""
Intermediário: Tradutor simples
Crie um dicionário que funcione como um tradutor inglês-português. Escreva uma função que recebe uma palavra em inglês e retorna sua tradução em português. Se a palavra não existir no dicionário, retorne "Palavra não encontrada".
"""

tradutor = {
    "dog": "cachorro",
    "cat": "gato",
    "bird": "pássaro"
}

def traducao(palavra):
    return tradutor.get(palavra, "Palavra não encontrada")

"""
Crie um dicionário que armazena as notas de alunos. Escreva uma função que calcula a média das notas de um aluno específico. Se o aluno não existir, retorne uma mensagem de erro.
"""

alunos = {
    "João": [7, 8, 9],
    "Maria": [10, 9, 8],
    "Pedro": [6, 7, 8]
}

def media_aluno(nome):
    if nome in alunos:
        return sum(alunos[nome]) / len(alunos[nome])
    return 'Aluno nao existe'



"""
Crie uma função chamada adicionar_elemento que recebe uma lista e um valor. A função deve adicionar o valor ao final da lista, se ele ainda não estiver presente.
"""

def adicionar_elemento(lista, valor):
    return lista.append(valor)


lista_exemplo = [1, 2, 3]
adicionar_elemento(lista_exemplo, 4)
print(lista_exemplo)  # Saída: [1, 2, 3, 4]


"""
Crie uma função que recebe uma lista de números e a ordena de forma crescente e depois de forma decrescente.
"""

def ordenar_lista(lista):
    lista.sort()
    print(lista)

# Testes:
numeros = [5, 3, 8, 6, 2]

"""
Crie uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados.
"""

def remover_duplicatas(lista):
    return sorted(set(lista))

# Testes:
lista_com_duplicatas = [1, 2, 2, 3, 4, 4, 5]
print(remover_duplicatas(lista_com_duplicatas))  # Saída esperada: [1, 2, 3, 4, 5]


"""
Crie uma função que recebe uma tupla e um valor, e retorna True se o valor estiver na tupla, ou False caso contrário.
"""

def verificar_valor(tupla, valor):
    return valor in tupla

# Testes:
minha_tupla = (10, 20, 30, 40)


"""
Crie uma função que, dada uma lista de números, encontre o segundo maior e o segundo menor número.
"""

def segundo_maior_menor(lista):
    lista.sort()
    return f'segundo menor: {lista[1]}, segundo maior: {lista[-2]} '

# Testes:
numeros = [12, 45, 2, 30, 10, 22]



"""
Exercício 2: Somatório dos Números Divisíveis por 3 e 5
Escreva uma função que receba um número inteiro positivo n e retorne a soma de todos os números entre 1 e n que são divisíveis por 3 ou 5.
"""

def soma_divisiveis(n):
    """result = []
    for v in range(n+1):
        if v %3 == 0 or v %5 == 0:
            result.append(v)
    return sum(result)"""
    return sum([v for v in range(n+1) if v % 3 == 0 or v % 5 == 0])
    


# Teste

"""
Exercício 3: Contador de Caracteres Mais Frequente
Crie uma função que receba uma string e retorne o caractere que aparece com mais frequência. Se houver empate, retorne o que aparece primeiro.
"""

def caractere_mais_frequente(s):
    result = {}
    for n in list(s):
        if n  in result:
            result[n] += 1
        else:
            result[n] = 1
    return max(result, key=result.get)
