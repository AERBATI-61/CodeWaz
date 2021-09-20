
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import *
from .forms import *

class indexView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'slider': Slider.objects.all()[:1],
            'projects': Project.objects.all()[:6],
            'services': Service.objects.all()[:6],
            'rises': Rise.objects.all()[:3],
            "risejobs": RiseJob.objects.all()[:3],
            'ourdetails': OurDetail.objects.all()[:1],
        }
        return render(request, 'codes/index.html', context)

    def post(self, request):
        form = ContactForm(request.POST or None)
        if form.is_valid():
            c_form = form.save(commit=False)
            c_form.save()
            return redirect('index')
        else:
            print(form.errors)



