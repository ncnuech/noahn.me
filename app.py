from flask import Flask, render_template
import controllers
app = Flask(__name__, template_folder='views')

app.register_blueprint(controllers.main)

app.secret_key = 'developer'
if __name__ == '__main__':
	app.run(host='162.243.211.114',port=80,debug=True)


