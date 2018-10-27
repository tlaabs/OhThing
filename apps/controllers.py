# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for,jsonify
from apps import app,db
from sqlalchemy import desc
from models import (
	User
)
import pusher


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/text', methods=['GET'])
def text():

	p = pusher.Pusher(
		app_id = '',
		key = '',
		secret = ''
		)

	choice = request.args.get('choice')
	txt_msg = request.args.get('txt_msg')
	choice_target = request.args.get('choice_target')
	room_id = request.args.get('room_id')
	i_height = request.args.get('i_height')
	i_width= request.args.get('i_width')

	p['devsim'].trigger('text', {'choice' : choice, 'txt_msg' : txt_msg,'choice_target' : choice_target, 'room_id' : room_id, 'i_height' : i_height, 'i_width' : i_width})

	# code here

	return ""

@app.route('/join', methods = ['GET'])
def join():

	room_id = request.args.get('room_id')

	room_check = User.query.get(room_id)

	if room_check is None:
		User_data = User(
			room_id = room_id,
			available = "1"
			
			)
		db.session.add(User_data)
		db.session.commit()


	if (room_check.available) == "0":
		return jsonify(room_available = "0")

	return jsonify(room_available = "1")




@app.route('/move', methods=['GET'])
def move():
	p = pusher.Pusher(
		app_id = '',
		key = '',
		secret = ''
		)

	x = request.args.get('x')
	y = request.args.get('y')
	id = request.args.get('id')
	room_id = request.args.get('room_id')
	

	p['devsim'].trigger('move', {'x' :x,'y' : y, 'id' : id, 'room_id' : room_id})

	# code here

	return ""

@app.route('/add', methods=['GET'])
def add():
	p = pusher.Pusher(
		app_id = '',
		key = '',
		secret = ''
		)

	id = request.args.get('id')
	index = request.args.get('index')
	room_id = request.args.get('room_id')

	

	p['devsim'].trigger('add', {'id' : id,'index' : index, 'room_id' : room_id})

	# code here

	return ""

@app.route('/del', methods=['GET'])
def delete():
	p = pusher.Pusher(
		app_id = '',
		key = '',
		secret = ''
		)

	del_id = request.args.get('del_id')
	room_id = request.args.get('room_id')

	p['devsim'].trigger('del', {'del_id' : del_id, 'room_id' : room_id})

	# code here

	return ""

@app.route('/add_child', methods=['GET'])
def add_child():
	p = pusher.Pusher(
		app_id = '',
		key = '',
		secret = ''
		)
	
	obj_fullname = request.args.get('obj_fullname')
	child_id = request.args.get('child_id')
	target_parent = request.args.get('target_parent')
	child_x = request.args.get('child_x')
	child_y = request.args.get('child_y')
	room_id = request.args.get('room_id')

	p['devsim'].trigger('child', {'obj_fullname' : obj_fullname,\
	 'child_id' : child_id,'target_parent' : target_parent, 'child_x' : child_x, 'child_y' : child_y, 'room_id' : room_id})

	# code here

	return ""

@app.route('/send_msg', methods=['GET'])
def send_msg():
	p = pusher.Pusher(
		app_id = '',
		key = '',
		secret = ''
		)


	nickname = request.args.get('nickname')
	msg_data = request.args.get('msg_data')
	room_id = request.args.get('room_id')

	p['devsim'].trigger('send_msg', {'nickname' : nickname, 'msg_data' : msg_data, 'room_id' : room_id})

	# code here

	return ""