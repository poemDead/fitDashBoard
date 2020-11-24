from django.http import HttpResponse
from django.shortcuts import render

from .models import WeightRecords
from django.template import loader
# Create your views here.
def index(request):
    records = WeightRecords.objects.all()
    output = '; '.join(str(r.weight) for r in records)

    template = loader.get_template('bodytracker/index.html')
    context = {
        'records': records,
    }
    return HttpResponse(template.render(context,request))
    #return render(request, 'index.html',)