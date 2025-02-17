from flask import Flask
from flask_oidc import OpenIDConnect
from flask_bootstrap import Bootstrap5
import os
from .config import Config, DevConfig

os.environ['REQUESTS_CA_BUNDLE'] = '/etc/ssl/certs/ca-certificates.crt'

app = Flask(__name__)
oidc = OpenIDConnect()
bs = Bootstrap5()

if 'FLASK_DEV' in os.environ:
    config = DevConfig()
else:
    config = Config()


def create_app():
    app.config.from_object(config)
    oidc.init_app(app)
    bs.init_app(app)
    from .views import views
    app.register_blueprint(views)
    return app

