# **************************************************
#                   palindromes                    #
# **************************************************

def palindromes(word):
    palin_word = word
    reverse = word[::-1]
    if palin_word == reverse:
        return "{} is a palindrome.".format(palin_word)
    else:
        return "{} is not a palindrome.".format(palin_word)


result = palindromes("isi")
print(result)


# palindrome sentence
def palindrome_sentence(sentence):
    sentence = sentence[:]
    backwards = "".join(i for i in sentence if i.isalpha() or i.isalnum())[::-1]
    sentence_ = "".join(i for i in sentence if i.isalpha() or i.isalnum())
    if backwards.casefold() == sentence_.casefold():
        return "{} is a palindrome".format(sentence)
    else:
        return "{} is not a palindrome".format(sentence)


# some examples of palindromes
result_sentence1 = palindrome_sentence("Was it a car or a cat I saw?")
print(result_sentence1)
result_sentence2 = palindrome_sentence("Live on time, emit no evil")
print(result_sentence2)
result_sentence3 = palindrome_sentence("Rats live on no evil star")
print(result_sentence3)
result_sentence4 = palindrome_sentence("Mr. Owl ate my metal worm")
print(result_sentence4)
result_sentence5 = palindrome_sentence("Do geese see God?")
print(result_sentence5)
result_sentence6 = palindrome_sentence("Step on no pets")
print(result_sentence6)
result_sentence7 = palindrome_sentence("Radar")
print(result_sentence7)
