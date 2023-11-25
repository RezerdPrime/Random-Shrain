from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1 style="color:red">Meine Leben ist vorbei</h1>')