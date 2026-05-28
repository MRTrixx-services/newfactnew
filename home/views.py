from django.shortcuts import render, get_object_or_404
from .models import Slider, HomeContent
from django.shortcuts import render
from .models import (
    Slider,
    HomeContent,
    ServicePageIntro,
    Service
)

def home_view(request):

    sliders = Slider.objects.filter(is_active=True)

    content = HomeContent.objects.first()

    featured_services = Service.objects.filter(
        is_featured=True
    )[:9]

    return render(request, 'home.html', {
        'sliders': sliders,
        'content': content,
        'featured_services': featured_services
    })


def services_view(request):

    intro = ServicePageIntro.objects.first()

    services = Service.objects.all()

    context = {
        'intro': intro,
        'services': services
    }

    return render(request, 'services.html', context)







from .models import (
    ProjectsPage,
    Project,
    SocialServicesPage,
    SocialService
)


def projects_view(request):

    page = ProjectsPage.objects.first()

    history_projects = Project.objects.filter(status='history')
    live_projects = Project.objects.filter(status='live')
    upcoming_projects = Project.objects.filter(status='upcoming')

    context = {
        'page': page,
        'history_projects': history_projects,
        'live_projects': live_projects,
        'upcoming_projects': upcoming_projects,
    }

    return render(request, 'projects.html', context)

def project_detail_view(request, slug):

    project = get_object_or_404(Project, slug=slug)

    return render(request, 'project_detail.html', {'project': project})

def social_services_view(request):

    page = SocialServicesPage.objects.first()

    history = SocialService.objects.filter(status='history')
    ongoing = SocialService.objects.filter(status='ongoing')
    upcoming = SocialService.objects.filter(status='upcoming')

    context = {
        'page': page,
        'history': history,
        'ongoing': ongoing,
        'upcoming': upcoming,
    }

    return render(request, 'social_services.html', context)

def social_service_detail_view(request, slug):

    service = get_object_or_404(SocialService, slug=slug)

    return render(request, 'social_service_detail.html', {'service': service})

def contact_view(request):

    return render(
        request,
        'contact.html'
    )