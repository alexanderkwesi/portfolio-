import smtplib
from email.message import EmailMessage
from flask import Flask, render_template, request, flash, session


app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = "Alexander Oluwaseun Kwesi"

@app.route('/')
def index():
    return render_template('portfolio.html')

@app.route('/mail_post', methods=['POST'])
def mail_post():
    
    if request.method == 'POST':
        name = request.form.get('fullname')
        email = request.form.get('email')
        message = request.form.get('message')
        subject = request.form.get('subject')
        msg = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        messages = EmailMessage()
        server.login('seankwesi24@googlemail.com', 'rlxj hrxj ymep bxjr')
        messages['From'] = 'seankwesi24@googlemail.com'
        messages['To'] = 'seankwesi24@googlemail.com'
        messages['Subject'] = subject
        messages.set_content(msg)
        server.send_message(messages)
        server.quit()
        flash("Thank you for submitting your message.")
    return render_template('portfolio.html')