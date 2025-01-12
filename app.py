from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, EmailStr
from dotenv import load_dotenv
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


#Initialize FastAPI
app = FastAPI();

#Pydantic model
class EmailRequest(BaseModel):
    from_adress: str
    to_address: str
    subject: str
    html_body: str


#FastAPI endpoints
@app.post("/send-email")
async def send_email_endpoint(request: Request):
    """
    Endpoint to send email
    """
    try:
        #get the JSON payload
        email_request = await request.json()

        response = send_email(
            email_request.get("from_address"),
            email_request.get("to_address"),
            email_request.get("subject"),
            email_request.get("html_body"),
        )
        
        return{"response": response}
    except HTTPException as e:
        raise e


