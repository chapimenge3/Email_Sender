# Email_Sender
Email_Sender is Python Package For Sending Email Easily. This package is trying to help programmer save time adjusting code for sending email.

## Installation 
you should have [python 3](https://www.python.org/download/releases/3.0/)
```shell
$ pip3 install email_sender
```

## Usage 
email_sender have one base class [**Mail**](https://github.com/chapimenge3/Email_Sender/blob/282a0a499b9940db071e1a9beb33d2b375d2ea70/email_sender/mail.py#L6) that used to send email using smtp connection. 

[**Mail**](https://github.com/chapimenge3/Email_Sender/blob/282a0a499b9940db071e1a9beb33d2b375d2ea70/email_sender/mail.py#L6) 
   > **Parameters**
   - **email** - Required 
           - Email of sender. once you initiate it, it can be used for sending emails
   - **password** - Required if envPath is None
              - Password is required if you don't specify the `.env` path 
              - in Most case programmer don't wanna put password as string inside their code for that email_sender module use [dotenv](https://github.com/pedroburon/dotenv). 
   - host - default to 'smtp.gmail.com'
   - port - default to 587
   - **envPath** - optional 
             - envPath expect `python pathlib.Path('.env file location').resolve()`
   - envName - optional default to `password` 
             - envName if the name of the password in the `.env` is another name.


## Example
```python
from email_sender.mail import Mail
from pathlib import Path
senderEmail = 'sender@gmail.com
receiverEmail = 'receiverEmail@gmail.com'
mail = Mail(senderEmail, envPath=Path('.env'), envName='cha')

message = '''\
Subject: Testing Emails 
This is testing email message 
'''
mail.send_email(receiverEmail, message)
```
### Clone
if you want to clone and use the repo use the **requirement.txt** file

```shel
pip3 install -r requirements.txt 
```

### About Developer 
My Name is Temking Mengistu . I am Student at [Adama Science and Technology University](http://www.astu.edu.et/) in field of Computer Science and Engineering. 
**Follow me on** 
   - [Github](https://github.com/chapimenge3)
   - [Linkedin](https://www.linkedin.com/in/chapi-menge/)


### ©chapimenge 2020