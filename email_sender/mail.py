from smtplib import SMTP
import ssl
from pathlib import Path


class Mail:
    """
    Base class for sending email.
    Parameters 
        email - required
        password - optional(but envPath must be given)
        host - default
        port - default
        envPath - optional(if password is None it is required)
        envName - name of the key found in .env file for storing the password of the email 
    """

    def __init__(self, email, password=None, host='smtp.gmail.com', port=587, envPath=None, envName='password'):
        if password is None and envPath is None:
            raise Exception(
                "You can't leave both password and envPath None , one must have value")
        if password is not None and envPath is not None:
            raise Exception(
                "You can't give both password and envPath value , only one must have value")
        elif password is not None:
            self.password = password
        else:
            '''
            Configuring .env file
            import inside the else because if the use don't want to use .env they don't have to install dot env  
            '''
            # importing dot env
            from dotenv import load_dotenv
            # register the .env file path to load_dotenv
            load_dotenv(dotenv_path=envPath)

            # Nowthe .env file is accessible through os module in environ dictionary
            import os
            # now we can access through envName name in the os.environ
            self.password = os.environ.get(envName)

            # if the password is None means user either misspell envName or there dont set it in .env file
            if self.password is None:
                raise Exception(
                    "Password can't be None , check your envName in .env file")
        # set email
        self.email = email 
        
        # create secure connection
        context = ssl.create_default_context()
        try:
            pass
        # start the SMTP server using host and port
            self.server = SMTP(host=host, port=port)
            
            self.server.ehlo()
            self.server.starttls(context=context)  # secure the connection
            self.server.ehlo()
            
            self.server.login(self.email, self.password)
            # print('Successfully logged in')
        except Exception as exception:
            # print('unsuccessfull login trial')
            print(exception)
        

    def send_email(self, receiverEmail, message):
        '''
        it uses self.email as email 
        send email message to the receiverEmail
        '''
        emailResponse = self.server.sendmail(self.email, receiverEmail, message)
        return emailResponse
        
    def __del__(self):
        '''
        Destructor , to close the server
        '''
        self.server.quit()
        print("Good bye...")
