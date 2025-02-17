from python_freeipa import Client
from . import config


def reset_password(username,
                   old_password,
                   new_password):
    

    ipa = Client(host=config.IPA_SERVER)

    try:
        ipa.change_password(old_password=old_password,username=username,new_password=new_password)
        return "success"
    except Exception as e:
        return e