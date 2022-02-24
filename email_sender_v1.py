#Importing
import smtplib                                #access e-mails
from email.message import EmailMessage        #Build a variable as an e-mail
from string import Template                   #template to html form
from pathlib import Path                      #Object-oriented filesystem paths
from módulos import layout, credentials, email_body


#Variables
html = Template(Path('index.html').read_text()) #variable to link index.html on the python file
email = EmailMessage()                          #variable to receive the e-mail built structure

#Functions                                      #please enter "stop404**" to stop. Doesn't work on 'subject' field.
layout()
cred=credentials()


#Email credentials
email['from'] = cred[0]               #Your personal or company name
email['to'] = cred[1]            #For who you're sending the e-mail
email['subject'] = cred[2]  #The subject of the e-mail
fbody = email_body()


#Here you can declare any word at index.html as a variable. You can give a value too.
email.set_content(html.substitute({'name' : name, 'body': fbody}), 'html')

#App main function
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('your_email@email.com', 'password')
    smtp.send_message(email)
    print('e-mail enviado.')