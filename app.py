from flask import Flask, request, render_template, redirect, url_for, abort
app = Flask(__name__)

app.secret_key = b'aaa!111/'

@app.route('/')
def index():
    return '메인페이지'

@app.route('/startgame') 
def startgame(): 
    return render_template('startgame.html')

@app.route('/join') 
def join(): 
    return render_template('test.html')

@app.route('/hello/')
def hello():
    return 'Hello, World!'

@app.route('/hello/<name>')
def helloovar(name):
    return 'Hello, {}!'.format(name)

@app.route('/getinfo') 
def getinfo(): 
    # 파일 입력 
    with open("static/save.txt", "r", encoding='utf-8') as file: 
        student = file.read().split(',') # 쉽표로 잘라서 student 에 배열로 저장 
    return '번호 : {}, 이름 : {}'.format(student[0], student[1])

@app.route('/input/<int:num>')
def input_num(num):
    if num == 1:
        return "도라에몽"   
    elif num == 2:
        return "진구"
    elif num == 3:
        return "퉁퉁이"
    else:
        return "없어요"

    # return 'Hello, {}!'.format(name)

# 로그인
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
        print (id,type(id))
        print (pw,type(pw))
        # id와 pw가 임의로 정한 값이랑 비교 해서 맞으면 맞다 틀리면 틀리다
        if id == 'abc' and pw == '1234':
            session['user'] = id
            return ''' 
                <script> alert("안녕하세요~ {}님"); 
                location.href="/form" 
                </script>
             '''.format(id) 
             # return redirect(url_for('form'))
        else:
            return "아이디 또는 패스워드를 확인 하세요."

#로그인 사용자만 접근 가능으로 만들면
@app.route('/form') 
def form(): 
    if 'user' in session: 
        return render_template('test.html') 
    return redirect(url_for('login'))

@app.route('/logout') 
def logout(): 
    session.pop('user', None) 
    return redirect(url_for('form'))


@app.route('/method', methods=['GET', 'POST']) 
def method(): 
    if request.method == 'GET':
         # args_dict = request.args.to_dict() 
         # print(args_dict) 
         num = request.args["num"] 
         name = request.args.get("name") 
         
         return "GET으로 전달된 데이터({}, {})".format(num, name) 
    else: 
        num = request.form["num"] 
        name = request.form["name"] 
        with open("static/save.txt","w", encoding='utf-8') as f: 
            f.write("%s,%s" % (num, name)) 
        return "POST로 전달된 데이터({}, {})".format(num, name)

@app.route('/naver')
def naver():
    return redirect("https:/www.naver.com/")
    # return render_template("naver.html")

@app.route('/kakao')
def daum():
    return redirect("https:/www.daum.net/")

@app.route('/urltest')
def url_test():
    return redirect(url_for("naver"))

@app.route('/move/<site>')
def move_site(site):
    if site == 'naver':
        return redirect(url_for("naver"))
    elif site == 'daum':
        return redirect(url_for("daum"))
    else:
        abort(404)
        # return '없는 페이지 입니다.'

@app.route('/') 
def index(): 
    return render_template("main.html")

@app.errorhandler(404)
def page_not_found(error):
    return "페이지가 없습니다. URL을 확인 하세요", 404

@app.route('/img')
def img():
    return render_template("myimage.html")

if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('daum'))