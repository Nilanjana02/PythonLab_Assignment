# Write a program to enter a string. Calculate the length of the string. Find the substring country.Count the occurences of each word in the given sentence.If the String as input is India is my motherland. I love my country. Capital of India is New Delhi.
string = input("Enter a string: ")
print("Length of the string is: ", len(string))
substring = "country"
print("Substring is: ", substring)
words = string.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print("Occurences of each word in the given string is: ", word_count)
