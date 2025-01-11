# File: postmark_email_sender.py

import requests
from dotenv import load_dotenv
import os

#load environment variables
load_dotenv()

# Postmark API URL
POSTMARK_API_URL = os.getenv("POSTMARK_API_URL")

# Your Postmark server token
POSTMARK_SERVER_TOKEN = os.getenv("POSTMARK_SERVER_TOKEN")

def send_email(from_address, to_address, subject, html_body, message_stream="outbound"):
    """
    Sends an email using the Postmark API.

    Args:
        from_address (str): Sender email address.
        to_address (str): Recipient email address.
        subject (str): Email subject line.
        html_body (str): HTML content of the email.
        message_stream (str): The message stream to use (default: 'outbound').

    Returns:
        dict: API response data.
    """
    # Headers for the request
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-Postmark-Server-Token": POSTMARK_SERVER_TOKEN,
    }

    # Email data
    data = {
        "From": from_address,
        "To": to_address,
        "Subject": subject,
        "HtmlBody": html_body,
        "MessageStream": message_stream,
    }

    # Sending the request
    try:
        response = requests.post(POSTMARK_API_URL, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for bad HTTP responses
        print("Email sent successfully!")
        return response.json()  # Return the API response data
    except requests.exceptions.RequestException as e:
        print(f"Error sending email: {e}")
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    from_address = "naoresponder@gruposkip.com"
    to_address = "eduardo.lemosinc@gmail.com"
    subject = "Racha Conta"
    html_body = "<strong>Hello Sócios</strong> Mensageria is being born 2"

    # Send email
    response = send_email(from_address, to_address, subject, html_body)
    print(response)
