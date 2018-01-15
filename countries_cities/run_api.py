# coding: utf-8

from countries_cities import app, api
from countries_cities import views


def route_resources():
    # api.add_resource(Book, '/book')
    pass


def run_api():
    app.run(debug=True)


if __name__ == '__main__':
    route_resources()
    run_api()
