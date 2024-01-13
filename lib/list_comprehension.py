#!/usr/bin/env python3

def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = return_evens(numbers)
print(result)

def make_exclamation(sentence_list):
    return [sentence + '!' for sentence in sentence_list]

sentences = ["Hello", "How are you", "Python is great"]
result = make_exclamation(sentences)
print(result)
