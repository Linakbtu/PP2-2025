def is_palindrome(s):
    s = ''.join(s.lower().split())  


user_input = input("Enter a word or phrase: ")
if is_palindrome(user_input):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
