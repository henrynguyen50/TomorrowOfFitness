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

@views.route('/WorkoutPlanner', methods=['GET', 'POST'])
@login_required
def workout():
    if request.method == 'POST':
        full_body_note = request.form.get('full_body_note')
        upper_lower_note = request.form.get('upper_lower_note')

        if full_body_note and len(full_body_note) > 1:
            new_note = Note(data=f"Full Body: {full_body_note}", user_id=current_user.id)
            db.session.add(new_note)

        if upper_lower_note and len(upper_lower_note) > 1:
            new_note = Note(data=f"Upper Lower: {upper_lower_note}", user_id=current_user.id)
            db.session.add(new_note)

        db.session.commit()
        flash('Workout added!', category='success')

    return render_template("WorkoutPlanner.html", user=current_user)

@views.route('/guidelines')
@login_required
def guidelines():

    return render_template("guidelines.html", user=current_user)

@views.route('/brainrot')
@login_required
def brainrot():

    return render_template("brainrot.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


