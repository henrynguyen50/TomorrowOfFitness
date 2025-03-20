# Import required Flask modules and database models
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
import time
from random import shuffle

# Create Blueprint for views
views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    # Render home page template
    return render_template("home.html", user=current_user)


@views.route('/FAQ')
@login_required
def faq():
    # Render FAQ page template
    return render_template("FAQ.html", user=current_user)

@views.route('/WorkoutPlanner', methods=['GET', 'POST'])
@login_required
def workout():
    # Handle workout form submission
    if request.method == 'POST':
        full_body_note = request.form.get('full_body_note')
        upper_lower_note = request.form.get('upper_lower_note')

        # Save full body workout if provided and valid
        if full_body_note and len(full_body_note) > 1:
            new_note = Note(data=f"Full Body: {full_body_note}", user_id=current_user.id)
            db.session.add(new_note)

        # Save upper/lower workout if provided and valid  
        if upper_lower_note and len(upper_lower_note) > 1:
            new_note = Note(data=f"Upper Lower: {upper_lower_note}", user_id=current_user.id)
            db.session.add(new_note)

        db.session.commit()
        flash('Workout added!', category='success')

    return render_template("WorkoutPlanner.html", user=current_user)

@views.route('/guidelines')
@login_required
def guidelines():
    # Render workout guidelines page template
    return render_template("guidelines.html", user=current_user)

@views.route('/brainrot')
@login_required
def brainrot():
    #list of dictionaries, each dictionary contains a username and id of a tiktok video
    #can access by index
    videos = [
        {'username': 'coach_mundy_', 'id': '7473904064862948638'},
        {'username': 'coach_mundy_', 'id': '7466475546600410399'},
        {'username': 'coach_mundy_', 'id': '7460530053974134047'},
        {'username': 'coach_mundy_', 'id': '7461275482730908958'},
        {'username': 'coach_mundy_', 'id': '7472784522883435807'},
        {'username': 'coach_mundy_', 'id': '7468735293001141535'},
        {'username': 'coach_mundy_', 'id': '7466118683534822687'},
        {'username': 'coach_mundy_', 'id': '7462768678178671902'},
        {'username': 'coach_mundy_', 'id': '7474609601850182943'},
        {'username': 'coach_mundy_', 'id': '7474263950129974559'},

        {'username': 'scivinhtific', 'id': '7470380143547108638'},
        {'username': 'scivinhtific', 'id': '7463943707885128991'},
        {'username': 'scivinhtific', 'id': '7461815511626665246'},
        {'username': 'scivinhtific', 'id': '7459454317100141867'},
        {'username': 'scivinhtific', 'id': '7456136473260166446'},
        {'username': 'scivinhtific', 'id': '7458438938135579950'},
        {'username': 'scivinhtific', 'id': '7455995333333333333'},
        
        {'username': 'dxklanx', 'id': '7463959288533273864'},
        {'username': 'dxklanx', 'id': '7460315691804052743'},
        {'username': 'dxklanx', 'id': '7459125277927542024'},
        {'username': 'dxklanx', 'id': '7455798535116705031'},
        {'username': 'dxklanx', 'id': '7472185255336742162'},

        {'username': 'doom_mxn', 'id': '7456905543362333984'},
        {'username': 'doom_mxn', 'id': '7452771458209664288'},
        {'username': 'doom_mxn', 'id': '7452116449713212705'},
        {'username': 'doom_mxn', 'id': '7450558446879001888'},

        {'username': 't_nutrition_fitness', 'id': '7472393756193443118'},
        
        
        {'username': 'scientificallyjacked', 'id': '7463206872812637486'},
        {'username': 'scientificallyjacked', 'id': '7459474781138783534'},
        {'username': 'scientificallyjacked', 'id': '7456134075275857198'},
        {'username': 'scientificallyjacked', 'id': '7451785471686036782'},
        {'username': 'scientificallyjacked', 'id': '7475793442187087150'},

        {'username': 'calciumionsfanclub', 'id': '7472889193048313106'},
        {'username': 'calciumionsfanclub', 'id': '7470716387825028370'},
        {'username': 'calciumionsfanclub', 'id': '7468587000837246215'},
        {'username': 'calciumionsfanclub', 'id': '7467722950817369362'},
        {'username': 'calciumionsfanclub', 'id': '7467382448259665170'},
        {'username': 'calciumionsfanclub', 'id': '7467145802066988295'},
        {'username': 'calciumionsfanclub', 'id': '7465657880784473362'}
    ]
    import random
    random.seed(time.time())
    shuffle(videos)
    # Render brainrot page template with social media embeds
    return render_template("brainrot.html", user=current_user, videos=videos)

@views.route('/delete-note', methods=['POST'])
def delete_note():  
    # Parse note ID from JSON request data sent by frontend
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    
    # Delete note if it exists and belongs to current user
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})