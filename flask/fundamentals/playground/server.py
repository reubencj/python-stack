from cmath import phase
from distutils.log import debug
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/play/<int:num_box>')
@app.route('/play/<int:num_box>/<string:box_color>')
@app.route('/play')
def play(num_box = 3, box_color = "aqua"):
    return render_template('index.html',num_box = num_box,box_color=box_color)


app.run(debug = True, host='localhost', port=3000)