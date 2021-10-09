import yagmail

def registration_email(receiver, subj, body):

    yag = yagmail.SMTP("cbc.testing.email", "EmailTest21")
    yag.send(
        to=receiver,
        subject=subj,
        contents=[body]
    )
    
def email_blast(receivers, subj, body):
    yag = yagmail.SMTP("cbc.testing.email", "EmailTest21")
    
    for receiver in receivers:
        yag.send(
            to=receiver,
            subject=subj,
            contents=[body]
        )
    
def main():
    receiver = "email1"
    receivers_email_blast = [email1, email2]
    body = "Thank you for creating your account with Lousiana Green Corps!"
    subject = "Successful Registration!"
    
    # sending to one person
    # sending_email(receiver, subject, body)
    
    # sending to a group of people
    # email_blast(receivers_email_blast, subject, body)
     
if __name__ == "__main__":
    main()
