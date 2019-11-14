from . import app, views

# ----------------------------------------------------------------------------

app.add_url_rule("/images/", view_func=views.ImageView.as_view("get_images"))
