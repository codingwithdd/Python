# I am the honour of this website --Dipesh Pandit

from django.http import HttpResponse


def index(request):
    return HttpResponse("""<a href="https://www.facebook.com/">Facebook</a>\n<a href="https://www.youtube.com/">Youtube</a>\n<a href="https://www.google.com/">google</a>""")


def about(request):
    return HttpResponse("about")
