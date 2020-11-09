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
    ideo_dict = jobs_dict['Ideo']
    ideo_message = '\nCurrent open Ideo positions:\n\n'
    compiled_message = intro_message + ideo_message
    for i in jobs_dict['Ideo']:
        job_info = ideo_dict.get(i)
        compiled_message = compiled_message + 'Position: ' + job_info[0] + ' -' + '\n'
        compiled_message = compiled_message + 'Location: ' + job_info[1] + '\n'
        compiled_message = compiled_message + 'Link: ' + job_info[2] + '\n\n'

    frog_dict = jobs_dict['Frog']
    frog_message = '\nCurrent open Frog positions:\n\n'
    compiled_message = compiled_message + frog_message
    for f in jobs_dict['Frog']:
        job_info = frog_dict.get(f)
        compiled_message = compiled_message + 'Position: ' + job_info[0] + ' -' + '\n'
        compiled_message = compiled_message + 'Location: ' + job_info[1] + '\n'
        compiled_message = compiled_message + 'Link: ' + job_info[2] + '\n\n'

    ammo_dict = jobs_dict['Ammo']
    ammo_message = '\nCurrent open Ammo positions:\n'
    compiled_message = compiled_message + ammo_message
    for a in jobs_dict['Ammo']:
        job_info = ammo_dict.get(a)
        compiled_message = compiled_message + 'Position: ' + job_info[0] + ' -' + '\n'
        compiled_message = compiled_message + 'Location: ' + job_info[1] + '\n'
        compiled_message = compiled_message + 'Link: ' + job_info[2] + '\n\n'

    compiled_message = compiled_message + 'Love from\n\nBob Jot, your web scraping job bot!'

    print('Sending emails')
    formatted_message = MIMEText(compiled_message, "plain")
    message.attach(formatted_message)

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            for i in receiver_email:
                server.sendmail(sender_email, i, message.as_string())
    except smtplib.SMTPAuthenticationError:
        print('Either email or password were incorrect')
        print('Please try logging in again by using the "change_email" and "change_password" in the terminal')
        print('Then use the "test" command to resend the email')

    print('Emails sent!')
