from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string

User = get_user_model()

def create_guest_user():
    email = get_random_string(15) + '@guest_user.com'
    password = User.objects.make_random_password()
    first_name = 'Guest'
    last_name = 'Guest'
    guest_user = User.objects.create_user(email=email, 
                                          password=password, 
                                          first_name=first_name, 
                                          last_name=last_name, 
                                          is_guest=True)
    return guest_user

