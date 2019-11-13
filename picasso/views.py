from flask import jsonify, request
from flask.views import MethodView
from sqlalchemy import func

from .models import Image

from . import app, db

# ----------------------------------------------------------------------------

MAX_WIDTH = db.session.query(func.max(Image.width)).scalar()
MAX_HEIGHT = db.session.query(func.max(Image.height)).scalar()

# ----------------------------------------------------------------------------


class ImageView(MethodView):
    def get(self):

        page = int(request.args.get("page", default=1))
        width = int(request.args.get("width", default=MAX_WIDTH))
        height = int(request.args.get("height", default=MAX_HEIGHT))

        images = (
            db.session.query(Image)
            .filter(Image.width <= width)
            .filter(Image.height <= height)
            .paginate(page=page, error_out=False, max_per_page=10)
        )

        image_metadata = [
            {"id": img.image_id, "width": img.width, "height": img.height}
            for img in images.items
        ]

        return jsonify({
            "data": image_metadata,
            "page_info": {
                "current": images.page,
                "next_num": images.next_num if images.has_next else None,
                "prev_num": images.prev_num if images.has_prev else None,
            }
        })
