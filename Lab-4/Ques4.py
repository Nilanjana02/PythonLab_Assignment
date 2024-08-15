# 4. Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically. Suppose the following input is supplied to the program:hello world and practice makes perfect and hello world again Then, the output should be:again and hello makes perfect practice world.
words = input("Enter a sequence of whitespace separated words: ")
words = words.split()
words = list(set(words))    # internally it works like a dictionary, so it removes all duplicate words as for example, if we have "hello" 2 times, it will remove one of them.how ? because in dictionary, we can't have duplicate keys. means if we have same key, it will overwrite the value of that key.what is key here ? key is the word itself. so, if we have same word, it will overwrite the value of that word. so, we will have only one word in the list.
words.sort()
print("Words after removing all duplicate words and sorting them alphanumerically: ", words, end="")
