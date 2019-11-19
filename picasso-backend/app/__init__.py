from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import requests

from . import settings

# ----------------------------------------------------------------------------


def get_image_list(img_src_url):
    """Get list of image URLs from pastebin"""
    resp = requests.get(img_src_url)
    resp.raise_for_status()

    return resp.text.split("\r\n")


def populate_db(db, img_src_url):
    """Split image URL into metadata to be stored"""
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

# Create DB table (in this case `image`)
db.create_all()

# Get image URLs from pastebin, preprocess, and store metadata in DB
populate_db(db, app.config["IMG_SRC_URL"])

# ----------------------------------------------------------------------------

from . import routes
