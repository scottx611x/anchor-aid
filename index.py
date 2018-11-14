import uuid

from flask import Flask, Markup, Response, redirect, render_template, request
import markdown

from utils import dump_s3, load_s3, validate_form_data

app = Flask(__name__)


@app.route('/', defaults={'uuid': None}, methods=['GET'])
@app.route('/<string:uuid>', methods=['GET'])
def index(uuid):
    if uuid is None:
        with open("README.md") as md:
            readme = Markup(markdown.markdown(md.read()))
        return render_template("base.html", **locals())
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


@app.route('/create', methods=['POST'])
def create():
    form_data = request.form.to_dict()

    # Add <scheme>:// if not there already
    validated_form_data = validate_form_data(form_data)
    if not validated_form_data:
        return Response("Bad Request", status=400)

    key = str(uuid.uuid4())
    dump_s3(key, form_data)
    return redirect(f"./{key}")
