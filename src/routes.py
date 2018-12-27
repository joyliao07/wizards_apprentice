from flask import Flask, request, render_template, redirect, url_for, session, abort, flash, session

from . import app

@app.route('/')
def home():
    return render_template('home_test.html')
