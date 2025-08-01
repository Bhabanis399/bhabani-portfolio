from flask_mail import Mail, Message
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

# Email configuration (using Gmail example)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'bhabanis399@gmail.com'        # Replace with your email
app.config['MAIL_PASSWORD'] = 'pxwy orup lncb nhdl'      # Use Gmail App Password, not your real password

mail = Mail(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/skills')
def skills():
    return render_template("skills.html")

@app.route('/certificates')
def certificates():
    return render_template("certificates.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message(subject=f"New Contact from {name}",
                      sender=email,
                      recipients=['bhabanis399@gmail.com'],  # Your email to receive messages
                      body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}")

        try:
            mail.send(msg)
            flash('Message sent successfully!', 'success')
        except Exception as e:
            flash('Something went wrong. Message not sent.', 'danger')
            print(e)

        return redirect('/contact')

    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
