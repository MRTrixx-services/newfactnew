from django.urls import path
from .views import (
    home_view,
    services_view,
    projects_view,
    project_detail_view,
    social_services_view,
    social_service_detail_view,contact_view
)

urlpatterns = [

    path('', home_view, name='home'),

    path('services/', services_view, name='services'),

    path('projects/', projects_view, name='projects'),

    path('projects/<slug:slug>/', project_detail_view, name='project_detail'),

    path('social-services/', social_services_view, name='social_services'),

    path('social-services/<slug:slug>/', social_service_detail_view, name='social_service_detail'),

    path(
    'contact/',
    contact_view,
    name='contact'
),

]