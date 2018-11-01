import uuid

from flask import Flask, Response, jsonify, redirect, render_template, request

from .utils import dump_s3, load_s3, validate_form_data

app = Flask(__name__)


@app.route('/', defaults={'uuid': None}, methods=['GET'])
@app.route('/<string:uuid>', methods=['GET'])
def index(uuid):
    if uuid is None:
        return render_template("base.html")
    else:
        try:
            data = load_s3(uuid)
        except Exception as e:
            return Response(f"Bad Request: {e}", status=400)
        else:
            return render_template(
                "anchor-aid.html",
                **{"site": data["site"], "search": data["search"]}
            )


@app.route('/list/<string:uuid>', methods=['GET'])
def list(uuid):
    return jsonify(load_s3(uuid))


@app.route('/create', methods=['POST'])
def create():
    form_data = request.form
    if not validate_form_data(form_data):
        return Response("Bad Request", status=400)

    key = str(uuid.uuid4())
    dump_s3(key, form_data)
    return redirect(f"/{key}")
