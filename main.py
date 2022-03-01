from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)


blog_url = "https://api.npoint.io/3641e44b2cc6f1fa14e6"
blog_posts = requests.get(blog_url).json()

my_email = ""
password = ""


@app.route("/")
def home():
    return render_template("index.html", posts=blog_posts)



@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html", msg_sent=False)
    else:
        name = request.form['name']
        email = request.form['email']

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            result = connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="coreyaugburn7@gmail.com",
                                msg=f"{name}  {email}")
        # send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)


# def send_email(name, email, phone, message):
#     email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(OWN_EMAIL, OWN_PASSWORD)
#         connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)

@app.route("/post/<int:blog_id>")
def post(blog_id):
    return render_template("post.html", id=blog_id, posts=blog_posts)


@app.route("/form-entry")
def receive_data():
    name = request.form['name']
    email = request.form['email']
    print(name)
    print(email)
    return render_template("form-entry.html")




if __name__ == "__main__":
    app.run(debug=True)






