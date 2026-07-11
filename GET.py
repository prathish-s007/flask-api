from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Route 1: Home page
@app.route('/')
def home():
    return "Welcome to the Home Page! This is the main route."

# Route 2: About page
@app.route('/about')
def about():
    return "This is the About Page. We are learning how to use Flask!"

# Route 3: Contact page
@app.route('/contact')
def contact():
    return "Contact us at support@example.com."

# Route 4: A simple greeting
@app.route('/hello')
def hello():
    return "Hello there! I hope you are having a great day."

# Route 5: A farewell message
@app.route('/goodbye')
def goodbye():
    return "Goodbye! Thanks for visiting the app."

# Run the app
if __name__ == '__main__':
    # debug=True allows the server to auto-reload when you make code changes
    app.run(debug=True)
