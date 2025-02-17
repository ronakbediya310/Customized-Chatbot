# Django Chatbot with AI-Powered Responses

## Overview
This project is an AI-powered chatbot built using **Django**. It allows users to engage in real-time conversations with an AI assistant that provides solutions, explanations, and debugging assistance for coding-related queries. The chatbot supports **text-based interactions**, **chat history storage**, and **quick actions** to streamline the experience.

## Features
✅ **User Authentication** (Login/Logout)
✅ **Real-time Chat Interface**
✅ **Chat History Management**
✅ **Quick Action Buttons** (Explain, Debug, Optimize, Convert, Generate Code)
✅ **AJAX-Based Messaging** for Seamless Interaction
✅ **CSRF Protection & Security Measures**

## Tech Stack
- **Backend:** Django, Django REST Framework (DRF)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (Default) / MySQL (for production)
- **APIs:** Groq API (for AI-generated responses)
- **AJAX & JavaScript Fetch API** for Asynchronous Requests

## Installation Guide
### 1️⃣ Clone the Repository
```bash
$ git clone https://github.com/yourusername/django-chatbot.git
$ cd django-chatbot
```

### 2️⃣ Create & Activate a Virtual Environment
```bash
$ python -m venv venv
$ source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
$ pip install -r requirements.txt
```

### 4️⃣ Apply Migrations
```bash
$ python manage.py migrate
```

### 5️⃣ Create a Superuser (For Admin Panel)
```bash
$ python manage.py createsuperuser
```

### 6️⃣ Run the Development Server
```bash
$ python manage.py runserver
```

Now, open your browser and navigate to:
```
http://127.0.0.1:8000/users/login
```

## Usage
- **Login or Register** to access the chatbot.
- Type your query in the text box and hit send.
- Use **quick actions** for faster code-related responses.
- View and manage chat history.
- Logout securely when done.

## File Structure

📂 project_root/
│── 📂 chatbot/
│   │── 📂 static/
│   │── 📂 templates/
│   │   ├── 📄 chat.html
│   │   ├── 📄 history.html
│   │   └── 📄 welcome.html
│   │── 📄 __init__.py
│   │── 📄 admin.py
│   │── 📄 apps.py
│   │── 📄 models.py
│   │── 📄 prompt.py
│   │── 📄 tests.py
│   │── 📄 urls.py
│   └── 📄 views.py
│── 📂 code_assistant/
│   │── 📄 __init__.py
│   │── 📄 asgi.py
│   │── 📄 settings.py
│   │── 📄 urls.py
│   └── 📄 wsgi.py
│── 📂 templates/
│── 📂 users/
│── 📄 .gitignore
│── 📄 manage.py
│── 📄 README.md
└── 📄 requirements.txt


## Customization
- Modify **styles** in `static/chatbot/styles.css`.
- Change chatbot **response logic** in `views.py`.

## Deployment Guide
For deploying to **Heroku**, **AWS**, or **VPS**, follow these steps:
1. **Set up a production database (PostgreSQL)**
2. **Configure `ALLOWED_HOSTS` in settings.py**
3. **Use Gunicorn for WSGI server**
4. **Enable Static Files Handling**



## Contributing
We welcome contributions! Please follow these steps:
1. Fork the repository
2. Create a feature branch (`feature/new-feature`)
3. Commit changes (`git commit -m "Added new feature"`)
4. Push and create a Pull Request

## License
This project is licensed under the **MIT License**.

---

🚀 **Developed with ❤️ by [Ronak Bediya]**

