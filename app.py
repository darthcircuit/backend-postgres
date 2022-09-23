from flask import Flask
import routes
import db

app = Flask(__name__)

app.register_blueprint(routes.users)
app.register_blueprint(routes.orgs)

if __name__ == '__main__':
  db.create_all()
  app.run(port=8086, host="0.0.0.0")