

# TelGP-Senders-ID

A Python project to save usernames or numeric IDs of message senders in a specific Telegram group. This tool processes all messages in a group (from the most recent to the first) and stores the sender information in a `.txt` file. It is designed to handle both public and private groups efficiently.

---

## **Features**
- Logs into Telegram using the [Telethon](https://docs.telethon.dev) library.
- Accepts group information as input (group link, name, or numeric ID).
- Processes all messages in the group.
- Saves:
  - **Usernames** (if available) with `@` prefix.
  - **Numeric IDs** as clickable links (e.g., `https://t.me/123456789`).
- Saves data in a `.txt` file named after the group (special characters are removed from the group name).

---

## **Requirements**
- Python 3.8+
- A Telegram account, API ID and API HASH (from [my.telegram.org](https://my.telegram.org/apps))

---

## **Getting Started**

### **1. Clone the Repository**
```bash
git clone https://github.com/ItsOrv/TelGP-Senders-ID.git
cd TelGP-Senders-ID
```

### **2. Set Up a Virtual Environment**
Create and activate a virtual environment for the project:
```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### **3. Install Dependencies**
Install the required Python libraries from `requirements.txt`:
```bash
pip install -r requirements.txt
```

### **4. Configure Credentials**
Create `.env` file:
```bash
nano .env
```

Add your credentials:
```
API_ID = "YOUR_API_ID"       # Replace with your API ID
API_HASH = "YOUR_API_HASH"   # Replace with your API HASH
SESSION_NAME = "telegram_user_saver"
LOG_FILE = "app.log"
```

### **5. Run the Project**
Execute the main script to start the program:
```bash
python main.py
```

---

## **Usage**
1. When logged in to Telegram account , provide the **link, name, or numeric ID** of the target Telegram group.
2. The script will:
   - Connect to the group.
   - Process messages one by one (from the latest to the earliest).
   - Save user information in a `.txt` file named after the group.

### **Output**
- The `.txt` file will be created in the project directory.
- Example output for a group named `Test Group`:
  ```
  @username1
  https://t.me/123456789
  @username2
  https://t.me/987654321
  ```

## **Logs**
Logs are stored in `app.log` by default. You can check logs for:
- Login status
- Errors while processing groups or files

---

## **Future Enhancements**
Here are some potential improvements for this project:
- Add a GUI using libraries like Tkinter or PyQt.
- Save additional user details (e.g., profile picture, bio).
- Integrate with a database for better data management.
- Process multiple groups in one run.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
