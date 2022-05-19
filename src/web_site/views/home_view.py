from flask import render_template

from utils.base_definitions import MULTIPLICATION_ALGORITHM


class HomeView:
    def __init__(self):
        pass

    def get(self):
        return render_template(template_name_or_list="home/index.jinja2", algortims=MULTIPLICATION_ALGORITHM), 200
