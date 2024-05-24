from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import get_user_model

User = get_user_model()

class GuestSessionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.user.is_authenticated:
            if 'guest_user_id' in request.session:
                try:
                    guest_user = User.objects.get(id=request.session['guest_user_id'])
                    request.user = guest_user
                except User.DoesNotExist:
                    pass