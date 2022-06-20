from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/eventdetails')
def eventdetails():
    return render_template("eventdetails.html", user = current_user)


@views.route('/creatorView')
def creatorView():
    return render_template("creatorView.html", user = current_user)

@views.route('/buyticketform')
def buyticketform():
    return render_template("buyticketform.html", user = current_user)

@views.route('/creatorViewCreate')
def creatorViewCreate():
    return render_template("creatorViewCreate.html", user = current_user)

@views.route('/creatorViewEventDetail')
def creatorViewEventDetail():
    return render_template("creatorViewEventDetail.html", user = current_user)

@views.route('/creatorViewManage')
def creatorViewManage():
    return render_template("creatorViewManage.html", user = current_user)