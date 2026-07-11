# Flask API Basics

A simple Python Flask application built to demonstrate basic routing and handling `POST` requests. This project is a great starting point for learning how Flask APIs receive and process data. It can be easily tested using API clients such as Postman.

## Features

- Basic Flask API implementation
- Demonstrates multiple API routes
- Handles `POST` requests
- Accepts form data using `x-www-form-urlencoded`
- Easy to test with Postman

## Prerequisites

- Python 3.x
- Flask
- Postman (optional, for API testing)

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository.git
```

### 2. Navigate to the Project Directory

```bash
cd your-repository
```

### 3. Install Flask

```bash
pip install Flask
```

### 4. Run the Application

```bash
python app.py
```

The server will start at:

```
http://127.0.0.1:5000/
```

---

## API Endpoints

| Endpoint | Method | Description | Required Form Data |
|----------|--------|-------------|--------------------|
| `/` | POST | Returns a welcome message | None |
| `/about` | POST | Returns information about the API | None |
| `/contact` | POST | Returns contact information | None |
| `/hello` | POST | Returns a personalized greeting | `name` (x-www-form-urlencoded) |
| `/goodbye` | POST | Returns a farewell message | None |

> **Note:** All routes accept only **POST** requests. Accessing these endpoints directly through a web browser (GET request) will return a **405 Method Not Allowed** error.

---

## Testing with Postman

1. Open **Postman**.
2. Create a new HTTP request.
3. Select the **POST** method.
4. Enter the API URL (e.g., `http://127.0.0.1:5000/hello`).
5. Go to **Body → x-www-form-urlencoded**.
6. Add the following key-value pair:
   - **Key:** `name`
   - **Value:** Your Name
7. Click **Send** to view the response.

---

## Project Structure

```
Flask-API-Basics/
│── app.py
│── README.md
```

---

## Technologies Used

- Python
- Flask
- Postman

---

## Author

**PRATHISH S**
