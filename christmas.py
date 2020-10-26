import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Man:
    def __init__(self, name, mail, drawn):
        self.name = name
        self.mail = mail
        self.drawn = drawn
    
    def __str__(self):
        return "Mail: " + self.mail + "\tName:" + self.name + "\tdrawn: " + self.drawn

def createTest():
    temp_group = []
    temp_group.append(Man("Test1",  "test1.@gmail.com", ""))
    temp_group.append(Man("Test2",  "test2.@gmail.com", ""))
    temp_group.append(Man("Test3",  "test3.@gmail.com", ""))
    return temp_group

def main():
    print("CHRISTMAS PROGRAM 2.1")

    # Create group list
    group = createTest()

    # Shuffle group
    random.shuffle(group)

    # Draw 
    for idx in range(len(group) - 1):
        group[idx].drawn = group[idx + 1].name

    group[len(group) - 1].drawn = group[0].name

    # Debugprint
    """
    for idx in range(len(group)):
        print(group[idx]) #Print for tests only
    """

    # Set sender data
    gmail_user = "sender@gmail.com"   # Email used for sending letters
    gmail_password = "password"
    
    # Set subject
    subject = "This is a test email"
    
    # Send mails
    for idx in range(len(group)) :
        body = "Dear " + group[idx].name + "!\n\n"\
        "You pulled this man from the hat: < " + group[idx].drawn + " >\n\n"\
        "Bye.\n"\

        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = gmail_user
        message['Subject'] = subject
        message['To'] = group[idx].mail

        #The body and the attachments for the mail
        message.attach(MIMEText(body, 'plain'))

        #Create SMTP session
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(gmail_user, gmail_password)
        text = message.as_string()
        session.sendmail(gmail_user,  group[idx].mail, text)
        session.quit()

if __name__ == "__main__":
    main()