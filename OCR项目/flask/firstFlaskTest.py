from flask import Flask,request
import firstTry,os

from flask import render_template
from flask import jsonify
from flask import send_file

app = Flask(__name__)
'''
app = Api(app, version='1.0', title='文字识别接口')

predict = app.namespace('predict')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc'])  # 允许上传的文件类型


@predict.route('/')
class CMDcommand(Resource):
    @app.doc()
    def post(self):
        file = request.files['img']
        if file is None:
            return "未上传文件"

        base64_data = base64.b64encode(file.read())
        s = base64_data.decode()
        url = "http://192.168.5.218:8866/predict/ocr_system"
        data = "{\"images\": [\"%s\"]}" % s
        print(data)
        headers = {
            'Content-Type': 'application/json'
        }
        # 字符串格式
        res = requests.post(url=url, headers=headers, timeout=20, data=data)
        return res.text


def allowed_file(filename):  # 验证上传的文件名是否符合要求，文件名必须带点并且符合允许上传的文件类型要求，两者都满足则返回 true
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
'''

@app.route('/dis',methods=['POST', 'GET'])
def hello_world():


    if request.method == 'POST':

        f = request.files['file']

        basepath = os.path.dirname(__file__)  # 当前文件所在路径

        upload_path = os.path.join(basepath, 'static', f.filename)  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        print(upload_path)
        f.save(upload_path)

        firstTry.distinguish('./flask/static/1336940869923864577.jpg')

    #eturn redirect(url_for('upload'))

    #return render_template('upload.html')


    return "ok"

@app.route('/')
def index():
    return send_file("index.html")




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8081)