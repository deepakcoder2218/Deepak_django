from django.http import HttpResponse
from .models import Person

def crud(requset):
    pers = Person(
        name ='deepak chauhan',age ='20',birth ='1999-11-22'
    )
    pers.save()
    print(pers.name)
    return HttpResponse('done')

# Create your views here.
