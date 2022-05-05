import pyperclip,sys

# pyperclip.copy("Hello Python")
# pyperclip.paste()

# PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
# 'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
# 'luggage': '12345'}

#print(PASSWORDS)
pass_word={'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
'luggage': '12345'}

if len(sys.argv) < 2:
    print('USAGE Copy Account')
    sys.exit()
    account=sys.argv(1)
    print(pass_word)
    if account in pass_word:
        pyperclip.copy(pass_word[account])
        print("copied")

