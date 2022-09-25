uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
symbols = "/?.>,<][}{=+-_\|/*-+`~!@#$%^&*()"
password = input("create your password : ")
length = len(password)
minimum_length = 8
if ( len(password) < minimum_length):
    print("password must have atleast 8 characters")
elif ( (uppercase_letters == len(password) ) or (lowercase_letters == len(password)) or ( digits == len(password) ) or ( symbols == len(password)) ):
    print("weak password")
elif ( ( len(uppercase_letters) >= 1 ) and ( len(lowercase_letters) >= 1 ) and ( len(digits) >= 1 ) and ( len(symbols) >= 1 ) ):
    print("ok password")
elif ( ( len(uppercase_letters) >= 3 ) and ( len(lowercase_letters) >= 3 ) and ( len(digits) >= 3 ) and ( len(symbols) >= 3 ) ):
    print("strong password")
print()