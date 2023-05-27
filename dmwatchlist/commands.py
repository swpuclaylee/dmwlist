# --*--coding: utf-8 --*--
# @Time: 2023-05-26 23:58
# @Author: 李月初
# @FIle: commands
from dmwatchlist import db, app
from dmwatchlist.models import User

import click


@app.cli.command()# 注册为命令
@click.option('--drop', is_flag=True, help='Create after drop')
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')


@app.cli.command()
@click.option('--username', prompt=True, help='The username used to login.')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
def admin(username, password):
    db.create_all()
    user = User().query.first()
    if user is not None:
        click.echo('Updating user...')
        user.username = username
        user.set_password(password)
    else:
        click.echo('Creating user...')
        user = User(username=username, name='clay')
        user.set_password(password)
        db.session.add(user)
    db.session.commit()
    click.echo('Done')