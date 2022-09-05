from flask import Flask
from views import views

application = Flask(__name__)
# application.register_blueprint(views, url_prefix="/views")

# if __name__ == '__main__':
#     application.run( debug=True, port=5000)

@application.route('/')
def hello_world():
    return 'Sup. Scrub'