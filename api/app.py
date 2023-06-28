import json

from flask import abort, Flask, request

#######################
#  Initialize the App #
#######################

# Load our 'database' which is just a JSON file here
# Think of this as how we do in-memory caching
with open("./api/assets/database.json") as fp:
    database = json.load(fp)

# Initialize the Flask application
app = Flask(__name__)

##############
#  Endpoints #
##############

# GET all items
@app.route("/", methods=["GET"])
def get_all():
    return database


# GET an ID
@app.route("/<id>", methods=["GET"])
def get_item(id):
    if str(id) in database:
        return database[id]
    else:
        abort(404)


# POST an ID
@app.route("/<id>", methods=["POST"])
def post_item(id):
    if id in database:
        abort(409)
    else:
        database[str(id)] = request.json
        return {id: database[id]}


# PUT an ID
@app.route("/<id>", methods=["PUT"])
def put_item(id):
    if str(id) not in database:
        abort(404)
    else:
        database[str(id)] = request.json
        return {id: database[id]}


# DELETE an ID
@app.route("/<id>", methods=["DELETE"])
def delete_item(id):
    if id not in database:
        abort(404)
    else:
        deleted_item = database[str(id)]
        del database[str(id)]
        return {id: deleted_item}
