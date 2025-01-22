# **Mensageria API**

Mensageria is a FastAPI-based application for sending emails via the [Postmark API](https://postmarkapp.com). The application includes features such as email validation and API key-based security to ensure secure and reliable email delivery.

---

## **Features**
- Send HTML-formatted emails to multiple recipients.
- Validate email addresses using the `email-validator` library.
- Secure the API with an API key for access control.
- Return detailed responses with valid and invalid email addresses.

---

## **Requirements**
- Python 3.7 or later
- Dependencies listed in `requirements.txt`

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
POSTMARK_API_URL=https://api.postmarkapp.com/email
POSTMARK_SERVER_TOKEN=your-postmark-server-token
API_KEY=your-secure-api-key
```

Replace `your-postmark-server-token` and `your-secure-api-key` with your actual Postmark server token and API key.

### **5. Run the Application**
Start the FastAPI server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

---

## **Endpoints**

### **1. POST `/send-email`**
Send an email to one or more recipients.

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
        "To": "recipient1@example.com,recipient2@example.com",
        "SubmittedAt": "2025-01-10T00:00:00.000Z",
        "MessageID": "1234abcd-5678-efgh-9012-ijklmnopqrstu",
        "ErrorCode": 0,
        "Message": "OK"
    },
    "bad_addresses": "This addresses could not be reached: invalid-email@"
}
```

### **2. GET `/test`**
Validate the API key.

#### **Request Headers**
| Header       | Description              |
|--------------|--------------------------|
| `x-api-key`  | The API key for access.  |

#### **Response**
```json
{
    "message": "Valid API key"
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
- `email-validator`: Library for email address validation.
- `python-dotenv`: Manage environment variables.
- `requests`: For HTTP requests to the Postmark API.

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
