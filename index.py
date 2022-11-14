from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>賴玟愷Python讀取Firestore</h1>"
    homepage += "<a href=/account>網頁表單輸入實例</a><br><br>"
    return homepage

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        cond = request.form["leac"]
        cond1= request.form["teac"]
        result = "你的關鍵字的課程為:：" +cond
        result += "你的老師關鍵字為:：" +cond1


        db = firestore.client()
        collection_ref = db.collection("1111")
        docs = collection_ref.get()
        result = ""
        for doc in docs:
            dict = doc.to_dict()
            if cond in dict["Course"] and cond1 in dict["Leacture"]:
                #print("{}老師開的{}課程,每週{}於{}上課".format(dict["Leacture"], dict["Course"],  dict["Time"],dict["Room"]))
            result += dict["Leacture"] + "老師開的" + dict["Course"] + "課程,每週"
            result += dict["Time"] + "於" + dict["Room"] + "上課<br>"

        if result =="":
            result="sorry...."
        return result
    else:
        return render_template("search.html")            

    #if __name__ == "__main__":
     # app.run()