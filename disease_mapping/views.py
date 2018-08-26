from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Disease


def index(request):

    disease_list = Disease.objects.order_by('doid')

    context = {
        # 'disease_list': diseases,
        'disease_list': disease_list,
    }

    return render(request, 'disease_mapping/index.html', context)


class DiseaseListView(ListView):
    model = Disease
    # context_object_name = disease_list


class DiseaseDetailView(DetailView):
    model = Disease
