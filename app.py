# from flask import Flask
# from flask_restful import Resource, Api
#
# app = Flask(__name__)
# api = Api(app)
#
#
# class fakeapi(Resource):
#     def get(self):
#         thisdict = {
#             "brand": "Ford",
#             "model": "Mustang",
#             "year": 1964
#         }
#         return thisdict
#
#
#
# api.add_resource(fakeapi, '/fake')
#
# if __name__ == '__main__':
#     app.run(debug=True)

import calendar

calendar.prcal(2022)

