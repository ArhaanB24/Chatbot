from flask import Flask,render_template,redirect,request,flash
from instagrapi import Client
import instagrapi

app = Flask(__name__)
app.secret_key = "27"
cl = Client()


@app.route("/",methods=["GET","POST"])
def login():
    user = request.form.get("username")
    password = request.form.get("pass")
    if user and password:
        try:
            cl.login(user,password)
            return redirect("/accounts")
        except instagrapi.exceptions.BadPassword:
            flash("Incorrect Password")
    return render_template("index.html")

@app.route("/accounts",methods=["POST","GET"])
def accounts():
    global acclst
    acclst = []
    num = request.form.get("num")
    if num:
        num = int(num)
        for x in range(num):
            var = request.form.get(f"acc{x}")
            if var:
                acclst.append(var)
    else:
        num = 0
    if acclst:
        return redirect("/text")
    return render_template("accounts.html",num=num,acclst=acclst)

@app.route("/text",methods=["GET","POST"])
def text():
    msg = request.form.get("msg")
    if msg:
        for x in acclst:
            acc = cl.user_id_from_username(x)
            try:
                cl.direct_send(text=msg,user_ids=[acc])
            except instagrapi.exceptions.UserNotFound:
                flash("User not found please enter valid username")
    return render_template("text.html")


if __name__ == "__main__":
    app.run(debug=True)







































