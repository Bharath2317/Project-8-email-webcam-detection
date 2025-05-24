import smtplib
from email.message import EmailMessage
from PIL import Image
import mimetypes

PASSWORD = "hkzcqnnnbbxgsqgh"
SENDER = "bharathh1817@gmail.com"
RECEIVER = "bharathh1817@gmail.com"

def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "You got a new customer!"
    email_message.set_content("Hey! The customer has just arrived")

    with open(image_path , "rb") as file:
        content = file.read()

    with Image.open(image_path) as img:
        image_format = img.format.lower()
    email_message.add_attachment(content,maintype = "image",subtype= image_format)

    gmail = smtplib.SMTP("smtp.gmail.com",587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER,PASSWORD)
    gmail.sendmail(SENDER,RECEIVER,email_message.as_string())
    gmail.quit()


if __name__ == "__main__":
    send_email("images/255.png")


    
    