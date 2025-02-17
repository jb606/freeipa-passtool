from flask import Blueprint, render_template, url_for, request, jsonify, redirect

from . import oidc
from .freeipa import reset_password
import html2text
views = Blueprint('views', __name__)

@views.route("/", methods=['GET', 'POST'])
@oidc.require_login
def home_path():
    info = oidc.user_getinfo(['preferred_username', 'given_name', 'family_name'])
    username = info['preferred_username']
    full_name = info['given_name'] + " " + info['family_name']
    context = { 'current_user': full_name,
                'username': username,
               }
    if request.method == 'POST':
        current_password = request.form.get('current_password')
        new_password = request.form.get('password')
        status = reset_password(username=username, old_password=current_password, new_password=new_password)
        if status == "success":
            reset_state = True
        else:
            reset_state = False
            status = html2text.html2text(str(status))
        context.update({ 'status': reset_state })
        print(status)
        return render_template("main.html", data=context, status=status)
    else:
        return render_template("main.html", data=context)