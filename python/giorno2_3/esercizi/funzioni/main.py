# Scrivere il codice dell'esercizi qui dentro

def pow_list(lista):
    lista1 = []
    for el in lista:
        lista1.append(el**2)
    return lista1

assert pow_list([1, 2, 3]) == [1, 4, 9], (
    "Implement a function that takes a list "
    "and returns another list with each value raised "
    "to the power of 2"
)

def count_words(stringa):
    return len(stringa.split(" "))


assert count_words("hello world"), (
    "Implement a trivial function that counts the "
    "number of words in the given string. "
    "Hint: try executing the following command in the "
    "Python console: 'hello world'.split(' ')"
)

def reverse_string(stringa):
    insieme_caratteri= list(stringa)
    insieme_caratteri.reverse()     #esiste anche [::-1]
    return ''.join(insieme_caratteri)


assert reverse_string("hello") == "olleh", (
    "Implement a function that takes a string "
    "and returns it reversed. For example, 'hello' becomes 'olleh'."
)

def factorial(n):
     if n == 0:
         return 1
     else:
         return n * factorial(n-1)   #ricorsione
    
#2 modalità per calcolare il fattoriale
def factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result

assert factorial(5) == 120, (
    "Implement a function that computes the factorial of a given number. "
    "Factorial of n (n!) is the product of all positive integers from 1 to n. "
    "For example, factorial(5) = 5 * 4 * 3 * 2 * 1."
)

#Il codice commentato serve a vedere cosa sucede quando passo la parola
def is_palindrome(stringa):
    #  if stringa == stringa[::-1]:
    #      controllo=True
    #      print (f"La stringa {stringa} è palindroma!!!")
    #  else: 
    #      controllo=False
    #  return controllo
    return stringa == stringa[::-1]

assert is_palindrome("racecar") == True, (
"Implement a function that checks if a given string is a palindrome. "
"A palindrome reads the same forwards and backwards, e.g., 'racecar'. "
"Hint: try executing the following command in the "
"Python console: 'racecar'[::-1]"
)

def sum_even_numbers(lista):
    somma=0
    for el in lista:
        if el%2==0:     #se il numero è pari
            somma+=el   #lo sommo
    return somma

assert sum_even_numbers([1, 2, 3, 4, 5]) == 6, (
    "Implement a function that takes a list of numbers "
    "and returns the sum of all even numbers in the list."
)

def find_max(lista):
    return max(lista)   #max è una funzione

assert find_max([3, 1, 4, 1, 5]) == 5, (
    "Implement a function that takes a list of numbers "
    "and returns the largest number in the list."
)

def count_vowels(stringa):
    vocali=["a","e","i","o","u"]
    count=0
    for el in stringa:
        if el in vocali:
            count+=1
    return count



assert count_vowels("hello world") == 3, (
    "Implement a function that takes a string "
    "and returns the count of vowels ('a', 'e', 'i', 'o', 'u') in it. "
    "For example, 'hello world' contains 3 vowels."
)