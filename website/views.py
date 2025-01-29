from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    

    return render_template("home.html", user=current_user)


@views.route('/FAQ')
@login_required
def faq():

    return render_template("FAQ.html", user=current_user)


@views.route('/WorkoutPlanner')
@login_required
def workout():

    return render_template("WorkoutPlanner.html", user=current_user)

@views.route('/brainrot')
@login_required
def brainrot():

    return render_template("brainrot.html", user=current_user)


