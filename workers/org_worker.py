from db import conn, cursor

def add_org(name, phone, city, state, active):
  cursor.execute("""
  INSERT INTO Organizations (name, phone, city, state, active)
    VALUES (%s,%s,%s,%s,%s);""", (name, phone, city, state, active))
  
  conn.commit()

def get_all_active_orgs():
    cursor.execute('SELECT * FROM Organizations WHERE active=1')
    results = cursor.fetchall()
    if results:
      orgs = []
      for result in results:
        org = {
          'org_id'    : result[0],
          'name'      : result[1],
          'phone'     : result[2],
          'city'      : result[3],
          'state'     : result[4]

        }

        orgs.append(org)
      return orgs

def get_org_by_id(org_id):
    cursor.execute('SELECT * FROM Organizations WHERE org_id = %s', [org_id])
    result = cursor.fetchone()
    if result:
        org = {
          'org_id'    : result[0],
          'name'      : result[1],
          'phone'     : result[2],
          'city'      : result[3],
          'state'     : result[4]

        }
    return org

def update_org(org_dict):

    org_id = org_dict['org_id']
    name = org_dict['name']
    phone = org_dict['phone']
    city = org_dict['city']
    state = org_dict['state']
    active = org_dict['active']

    cursor.execute('''UPDATE orgs SET 
      name = %s,
      phone = %s,
      city = %s,
      state = %s,
      active = %s
      WHERE org_id = %s''',
      [name,phone,city,state,active,org_id])

    conn.commit()

def deactivate_org(org_id):
    cursor.execute('UPDATE Organizations SET active = 0 WHERE org_id = %s', [org_id])
    conn.commit()

def activate_org(org_id):
    cursor.execute('UPDATE Organizations SET active = 1 WHERE org_id = %s', [org_id])
    conn.commit()

def delete_org(org_id):
    cursor.execute('DELETE FROM Organizations WHERE org_id = %s', [org_id])
    conn.commit()