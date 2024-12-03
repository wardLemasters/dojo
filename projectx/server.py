# ...server.py
from flask_app import app
from flask_app.controllers.user import *
from flask_app.controllers.post import *
# ...server.py



if __name__=="__main__":
    app.run(debug=True, host="localhost", port=8000)