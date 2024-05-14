from main import create_app
from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy


app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://system:qweseam1@103.175.242.10:3306/voter'


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
