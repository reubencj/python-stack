from flask_app.models.user import User
from flask_app import app


# data = {
#     'first_name': 'karen',
#     'last_name': 'Joh',
#     'email': 'kemclaughlin@gmail.com', 
#     'password': 'password89',
#     'password_confirm': 'password89',

# }
# print(User.save(data))


print(User.get_user('reuben.chacko.jon@gmail.com'))