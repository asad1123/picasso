import uuid

from . import db

# ----------------------------------------------------------------------------


def uuid_to_str():
    return str(uuid.uuid4())

# ----------------------------------------------------------------------------

class Image(db.Model):
    id = db.Column(db.String, primary_key=True, nullable=False, default=uuid_to_str)
    image_id = db.Column(db.Integer)
    width = db.Column(db.Integer)
    height = db.Column(db.Integer)

    def __repr__(self):
        return f"<Image https://picsum.photos/id/{self.id}/{self.width}/{self.height}>"