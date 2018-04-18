from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Disease


def index(request):
    diseases = [
        {
            "name": "Systemic Lupus Erythematosus",
            "DOID": "DOID9034",
            "match_status": True,
        },
        {
            "name": "Systemic Lupine Ethemosuss",
            "DOID": "DOID1234",
            "match_status": False,
        },
        {
            "name": "Lupine Erythrisis",
            "DOID": "DOID4234",
            "match_status": False,
        },
        {
            "name": "Lupinedid Erythrsmousis",
            "DOID": "DOID8234",
            "match_status": False,
        },
    ]

    context = {
        'disease_list': diseases,
    }

    return render(request, 'disease_mapping/index.html', context)


class DiseaseListView(ListView):
    model = Disease
    # context_object_name = disease_list


class DiseaseDetailView(ListView):
    model = Disease
