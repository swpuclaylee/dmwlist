# --*--coding: utf-8 --*--
# @Time: 2023-05-26 23:57
# @Author: 李月初
# @FIle: errors
from dmwatchlist import app
from flask import render_template


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404