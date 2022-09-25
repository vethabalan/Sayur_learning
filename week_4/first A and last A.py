#print the words between "a"
word = input("enter the word: ")
length = len(word)
for first_word in range (0, length):
    for second_word in range(first_word + 1 , length):
        if((word[first_word] == word[second_word])):
            first_a = first_word
            second_a = second_word
            break
    break       
print(word[first_a + 1 : second_a])


"""
TEST CASE : 1
enter the word: abcdefa
bcdef
"""