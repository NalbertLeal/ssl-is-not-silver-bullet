from flask import Flask, request, redirect
from OpenSSL import SSL

if __name__ == '__main__':
    context = ('./keys/certificate.crt', './keys/privateKey.key')

    app = Flask(__name__)

    @app.before_request
    def before_request():
        if request.url.startswith('http://'):
            url = request.url.replace('http://', 'https://', 1)
            code = 301
            return redirect(url, code=code)

    @app.route('/', methods=['GET'])
    def index():
        return """
        <form action='/login' method='POST'>
            Username: <input type='text' name='username' placeholder='username'> </input>
            Password: <input type='password' name='password' placeholder='password'> </input>
            <input type='submit' value='submit'> </input>
        </form>
    """

    @app.route('/login', methods=['GET','POST'])
    def login():
        username = request.form.get("username")
        password = request.form.get("password")
        print(username)
        if username == 'nalbertg' and password == '2444666668888888':
            code = 301
            return redirect('https://localhost:4040/profile/' + username, code=code)
        else:
            code = 301
            return redirect('https://localhost:4040', code=code)

    @app.route('/profile/<user>', methods=['GET'])
    def profile(user):
        return "<h1> "+ user +" </h1>"

    app.run(host='localhost', port=4040, debug=True, ssl_context=context, threaded=True)
