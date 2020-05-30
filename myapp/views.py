from django.shortcuts import render
from django.views import View
from .models import SinhVien

# Create your views here.

def index(request):
    return render(request, 'index.html')


class IndexView(View):


    def get(self, request):
        list_sv = SinhVien.objects.all()
        context = {
            'var1': 'nguyen trung phuc',
            'var2': 'nltt',
            'list_sv': list_sv
        }

        return render(request, 'index.html', context)