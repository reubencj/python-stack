from crypt import methods
from flask import Flask, render_template, request, redirect

from friend import Friend
app = Flask(__name__)
@app.route("/")
def index():
    friends = Friend.get_all()
        
    return render_template("index.html", all_friends = friends)
    

@app.route("/create_friend",methods=["POST"])
def create_friend():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "occupation": request.form["occupation"]
    }
    result = Friend.save(data)
    print(result)
    return redirect("/")



        
if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=3000)