from flask import request, make_response
from flask import Flask, jsonify, Response
from flask_restful import Api, Resource
import time
import datetime
import xlsxwriter
from io import BytesIO

class Test(Resource):

    def create_excel(self):
        output = BytesIO()
        resp = Response()

        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()

        rows = ["col1", "col2", "col3"]
        worksheet.write_row("A1", rows)
        dictList = [{"a": "a1", "b": "b1", "c": "c1"}, {"a": "a2", "b": "b2", "c": "c2"},
                    {"a": "a3", "b": "b3", "c": "c3"}]
        for i in range(len(dictList)):
            row = [dictList[i]["a"], dictList[i]["b"], dictList[i]["c"]]
            print(row)
            worksheet.write_row('A{}'.format(i+2), row)
        workbook.close()
        resp.data = output.getvalue()
        # resp = make_response(output.getvalue())

        return resp

    def get(self):

        response = self.create_excel()
        print(response)
        response.headers['Content-Type'] = "utf-8"
        response.headers["Cache-Control"] = "no-cache"
        response.headers["Content-Disposition"] = "attachment; filename=download.xlsx"
        return make_response(response)
        # return response

app = Flask(__name__)
api = Api(app)
api.add_resource(Test, "/download")
if __name__ == '__main__':
    app.run("127.0.0.1", port=8888)