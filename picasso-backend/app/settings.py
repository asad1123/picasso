import os

# ----------------------------------------------------------------------------

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = (
    os.environ.get("DATABASE_URL")
    or f"sqlite:///{os.path.join(basedir, 'app.db')}"
)

IMG_SRC_URL = os.environ["IMG_SRC_URL"]
