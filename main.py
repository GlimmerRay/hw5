import flask
import os

app = flask.Flask(__name__)

my_fav_shows = ['Legend of Korra', 'Hunter x Hunter', 'Vikings', 'Heaven\'s Lost Property', 'Avatar: the last airbender']
korra = my_fav_shows[0]
hunter = my_fav_shows[1]
vikings = my_fav_shows[2]

@app.route('/')
def index():
    return flask.render_template("index.html", my_fav_shows=my_fav_shows)

app.run(
    debug=True
)