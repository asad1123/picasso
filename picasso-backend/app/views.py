from flask import jsonify, request
from flask.views import MethodView
from sqlalchemy import func

from . import app, db
from .models import Image

# ----------------------------------------------------------------------------

# setting max dimensions as defaults to show all images at start
MAX_WIDTH = db.session.query(func.max(Image.width)).scalar()
MAX_HEIGHT = db.session.query(func.max(Image.height)).scalar()

# ----------------------------------------------------------------------------


class ImageView(MethodView):
    """HTTP request dispatcher for /images/ route"""
    def get(self):
        """GET method callback"""
        page = int(request.args.get("page", default=1))
        width = int(request.args.get("width", default=MAX_WIDTH))
        height = int(request.args.get("height", default=MAX_HEIGHT))

        # filter images based on GET query parameters
        images = (
            db.session.query(Image)
            .filter(width >= Image.width, height >= Image.height)
            .paginate(page=page, error_out=False, max_per_page=10)
        )

        image_metadata = [
            {"id": img.image_id, "width": img.width, "height": img.height}
            for img in images.items
        ]

        resp = jsonify(
            {
                "data": image_metadata,
                "page_info": {
                    "current": images.page,
                    "next_num": images.next_num if images.has_next else None,
                    "prev_num": images.prev_num if images.has_prev else None,
                },
            }
        )
        
        # enable CORS 
        resp.headers.add("Access-Control-Allow-Origin", "*")

        return resp
