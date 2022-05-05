import re
import pyperclip
pass_length_ck=re.compile(r'.{8,}')
pass_upper_ck=re.compile(r'[A-Z]')
pass_lower_ck=re.compile(r'[a-z]')
pass_number_ck=re.compile(r'[0-9]')

def pass_strength_ck(text):
    print("Start")
    if pass_length_ck.search(text) is None:
        print("Start-1")
        print('String Test')
        return False
    if pass_upper_ck.search(text) is None:
        print("Start-2")
        return False
    if pass_lower_ck.search(text) is None:
        print("Start-3")
        return False
    if pass_number_ck.search(text) is None:
        print("Start-4")
        return False
    else:
        print("Start-5")
        return True
    password=pyperclip.copy("FFFFFFayaz123")
    print("Start-6")
    str(pyperclip.paste())
    print("Start-7")
    if pass_strength_ck(password) is True:
        print("Its Strong Password")
    else:
        print("Thats Weak Password")
password="Fayaz123"
print(pass_strength_ck(password))