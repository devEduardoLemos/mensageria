from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from dotenv import load_dotenv
from email_validator import validate_email, EmailNotValidError
import requests
import os

#load environment variables
load_dotenv()

# Postmark API URL
POSTMARK_API_URL = os.getenv("POSTMARK_API_URL")

# Your Postmark server token
POSTMARK_SERVER_TOKEN = os.getenv("POSTMARK_SERVER_TOKEN")


#Functions
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


def validate_email_addresses(email: str) -> dict:
    """
    Validates an email address using the email-validator library.

    Args:
        email (str): The email address to validate.

    Returns:
        dict: A dictionary with the email address and its validation status.
              Example: {"email": "example@example.com", "is_valid": True}
    """
    try:
        validated = validate_email(email)
        return {"email": validated["email"], "is_valid": True}  # Return the normalized email
    except EmailNotValidError:
        return {"email": email, "is_valid": False}  # Return original email with invalid status


#Initialize FastAPI
app = FastAPI();

#Pydantic model
class EmailRequest(BaseModel):
    from_address: EmailStr
    to_address: str
    subject: str
    html_body: str


#FastAPI endpoints
@app.post("/send-email")
async def send_email_endpoint(email_request:EmailRequest):
    """
    Endpoint to send email
    """
    try:
        #validate email
        if(validate_email_addresses(email_request.from_address)["is_valid"]):
            from_address = validate_email_addresses(email_request.from_address)["email"]
        else:
            raise HTTPException(status_code=422,detail=f"Invalid from_address: {email_request.from_address}")
       
        to_address = ''
        not_sent = ''
        emails = email_request.to_address.split(",")
        for email in emails:
            if(validate_email_addresses(email)["is_valid"]):
                to_address = to_address+validate_email_addresses(email)["email"]+","
            else:
                not_sent = not_sent+validate_email_addresses(email)["email"]+","

        response = send_email(
            from_address,
            to_address,
            email_request.subject,
            email_request.html_body,
        )
        
        return {
            "response": response,
            "bad_addresses": f"This addresses could not be reached: {not_sent}"
        }
    except HTTPException as e:
        raise e


