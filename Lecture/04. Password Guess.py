CORRECT_PASS = 's3cr3t!P@ssw0rd'
MESSAGE_IF_CORRECT = 'Welcome'
MESSAGE_IF_WRONG = 'Wrong password!'

password_try = input()

if password_try == CORRECT_PASS:
    print(MESSAGE_IF_CORRECT)
else:
    print(MESSAGE_IF_WRONG)
