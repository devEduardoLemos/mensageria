# **Mensageria**

Mensageria is a lightweight Python application for sending emails using the [Postmark API](https://postmarkapp.com). This project is designed to be simple, modular, and secure, leveraging environment variables to manage sensitive data.

---

## **Features**
- Send HTML-formatted emails.
- Easy configuration with a `.env` file.
- Secure token management using `python-dotenv`.
- Built with extensibility and maintainability in mind.

---

## **Requirements**
- Python 3.7 or later
- Dependencies listed in `requirements.txt`

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-repo/messageria.git
cd messageria
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
POSTMARK_SERVER_TOKEN=your-postmark-server-token
POSTMARK_API_URL=your-postmark-api-url
```

Replace `your-postmark-server-token` and `your-postmark-api-url` with your Postmark info.

### **5. Run the Application**
Execute the script to send an email:
```bash
python app.py
```

---

## **Usage**
### **Email Sending Example**
The script includes an example in the `app.py` file. Update the following variables to customize your email:
- `from_address`: Sender's email address.
- `to_address`: Recipient's email address.
- `subject`: Email subject line.
- `html_body`: HTML content for the email body.

Example snippet:
```python
from_address = "sender@sender.com"
to_address = "recipient@example.com"
subject = "Hello from Messageria"
html_body = "<strong>Hello</strong> dear Postmark user."
```

Run the script to send the email:
```bash
python app.py
```

---

## **Project Structure**
```
messageria/
│
├── .env                      # Environment variables (not included in version control)
├── .gitignore                # Excludes .env and env/ directories
├── env/                      # Virtual environment (ignored by Git)
├── app.py                    # Main email-sending script
├── requirements.txt          # Project dependencies
├── README.md                 # Documentation
```

---

## **Dependencies**
- `requests`: For making HTTP requests.
- `python-dotenv`: For managing environment variables.

Install them using:
```bash
pip install -r requirements.txt
```

---

## **Future Enhancements**
- Add support for plain-text emails and attachments.
- Build a web-based frontend for easier email composition.
- Include logging and advanced error handling.

---

## **Contributing**
Contributions are welcome! Please fork this repository and submit a pull request with your improvements.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## **Support**
If you encounter any issues, feel free to open an issue on the repository or contact us at [suporte@gruposkip.com](mailto:suporte@gruposkip.com).

---

Let me know if you'd like additional customization for this `README.md`.