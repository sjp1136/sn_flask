from flask import Flask
from flask_sqlalchemy import SQLAlchemy
######################
# TO GET SECRET_KEY #
# import secrets
# secrets.token_hex(16)
#######################

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from sn_flask import routes
