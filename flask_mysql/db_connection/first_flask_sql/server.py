from flask import Flask, render_template

from friend import Friend
app = Flask(__name__)
@app.route("/")
def index():
    friends = Friend.get_all()
    for f in friends:
        print(f.first_name)
        
    return render_template("index.html")
            
if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=3000)

