from flask import jsonify,request,Blueprint
from workers import add_user, get_user_by_id, get_all_active_users, deactivate_user, activate_user, delete_user, update_user
users = Blueprint('users', __name__)

@users.route('/user/update/<user_id>', methods=["POST"])
def update_user_route(user_id):
    user_dict = get_user_by_id(user_id)
    new_data = request.form if request.form else request.json

    if new_data:
      new_data = dict(new_data)
    else:
      return jsonify("No values to change")

    user_dict.update(new_data)

    updated_fields = []

    for field in new_data:
      updated_fields.append(field)

    if updated_fields:
      fields_str = ','.join(updated_fields)
    else:
      fields_str = ""

    if fields_str:
      update_user(user_dict)
      return jsonify(f'{fields_str} have been updated for User ID: {user_id}')

    else:
      return jsonify(f'No Fields Updated')

@users.route('/user/deactivate/<user_id>', methods=["POST"])
def deactivate_user_route(user_id):
  deactivate_user(user_id)
  return jsonify(f'User with ID {user_id} has been set to inactive.'), 200

@users.route('/user/activate/<user_id>', methods=["POST"])
def activate_user_route(user_id):
  activate_user(user_id)
  return jsonify(f'User with ID {user_id} has been set to active.')

@users.route('/user/delete/<user_id>', methods=["POST"])
def delete_user_route(user_id):
  delete_user(user_id)
  return jsonify(f'User with ID {user_id} has been deleted')

@users.route('/user/add', methods=["POST"])
def user_add():
  post_data =  request.form if request.form else request.json
  first_name = post_data.get('first_name')
  last_name = post_data.get('last_name')
  email = post_data.get('email')
  phone = post_data.get('phone')
  city = post_data.get('city')
  state = post_data.get('state')
  org_id = post_data.get('org_id')
  active = post_data.get('active')

  add_user(first_name, last_name, email, phone, city, state, org_id, active)
  return jsonify("User created"), 201

@users.route('/users/get', methods=["GET"])
def get_all_active_users_route():
    users = get_all_active_users()

    return jsonify(users), 200