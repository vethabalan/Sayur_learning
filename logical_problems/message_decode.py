from num2words import num2words
#message as input
message = input("message : ")
#assign a variable as vowels and store it as a string
vowels = ["a","e","i","o","u","A","E","I","O","U"]
#assign a empty string to store the output
decoded_message = " "
numbers = " "
#to check the message is all are aplhabets
verify_message = message.isalpha()
#if true this statement executes
if(verify_message == True):
    #if the word ends with the vowel split the last letter and reverse the other letters
    if(message[-1] in vowels):
        decoded_message += message[-1]
        #to reverse the letters
        for reverse in range(0,len(message)-1):
            #to store the reversed word in output
            decoded_message += message[reverse]
        print(decoded_message)
    else:
        half_split_word = len(message)//2
        if(len(message) % 2 == 0):
            for reverse in range(half_split_word , len(message)):
                decoded_message += message[reverse]
                for forward in range(0,half_split_word):
                    decoded_message += message[forward]
            print(decoded_message)
        else:
            for reverse in range(half_split_word + 1 , len(message)):
                decoded_message += message[reverse]
                decoded_message += message[half_split_word]
        print("the decoded message is : ",decoded_message)
else:
    message=message.split()
    for num in range(0,len(message)):
        numeric_message = message[num].isnumeric()
        if(numeric_message == True):
            decoded_message += "A"
            decoded_message += (num2words(message[num]))
            decoded_message += "A"
        else:
            decoded_message = message[num]
    print(*decoded_message)