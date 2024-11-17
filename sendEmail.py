import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, app_password, recipient_email, subject, message):
    try:

        smtp_server = 'smtp.gmail.com'
        smtp_port = 465
        

        server = smtplib.SMTP_SSL(smtp_server, smtp_port)

        server.login(sender_email, app_password)
        

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        

        msg.attach(MIMEText(message, 'plain'))

        server.sendmail(sender_email, recipient_email, msg.as_string())

        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    sender_email = 'sushilkumardora1290@gmail.com'
    app_password = 'bqjdqsxnkicbhdrc'
    recipient_email = 'anishpanda3@gmail.com'
    subject = 'New Nursery Job Requirement'
    message = '''
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

Twinkle, twinkle, little star,
How I wonder what you are!

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Twinkle, twinkle, little star,
How I wonder what you are!

Then the traveler in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

Twinkle, twinkle, little star,
How I wonder what you are!

In the dark blue sky you keep,
And often through my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

Twinkle, twinkle, little star,
How I wonder what you are!

As your bright and tiny spark,
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.

Twinkle, twinkle, little star,
How I wonder what you are!'''
    
    send_email(sender_email, app_password, recipient_email, subject, message)
