from flask import Flask, render_template, jsonify, request
# FmysJiwa6dE7hCoh
import pymongo
client = pymongo.MongoClient(
    "mongodb+srv://ptd_admin:<password>@cluster0.cmnzcow.mongodb.net/?retryWrites=true&w=majority")
db = client.todolist

app = Flask(__name__)

app.config["MONGo_CONNECT"] = False


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def sendpost():
    todoText = request.form['todoText']
    client.todo.insert_one({"todoText": todoText})
    # return( jsonify(msg={msg:"todocreated"}))


if __name__ == "__main__":
    app.run(debug=True)
