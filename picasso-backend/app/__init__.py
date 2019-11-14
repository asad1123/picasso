from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import requests

from . import settings

# ----------------------------------------------------------------------------


def get_image_list(img_src_url):
    resp = requests.get(img_src_url)
    resp.raise_for_status()

    return resp.text.split("\r\n")


def populate_db(db, img_src_url):
    image_list = get_image_list(img_src_url)
    for image_url in image_list:
        image_id, width, height = image_url.split("/")[-3:]

        image = models.Image(image_id=image_id, width=width, height=height)
        db.session.add(image)
    
    db.session.commit()

# ----------------------------------------------------------------------------


app = Flask(__name__)
app.config.from_object(settings)
app.config["APPLICATION_ROOT"] = "/api/v1"

db = SQLAlchemy(app)

from .models import Image

db.create_all()
populate_db(db, app.config["IMG_SRC_URL"])

# ----------------------------------------------------------------------------

from . import routes