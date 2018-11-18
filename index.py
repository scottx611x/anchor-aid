import uuid

from flask import Flask, Markup, Response, redirect, render_template, request
import markdown

from config import set_app_config
from utils import S3Interface, validate_form_data


app = Flask(__name__)
set_app_config(app)

s3 = S3Interface(app)


@app.route('/', defaults={'uuid': None}, methods=['GET'])
@app.route('/<string:uuid>', methods=['GET'])
def index(uuid):
    if uuid is None:
        with open("README.md") as md:
            readme = Markup(markdown.markdown(md.read()))
        return render_template("base.html", **{"readme": readme})
    else:
        try:
            data = s3.load(uuid)
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
    s3.dump(key, form_data)
    return redirect(f"./{key}")
