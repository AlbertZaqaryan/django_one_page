from django.shortcuts import render
from django.views.generic import ListView
from .models import Welcome, Category, OurWork, OurTeam


class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        category = Category.objects.all()
        welcome = Welcome.objects.all()
        ourteam = OurTeam.objects.all()
        ourwork = OurWork.objects.all()
        return render(request, self.template_name, {'category':category, 'welcome':welcome, 'ourteam':ourteam, 'ourwork':ourwork})