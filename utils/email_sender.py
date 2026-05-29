import smtplib

def send_email(order):

    sender = "your_email@gmail.com"
    password = "your_app_password"

    message = f"""
    New Order:
    Area: {order['area']}
    Item: {order['item']}
    Quantity: {order['quantity']}
    """

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)

    server.sendmail(sender, sender, message)
    server.quit()
