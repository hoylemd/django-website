from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


def hello_function_based_view(request):
    """Example of a simple function based view"""
    return HttpResponse('hello, world!')


def hello_with_template(request):
    """Example of a simple template FBV"""

    context = {
        'current_time': datetime.now(),
    }

    return render(request, 'hello.html', context=context)


class HelloClassBased(TemplateView):
    """Example of a Class-based view"""
    template_name = 'hello.html'

    def get_context_data(self, **kwargs):
        return {
            'current_time': datetime.now(),
        }
