from flask import request, redirect, render_template, session, flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.posts import *
from flask_app.models.users import User
from flask_app import app

#@app.route('/sightings/new',methods=['POST'])
#def createpost():
 #   print(request.form)
  #  Post.save(request.form)
   # return redirect('/success')

@app.route('/sightings/new')
def newsighting():
    id = session['user_id']
    query = "SELECT * FROM users WHERE id = {}".format(id)
    data = connectToMySQL('exam_schema').query_db(query)
    return render_template('sightings_new.html', user_info=data, user_index=id)


@app.route('/newprocess', methods=['POST'])
def newprocess():
    is_valid = True
    id = session['user_id']
    location = request.form['location']
    date = request.form['date']
    num_of_sas = request.form['num_of_sas']
    description = request.form['description']
    if len(location) < 1:
            flash("location cannot be empty!")
            is_valid = False
    if len(date) < 1:
            flash("date cannot be empty!")
            is_valid = False
    if int(num_of_sas) < 1:
            flash("numbder of sasquatch cannot be empty!")
            is_valid = False
    if len(description) < 1:
            flash("description cannot be empty!")
            is_valid = False
    if(is_valid):
        data = {
                'identifier': id,
                'location': location,
                'date': date,
                'num_of_sas': num_of_sas,
                'description': description
            }
        Post.save(data)
        return redirect('/success')
    return redirect('/sightings/new')

@app.route("/delete/<int:post_id>")
def delete(post_id):
    query = "DELETE FROM posts WHERE id = {}".format(post_id)
    data = connectToMySQL('exam_schema').query_db(query)
    return redirect('/success')


@app.route("/sightings/<int:postnum>")
def view(postnum):
    query = "SELECT * FROM posts WHERE id = {}".format(postnum)
    data = connectToMySQL('exam_schema').query_db(query)
    id = session['user_id']
    query_user = "SELECT * FROM users WHERE id = {}".format(id)
    data_user = connectToMySQL('exam_schema').query_db(query_user)
    all_users_query = "SELECT * FROM users"
    data_all_users = connectToMySQL('exam_schema').query_db(all_users_query)
    return render_template('view_post.html', view_data=data, user_info=data_user, all_users = data_all_users)

@app.route("/sightings/edit/<int:post_edit>")
def edit(post_edit):
    query = "SELECT * FROM posts WHERE id = {}".format(post_edit)
    data = connectToMySQL('exam_schema').query_db(query)
    id = session['user_id']
    query_user = "SELECT * FROM users WHERE id = {}".format(id)
    data_user = connectToMySQL('exam_schema').query_db(query_user)
    return render_template('edit_post.html', view_data=data, user_info=data_user, post_id=post_edit)


@app.route('/editprocess/<int:post_id>', methods=['POST'])
def editprocess(post_id):
    is_valid = True
    id = session['user_id']
    location = request.form['location']
    date = request.form['date']
    num_of_sas = request.form['num_of_sas']
    description = request.form['description']
    if len(location) < 1:
            flash("location cannot be empty!")
            is_valid = False
    if len(date) < 1:
            flash("date cannot be empty!")
            is_valid = False
    if int(num_of_sas) < 1:
            flash("numbder of sasquatch cannot be empty!")
            is_valid = False
    if len(description) < 1:
            flash("description cannot be empty!")
            is_valid = False
    if(is_valid):
        data = {
                'identifier': id,
                'location': location,
                'date': date,
                'num_of_sas': num_of_sas,
                'description': description,
                'post_id': post_id
            }
        Post.update(data)
        return redirect('/sightings/' + str(post_id))
    return redirect('/sightings/edit/' + str(post_id))