from flask import Flask, render_template, request, url_for
from flask_mail import Mail, Message
from flask_recaptcha import ReCaptcha

from flask import flash


app = Flask(__name__)

recaptcha = ReCaptcha(app=app)

app.config.update(dict(
    RECAPTCHA_ENABLED = True,
    RECAPTCHA_SITE_KEY = "",
    RECAPTCHA_SECRET_KEY = "",
))
 
recaptcha = ReCaptcha()
recaptcha.init_app(app)

app.secret_key = ""

#app.config["SECRET_KEY"] = ""
app.config["MAIL_SERVER"] = ""
app.config["MAIL_PORT"] = 
app.config["MAIL_USERNAME"] = ""
app.config["MAIL_PASSWORD"] = ""
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
mail = Mail(app)

@app.route("/", methods=["GET", "POST"])
@app.route("/index.html", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        if recaptcha.verify():
            msg = Message(sender="", recipients=[""])
            message = request.form.get("messageBody")
            name = request.form.get("senderName")
            email = request.form.get("senderMail")
            msg.body = "Name: {},\nEmail: {},\nMessage: {}".format(name, email, message)
            msg.subject = name
            mail.send(msg)
            flash("Message sent.") 
            return render_template("/index.html", scrollToAnchor="visualC")
            #return render_template("/success.html")
        else:
            flash('Error ReCaptcha')
            #return render_template("/failed.html")

    return render_template("/index.html")


if __name__ == "__main__":
    #app.run(debug=True)
    app.run()

