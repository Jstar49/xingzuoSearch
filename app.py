from flask import Flask,jsonify, make_response, render_template,request, session, url_for, redirect
import time
import requests

app = Flask(__name__)

@app.route('/<name>')
def index1(name):
    return render_template('hello.html', name=name)

@app.route('/login', methods=['POST', 'GET'])
def login():
    # 当请求方式是 POST
    if request.method == 'POST':
        #print(request.form.get("user"))
        if request.form['user'] == 'admin':
            session['user'] = request.form['user']
            response = make_response('Admin login successfully!')
            response.set_cookie('login_time', time.strftime('%Y-%m-%d %H:%M:%S'))
        else:
            return 'No such user!'
    # 当请求方式是 GET
    else:
        if 'user' in session:
            login_time = request.cookies.get('login_time')
            response = make_response('Hello %s, you logged in on %s' % (session['user'], login_time))
        else:
            title = request.args.get('title', 'comsters')
            response = make_response(render_template('login.html', title=title), 200)
            response.headers['key'] = 'lelelle'
            return response
    return response

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/updatebg', methods=['POST'], strict_slashes=False)
def update():
    return jsonify({"colors": "yellow"})

@app.route('/click')
def click():
    return render_template('click.html', bgcolor=0)

def Hitokoto():
    url = "https://v1.hitokoto.cn/?encode=json&charset=utf-8&c=a"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    response = requests.get(url, headers=headers)
    res = response.json()
    return (res['from'], res['hitokoto'])

@app.route('/')
def index():
    hitokoto = {}
    hitokoto['from'], hitokoto['hitokoto'] = Hitokoto()
    return render_template('index.html',hitokoto=hitokoto)

app.secret_key = '123sdf'
if __name__ == '__main__':
    app.run(debug=True)