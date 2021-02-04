import random

class password:

    nums = [chr(x) for x in range(48,58)]
    uppers = [chr(x) for x in range(65,91)]
    lowers = [chr(x) for x in range(97,123)]
    symbs = (
        [chr(x) for x in range(33,48)] 
        + [chr(x) for x in range(33,48)]
        + [chr(x) for x in range(91,97)]
        + [chr(x) for x in range(123,127)]
    )


    def __init__(self, pass_len, num_yn, upper_yn, lower_yn, symbols_yn):
        self.pass_len = pass_len
        self.num_yn = num_yn
        self.upper_yn = upper_yn
        self.lower_yn = lower_yn
        self.symbols_yn = symbols_yn

        self.password = self.generate_password()


    def generate_password(self):
        chars = self.get_chars()
        password = []
        while len(password) < self.pass_len:
            idx = random.randint(0,len(chars) - 1)
            password.append(chars[idx])
        password = self.check_char_inclusion(password)
        str_password = ''
        str_password = str_password.join(password)
        return str_password


    def get_chars(self):
        chars = []
        if self.num_yn:
            chars = chars + self.nums
        if self.upper_yn:
            chars = chars + self.uppers
        if self.lower_yn:
            chars = chars + self.lowers
        if self.symbols_yn:
            chars = chars + self.symbs
        return chars


    def check_char_inclusion(self,password):
        nums_bool = False
        upper_bool = False
        lower_bool = False
        symb_bool = False

        for ch in password:
            if ch in self.nums:
                nums_bool = True
            elif ch in self.uppers:
                upper_bool = True
            elif ch in self.lowers:
                lower_bool = True
            elif ch in self.symbs:
                symb_bool = True
            else:
                continue
        
        if not nums_bool:
            idx = random.randint(0,len(chars) - 1)
            num_idx = idx = random.randint(0,len(self.nums) - 1)
            password[idx] = self.nums[idx]
        if not upper_bool:
            idx = random.randint(0,len(chars) - 1)
            upper_idx = idx = random.randint(0,len(self.uppers) - 1)
            password[idx] = self.uppers[idx]
        if not lower_bool:
            idx = random.randint(0,len(chars) - 1)
            lower_idx = idx = random.randint(0,len(self.lowers) - 1)
            password[idx] = self.lowers[idx]
        if not symb_bool:
            idx = random.randint(0,len(chars) - 1)
            symb_idx = idx = random.randint(0,len(self.symb) - 1)
            password[idx] = self.symbs[idx]
        
        if nums_bool and upper_bool and lower_bool and symb_bool:
            return password
        else:
            check_char_inclusion(password)


