from flask import jsonify,request,Blueprint
from workers import add_org, get_org_by_id, get_all_active_orgs, deactivate_org, activate_org, delete_org, update_org
orgs = Blueprint('orgs', __name__)

@orgs.route('/org/update/<org_id>', methods=["POST"])
def update_org_route(org_id):
    org_dict = get_org_by_id(org_id)
    new_data = request.form if request.form else request.json

    if new_data:
      new_data = dict(new_data)
    else:
      return jsonify("No values to change")

    org_dict.update(new_data)

    updated_fields = []

    for field in new_data:
      updated_fields.append(field)

    if updated_fields:
      fields_str = ','.join(updated_fields)
    else:
      fields_str = ""

    if fields_str:
      update_org(org_dict)
      return jsonify(f'{fields_str} have been updated for org ID: {org_id}')

    else:
      return jsonify(f'No Fields Updated')

@orgs.route('/org/deactivate/<org_id>', methods=["POST"])
def deactivate_org_route(org_id):
  deactivate_org(org_id)
  return jsonify(f'org with ID {org_id} has been set to inactive.'), 200

@orgs.route('/org/activate/<org_id>', methods=["POST"])
def activate_org_route(org_id):
  activate_org(org_id)
  return jsonify(f'org with ID {org_id} has been set to active.')

@orgs.route('/org/delete/<org_id>', methods=["POST"])
def delete_org_route(org_id):
  delete_org(org_id)
  return jsonify(f'org with ID {org_id} has been deleted')

@orgs.route('/org/add', methods=["POST"])
def org_add():
  post_data = request.form if request.form else request.json
  name = post_data.get('name')
  phone = post_data.get('phone')
  city = post_data.get('city')
  state = post_data.get('state')
  active = post_data.get('active')

  add_org(name, phone, city, state, active)
  return jsonify("org created"), 201

@orgs.route('/orgs/get', methods=["GET"])
def get_all_active_orgs_route():
    orgs = get_all_active_orgs()

    if orgs:
        return jsonify(orgs), 200

    else:
        return jsonify('No matching records')