from db import conn, cursor

def add_user(first_name, last_name, email, phone, city, state, org_id, active):
  cursor.execute("""
  INSERT INTO Users (first_name, last_name, email, phone, city, state, org_id, active)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s);""", (first_name, last_name, email, phone, city, state, org_id, active))
  
  conn.commit()

def get_all_active_users():
    cursor.execute('SELECT * FROM Users WHERE active=1')
    results = cursor.fetchall()
    if results:
      users = []
      for result in results:
        user = {
          'user_id'   : result[0],
          'first_name': result[1],
          'last_name' : result[2],
          'email'     : result[3],
          'phone'     : result[4],
          'city'      : result[5],
          'state'     : result[6],
          'org_id'    : result[7],
          'active'    : result[8]
        }

        if user['org_id']:
          cursor.execute('SELECT * FROM Organizations WHERE org_id = %s', [user['org_id']])
          org_result = cursor.fetchone()
          org = { 
            'organization': {
                "org_id" : org_result[0],
                "name"   : org_result[1],
                "phone"  : org_result[2],
                "city"   : org_result[3],
                "state"  : org_result[4],
                "active" : org_result[5]
            }
          }

          user.update(org)
        users.append(user)
      return users

def get_user_by_id(user_id):
  cursor.execute('SELECT * FROM Users WHERE user_id = %s', [user_id])
  result = cursor.fetchone()
  if result:
    user = {
      'user_id'   : result[0],
      'first_name': result[1],
      'last_name' : result[2],
      'email'     : result[3],
      'phone'     : result[4],
      'city'      : result[5],
      'state'     : result[6],
      'org_id'    : result[7],
      'active'    : result[8]
    }
    return user

def update_user(user_dict):

    user_id = user_dict['user_id']
    first_name = user_dict['first_name']
    last_name = user_dict['last_name']
    phone = user_dict['phone']
    email = user_dict['email']
    city = user_dict['city']
    state = user_dict['state']
    org_id = user_dict['org_id']
    active = user_dict['active']

    cursor.execute('''UPDATE Users SET 
      first_name = %s,
      last_name = %s,
      email = %s,
      phone = %s,
      city = %s,
      state = %s,
      org_id = %s,
      active = %s
      WHERE user_id = %s''',
      [first_name,last_name,phone,email,city,state,org_id,active, user_id])

    conn.commit()

def deactivate_user(user_id):
    cursor.execute('UPDATE Users SET active = 0 WHERE user_id = %s', [user_id])
    conn.commit()

def activate_user(user_id):
    cursor.execute('UPDATE Users SET active = 1 WHERE user_id = %s', [user_id])
    conn.commit()

def delete_user(user_id):
    cursor.execute('DELETE FROM Users WHERE user_id = %s', [user_id])
    conn.commit()