import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
intro_message = 'This is your weekly update of available job positions in your favourite design companies.\n\n'

message = MIMEMultipart("alternative")
message["Subject"] = "Job Roles Update"


def send_email(jobs_dict, sender_email, receiver_email, password):
    print('Compiling email')
    ideo_message = '\nCurrent open Ideo positions:\n'
    compiled_message = intro_message + ideo_message
    for i in jobs_dict['Ideo']:
        compiled_message = compiled_message + '-' + i + '\n'

    frog_message = '\nCurrent open Frog positions:\n'
    compiled_message = compiled_message + frog_message
    for f in jobs_dict['Frog']:
        compiled_message = compiled_message + '-' + f + '\n'

    ammo_message = '\nCurrent open Ammo positions:\n'
    compiled_message = compiled_message + ammo_message
    for a in jobs_dict['Ammo']:
        compiled_message = compiled_message + '-' + a + '\n'

    print('Sending emails')
    formatted_message = MIMEText(compiled_message, "plain")
    message.attach(formatted_message)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        for i in receiver_email:
            server.sendmail(sender_email, i, message.as_string())
    print('Emails sent!')
