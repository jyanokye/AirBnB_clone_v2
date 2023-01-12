#!/usr/bin/python3
"""Flask"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """states_list"""
    res = []
    storage.reload()

    for v in storage.all("State").values():
        res.append([v.id, v.name])

    return render_template("7-states_list.html", states=res)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """cities_by_states"""
    res = []
    storage.reload()

    for v in storage.all("State").values():
        res.append([v.id, v.name])

    return render_template("8-cities_by_states.html", states=res)


@app.teardown_appcontext
def teardown_db(exception):
    """teardown"""
    storage.close()


if __name__ == "__main__":
    app.run()
