from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Hello world! This is home of the product catalog!')

def catalog(request):
    return HttpResponse('Hello fellows! This is catalog!')