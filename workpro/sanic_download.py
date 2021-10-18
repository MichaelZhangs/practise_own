from sanic.views import HTTPMethodView
import os
from sanic import response, Sanic
from sanic.response import json


class DownLoadView(HTTPMethodView):

    async def get(self, request):
        """下载Excel"""
        EXPORT_PATH = "./data/"

        import xlsxwriter
        file_path = os.path.join(EXPORT_PATH, "shuijun222.xlsx")
        workbook = xlsxwriter.Workbook(file_path)
        rows = ["手机号", "头像",  "性别", "公司", "部门", "职位"]
        sheet = workbook.add_worksheet()
        sheet.write_row("A1", rows)
        workbook.close()
        if os.path.isfile(file_path):
            res = await response.file_stream(file_path)
            return res
        else:
            return json({"error_message": "文件不存在{}".format(file_path), "error_code": "4000"})

app = Sanic(__name__)
app.add_route(DownLoadView.as_view(), "/sanic_test")
if __name__ == '__main__':
    app.run("127.0.0.1", port=8000)