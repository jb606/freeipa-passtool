import os
import yaml

class Config():
    with open("config.yaml") as config_file:
        cfg_file = yaml.load(config_file, Loader=yaml.FullLoader)
    def _get_secret_key(cfg):
        if os.environ.get("FLASK_SECRET_KEY"):
            return os.environ.get("FLASK_SECRET_KEY")
        elif "secret_key" in cfg:
            return cfg['secret_key']
        else:
            return os.urandom(12).hex()


    DEBUG = False
    SESSION_TYPE = "filesystem"
    SECRET_KEY = _get_secret_key(cfg_file)
    OIDC_CLIENT_SECRETS = cfg_file['oauth']
    OIDC_ID_TOKEN_COOKIE_SECURE = False
    #OIDC_COOKIE_SECURE = False
    OIDC_USER_INFO_ENABLED = True
    OIDC_SCOPES = "openid email profile"
    OIDC_INTROSPECTION_AUTH_METHOD = 'client_secret_post'
    if 'default_theme' in cfg_file:
        BOOTSTRAP_BOOTSWATCH_THEME = cfg_file['default_theme']
    else:
        BOOTSTRAP_BOOTSWATCH_THEME = 'darkly'

    IPA_SERVER = cfg_file['ipa_server']
class DevConfig(Config):
    DEBUG = True