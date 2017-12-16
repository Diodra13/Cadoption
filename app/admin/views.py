from flask import render_template
from flask_login import login_required

from . import admin

@admin.route('/admin_page')
def admin_page():
    return render_template("admin/admin_page.html", title='admin_page')