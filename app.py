from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

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
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # Save or print (you can replace this with saving to DB or sending email)
        print(f"New message from {name} ({email}): {message}")

        flash("Thanks for contacting me! I'll get back to you soon.")
        return redirect(url_for('contact'))

    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
