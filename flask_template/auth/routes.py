from . import auth

@auth.route('/login')
def login():
    return 'I am okay'