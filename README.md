# **Mensageria API**

Mensageria is a FastAPI-based application for sending emails via **AWS Simple Email Service (SES)**. The application includes features such as email validation and API key-based security to ensure secure and reliable email delivery.

---

## **Features**
- Send HTML-formatted emails to multiple recipients using AWS SES.
- Validate email addresses using the `email-validator` library.
- Secure the API with an API key for access control.
- Return detailed responses with valid and invalid email addresses.

---

## **Requirements**
- Python 3.7 or later
- AWS SES configured for your account.
- Dependencies listed in `requirements.txt`

---
## **What's Changed**
1. **Switched Email Provider**: Replaced Postmark API with **AWS SES** for email sending.
   - Emails are now sent using AWS SES's `send_email` method.
   - Requires AWS credentials (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_REGION`).

2. **Updated Environment Variables**:
   - Removed `POSTMARK_API_URL` and `POSTMARK_SERVER_TOKEN`.
   - Added `AWS_REGION`, `AWS_ACCESS_KEY_ID`, and `AWS_SECRET_ACCESS_KEY`.

3. **Enhanced Documentation**: Added details specific to AWS SES usage.

4. **Previous Version**: If you prefer the version using Postmark, you can find it [here](https://github.com/devEduardoLemos/mensageria/tree/createAPI).

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-repo/messageria-api.git
cd messageria-api
```

### **2. Set Up a Virtual Environment**
Create and activate a virtual environment:
```bash
# Create the environment
python -m venv env

# Activate the environment
# On Windows:
.\env\Scripts\activate
# On macOS/Linux:
source env/bin/activate
```

### **3. Install Dependencies**
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### **4. Configure Environment Variables**
Create a `.env` file in the project root and add the following:
```env
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your-aws-access-key-id
AWS_SECRET_ACCESS_KEY=your-aws-secret-access-key
API_KEY=your-secure-api-key
```

Replace the placeholders with your actual AWS credentials and API key.

### **5. Run the Application**
Start the FastAPI server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

---

## **Endpoints**

### **1. POST `/send-email`**
Send an email to one or more recipients using AWS SES.

#### **Request Headers**
| Header       | Description              |
|--------------|--------------------------|
| `x-api-key`  | The API key for access.  |

#### **Request Body**
```json
{
    "from_address": "sender@example.com",
    "to_address": "recipient1@example.com,recipient2@example.com",
    "subject": "Test Email",
    "html_body": "<strong>Hello World!</strong>"
}
```

#### **Response**
```json
{
    "response": {
        "MessageId": "1234abcd-5678-efgh-9012-ijklmnopqrstu",
        "ResponseMetadata": {
            "RequestId": "9c48b123-0b3b-41c1-8a23-123456789abc",
            "HTTPStatusCode": 200
        }
    },
    "bad_addresses": "This addresses could not be reached: invalid-email@"
}
```

---

## **Project Structure**
```
messageria/
│
├── .env                      # Environment variables (ignored by Git)
├── .gitignore                # Excludes unnecessary files
├── env/                      # Virtual environment (ignored by Git)
├── main.py                   # Main application code
├── requirements.txt          # List of dependencies
├── README.md                 # Documentation
```

---

## **Dependencies**
- `FastAPI`: Framework for building APIs.
- `boto3`: AWS SDK for Python to interact with AWS SES.
- `email-validator`: Library for email address validation.
- `python-dotenv`: Manage environment variables.

Install them using:
```bash
pip install -r requirements.txt
```

---

## **Future Enhancements**
- Add logging to track email delivery and errors.
- Implement user authentication using JWT tokens.
- Extend support for email attachments.

---

## **Contributing**
Contributions are welcome! Fork this repository, create a feature branch, and submit a pull request.

---

## **License**
This project is licensed under the MIT License.

---

## **Support**
If you encounter any issues, open an issue on the repository or contact support at [suporte@gruposkip.com](mailto:suporte@gruposkip.com).

