from app.services.app import app
from . import algorithm

app.add_url_rule('/przemek/', view_func=algorithm.Algorithm.as_view('przemek'))
