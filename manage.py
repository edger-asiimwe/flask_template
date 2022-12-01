import os 

from flask_template import init_app, db
from flask_template.models import User

app = init_app()

@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User':User}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ.get("PORT"))