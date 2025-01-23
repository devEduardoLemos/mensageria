from fastapi import FastAPI, HTTPException, Header, Depends
from pydantic import BaseModel, EmailStr
from dotenv import load_dotenv
from email_validator import validate_email, EmailNotValidError
import boto3
import os

# Load environment variables
load_dotenv()

# AWS SES Configuration
AWS_REGION = os.getenv("AWS_REGION")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

# API KEY for access to the services
API_KEY = os.getenv("API_KEY")

# Functions
def send_email(from_address, to_address, subject, html_body):
    """
    Sends an email using AWS SES.

    Args:
        from_address (str): Sender email address.
        to_address (str): Comma-separated recipient email addresses.
        subject (str): Email subject line.
        html_body (str): HTML content of the email.

    Returns:
        dict: Response from AWS SES.
    """
    try:
        # Initialize boto3 SES client
        ses_client = boto3.client(
            "ses",
            region_name=AWS_REGION,
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        )

        # Send the email
        response = ses_client.send_email(
            Source=from_address,
            Destination={
                "ToAddresses": to_address.split(","),
            },
            Message={
                "Subject": {"Data": subject},
                "Body": {
                    "Html": {"Data": html_body},
                },
            },
        )
        print("Email sent successfully!")
        return response
    except Exception as e:
        print(f"Error sending email: {e}")
        raise HTTPException(status_code=500, detail=f"Error sending email: {e}")


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


def validate_api_key(x_api_key: str = Header(...)):
    """
    Validates the API key provided in the request header.

    Args:
        x_api_key (str): The API key from the `x-api-key` header.

    Raises:
        HTTPException: If the API key is missing or invalid.
    """
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key",
        )
    return True


# Initialize FastAPI
app = FastAPI()

# Pydantic model
class EmailRequest(BaseModel):
    from_address: EmailStr
    to_address: str
    subject: str
    html_body: str


# FastAPI endpoints
@app.post("/send-email")
async def send_email_endpoint(
    email_request: EmailRequest,
    x_api_key: str = Depends(validate_api_key),
):
    """
    Endpoint to send email
    Protected with API KEY
    """
    try:
        # Validate email
        if validate_email_addresses(email_request.from_address)["is_valid"]:
            from_address = validate_email_addresses(email_request.from_address)["email"]
        else:
            raise HTTPException(
                status_code=422,
                detail=f"Invalid from_address: {email_request.from_address}",
            )

        to_address = ""
        not_sent = ""
        emails = email_request.to_address.split(",")
        for email in emails:
            if validate_email_addresses(email)["is_valid"]:
                to_address = to_address + validate_email_addresses(email)["email"] + ","
            else:
                not_sent = not_sent + validate_email_addresses(email)["email"] + ","

        response = send_email(
            from_address,
            to_address.strip(","),
            email_request.subject,
            email_request.html_body,
        )

        return {
            "response": response,
            "bad_addresses": f"This addresses could not be reached: {not_sent.strip(',')}",
        }
    except HTTPException as e:
        raise e
