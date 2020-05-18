from django.shortcuts import render
from django.views import View


def index(request):
    return render(request, 'frontend/index.html')


class NewArrival(View):
    template_name = 'frontend/new_arrivals.html'

    def get(self, request):
        print(request.GET)
        return render(request, 'frontend/new_arrivals.html', context={})