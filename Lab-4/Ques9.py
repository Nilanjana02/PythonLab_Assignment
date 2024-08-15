# 9.Write a program that accepts a string
# I. 1.reverses it.
# II. 2.checks whether it is a palindrome.
# III. 3.checks whether it ends with a specific substring.
# IV. 4.capitalize the first letter of each word in a string
# V. 5.check if a string is anagram of another string
# VI. 6.remove vowels from string
# VII. 7.find length of the longest word in a sentence
# I
string = input("Enter a string: ")
print("Reversed string is: ", string[::-1])
# II
if string == string[::-1]:
    print("String is a palindrome")
else:
    print("String is not a palindrome")
# III
substring = input("Enter a substring: ")
if string.endswith(substring):
    print("String ends with the specific substring")
else:
    print("String does not end with the specific substring")
# IV
words = string.split()
capitalized_words = []
for word in words:
    capitalized_words.append(word.capitalize())
capitalized_string = " ".join(capitalized_words)
print("String with first letter of each word capitalized: ", capitalized_string)
# V
string1 = input("Enter a string: ")
string2 = input("Enter another string: ")
if sorted(string1) == sorted(string2):
    print("String is an anagram of another string")
else:
    print("String is not an anagram of another string")
# VI
vowels = "aeiouAEIOU"
vowels_removed_string = ""
for char in string:
    if char not in vowels:
        vowels_removed_string += char
print("String after removing vowels: ", vowels_removed_string)
# VII
words = string.split()
longest_word_length = 0
for word in words:
    if len(word) > longest_word_length:
        longest_word_length = len(word)
print("Length of the longest word in the sentence is: ", longest_word_length, end="")
