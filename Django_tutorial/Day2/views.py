# I am the honour of this website --Dipesh Pandit

from django.http import HttpResponse
#from django.shortcuts import render


def index(request):
    return HttpResponse('<a href="http://127.0.0.1:8080/"><button>Home</button></a>'
                        '<a href="http://127.0.0.1:8080/about"><button>About</button></a>'
                        '<a href="http://127.0.0.1:8080/contact"><button>Contact</button></a>')
    # dic={"name":"Dipesh"}
    # 
    # return render(request,'index.html',dic)
def about(request):
    return HttpResponse('<a href="http://127.0.0.1:8080/"><button>Home</button></a>'
                        '<a href="http://127.0.0.1:8080/about"><button>About</button></a>'
                        '<a href="http://127.0.0.1:8080/contact"><button>Contact</button></a>')

def contact(request):
    return HttpResponse('<a href="http://127.0.0.1:8080/"><button>Home</button></a>'
                        '<a href="http://127.0.0.1:8080/about"><button>About</button></a>'
                        '<a href="http://127.0.0.1:8080/contact"><button>Contact</button></a>')
