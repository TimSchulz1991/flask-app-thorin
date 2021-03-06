import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env
# this is related to the secret key we need to flash the message


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)
# We read the data from the json file in the json-data variable and save it
# to the data list


@app.route("/about/<member_name>")
# member_name comes from line 25 in about.html
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)
# so in the member file I have access to the member object 
# which contain the data for the particular member that was clicked on


@app.route("/contact", methods=["GET","POST"])
# in order to send the form we need the methods parameter with GET & POST
def contact():
    if request.method == "POST":
        flash(f"Thanks {request.form['name']}, we have received your message!")
        # here we use the imported flash method, but also note
        # the code block inserted into the contact.html page
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
# Debug should be set to false when it is in a production
# environment (meaning when handing a project on)
