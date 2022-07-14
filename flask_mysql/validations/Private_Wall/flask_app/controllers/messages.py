from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import message, user

# Create 
@app.route('/users/message', methods=['POST'])
def create_message():
    if "user_id" in session:
        message.Message.save(request.form)
        return redirect(f'/users/profile/{session["user_id"]}')
    return redirect('/')

# Delete
@app.route('/messages/delete/<int:id>')
def delete_message(id):
    this_message = message.Message.get_message_by_id(id)
    if session['user_id'] != this_message.sender_id or session['user_id'] != this_message.recipient_id:
        if 'counter' not in session:
            session['counter'] = 1
            return redirect(f'/danger/{id}')
        else:
            return redirect('/users/logout')
    message.Message.delete(id)
    return redirect(f'/users/profile/{session["user_id"]}')