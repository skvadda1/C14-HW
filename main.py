file = open("words.txt" , "r")
print(file.readline())
file.close()

file = open("words.txt" , "a")
file.write("Learn about words")
file.close()

file = open("words.txt", "w")
file.write("This is the power of words.")
file.close()