import random
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from .models import Orders

def order_listview(request):
    template_name= 'orders/order_list.html'
    queryset = Orders.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, template_name, context)

    # Create your views here.
def home(request):
    num = None
    #num = random.randint(0, 10000000)
    some_list = [
        random.randint(0, 10000000),
        random.randint(0, 10000000),
        random.randint(0, 10000000)
    ]

    condition_bool_item = True
    if condition_bool_item:
        num = random.randint(0, 1000000)
        context = {
            #"bool_item": False, <-the logic should be in the views, not the html
            "num": num,
            "some_list":some_list
        }

    return render(request, 'home.html', context)#<-context/response

def about(request):
    context ={}
    return render(request, 'about.html', context)#<-context/response



def contact(request):
    context ={}
    return render(request, 'contact.html', context)#<-context/response


class HomeView(TemplateView):
    """Docstring for ContactTemplateView

    """
    template_name = 'home.html'

    # called an overriding method
    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        num = None
        #num = random.randint(0, 10000000)
        some_list = [
            random.randint(0, 10000000),
            random.randint(0, 10000000),
            random.randint(0, 10000000)
        ]

        condition_bool_item = True
        if condition_bool_item:
            num = random.randint(0, 1000000)
            context = {
                #"bool_item": False, <-the logic should be in the views, not the html
                "num": num,
                "some_list":some_list
            }
            return context
