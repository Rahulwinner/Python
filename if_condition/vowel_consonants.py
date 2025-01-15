try:
    user_input = input("Enter the single character (a-z)...")
    if user_input=="a" or user_input=="e" or user_input=="i" or user_input=="o" or user_input=="u":
        print("this is vowel")
    elif user_input=="A" or user_input=="E" or user_input=="I" or user_input=="O" or user_input=="U":
        print("this is vowel")
    else:
        print("this is consonants")
except:
    print("Enter the valid credential...")