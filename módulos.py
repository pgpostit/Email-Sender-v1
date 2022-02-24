from email_validator import validate_email, EmailNotValidError
import sys

def credentials():
    email_from = input('Tell who you are: ')
    if email_from == 'stop404**':
        sys.exit()
    while True:
        try:
            email_to = input('For who is this email? ')
            if email_to =='stop404**':
                sys.exit()
            valid = validate_email(email_to)
            email_to = valid.email
            break
        except EmailNotValidError as e:
            print(str(e))
    email_subject = input('Describe the subject: ')
    cred = [email_from, email_to, email_subject]
    return cred

def email_body():
    print('The email body: ')
    body=[]
    while True:
        n = input()
        if len(n) == 0:
            break
        body.append(n)
    text='\n'.join(body)
    return text

def layout():
    print('='*30)
    titulo = "EMAIL SENDER"
    print(f'{titulo:^30}')
    print('='*30)

