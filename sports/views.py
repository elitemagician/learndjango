from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1><marquee><b>CJ's Sports News and Scores</marquee></b>")