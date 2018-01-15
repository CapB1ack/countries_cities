# coding: utf-8

import vk_api

from flask_restful import Resource, request


class VkAuth(Resource):

    def post(self):
        login, password = '89103468336', 'Arti-marti260594'
        vk_session = vk_api.VkApi(login, password)

        try:
            vk_session.auth()
        except vk_api.AuthError as error_msg:
            print(error_msg)
            return

        vk = vk_session.get_api()


class GetCountries(Resource):

    def get(self):
        response = vk.database.getCountries(need_all=1, count=236)
        return response


class GetCities(Resource):

    def get(self, country_id):
        response = vk.database.getCities(country_id=country_id)
        return response