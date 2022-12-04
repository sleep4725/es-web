import os

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return {"test": "hello world"}

@app.route("/cluster/health")
def get_es_cluster_health():
    '''

    :return:
    '''

if __name__ == "__main__":
    app.run(
        host="0.0.0.0"
        ,port=5454
    )