import random

def set_options():
    # prompts the user to select what chars should be included in the password.
    # returns booleans 
    num_chars = int(input("How long should the password be? "))
    num = str_to_bool(input("Should it use numbers? "))
    upper = str_to_bool(input("Should it use UPPERCASE letters? "))
    lower = str_to_bool(input("Should it use lowercase letters? "))
    symbols = str_to_bool(input("Should it use symbols? (!@#$%^&&*(/?) "))
    return num, upper, lower, symbols, num_chars


def str_to_bool(s):
    true_words = ['yes','Yes','YES','true','True','TRUE','yeah','yea','ye']
    if s in true_words:
        return True
    else:
        return False


def gen_chars(num,upper,lower,symbols):
    # accepts booleans saying whether integers, uppercase letters, lowercase letters,
    # and special characters should be included in the password.
    #chr() pulls ascii values
    chars = []
    if num:
        nums = [chr(x) for x in range(48,58)]
        chars = chars + nums
    
    if upper:
        uppers = [chr(x) for x in range(65,91)]
        chars = chars + uppers

    if lower:
        lowers = [chr(x) for x in range(97,123)]
        chars = chars + lowers

    if symbols:
        symb = [chr(x) for x in range(33,48)]
        symb = symb + [chr(x) for x in range(58,65)]
        symb = symb + [chr(x) for x in range(91,97)]
        symb = symb + [chr(x) for x in range(123,127)]
        chars + symb
    
    return chars


def gen_password(chars, num_chars):
    # accepts a set of characters and the number to be randomly chosen,
    # returns a new password string.
    password = ""
    while len(password) < num_chars:
        idx = random.randint(0,len(chars) - 1)
        password = password + chars[idx]
    return password


def main():
    num, upper, lower, symbols, num_chars = set_options()
    chars = gen_chars(num,upper,lower,symbols)
    password = gen_password(chars, num_chars)
    print("Your Password is " + password)

if __name__ == '__main__':
    main()