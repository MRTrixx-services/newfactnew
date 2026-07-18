from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
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
    )[:12]

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

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.timezone import localtime, now
from django.conf import settings
from .models import ContactMessage


def send_contact_emails(msg):
    submitted_on = localtime(msg.submitted_at).strftime("%d %B %Y, %I:%M %p")
    ctx = {
        'name': msg.name,
        'email': msg.email,
        'subject': msg.subject,
        'message': msg.message,
        'submitted_on': submitted_on,
    }

    # ── ADMIN EMAIL ──────────────────────────────────────────
    admin_html = render_to_string('emails/contact_admin.html', ctx)
    admin_mail = EmailMultiAlternatives(
        subject=f"[Contact] {msg.name} — {msg.subject}",
        body=f"New contact message from {msg.name} ({msg.email}): {msg.subject}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[settings.DEFAULT_FROM_EMAIL],
    )
    admin_mail.attach_alternative(admin_html, "text/html")
    admin_mail.send(fail_silently=True)

    # ── USER CONFIRMATION EMAIL ───────────────────────────────
    user_html = render_to_string('emails/contact_user.html', ctx)
    user_mail = EmailMultiAlternatives(
        subject=f"We received your message — New Fact Engineering",
        body=(
            f"Dear {msg.name},\n\n"
            f"Thank you for contacting us. We have received your message and will get back to you shortly.\n\n"
            f"Best Regards,\nNew Fact Engineering"
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[msg.email],
    )
    user_mail.attach_alternative(user_html, "text/html")
    user_mail.send(fail_silently=True)


def contact_view(request):

    if request.method == 'POST':
        name    = request.POST.get('name', '').strip()
        email   = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        errors = []
        if not name or len(name) < 2:
            errors.append("Please enter your full name.")
        if not email or '@' not in email or '.' not in email.split('@')[-1]:
            errors.append("Please enter a valid email address.")
        if not subject:
            errors.append("Please enter a subject.")
        if not message or len(message) < 10:
            errors.append("Message must be at least 10 characters.")

        if errors:
            for err in errors:
                messages.error(request, err)
            return redirect('contact')

        msg = ContactMessage.objects.create(
            name=name, email=email, subject=subject, message=message
        )
        send_contact_emails(msg)
        messages.success(request, f"Thank you {name}! Your message has been sent. We'll get back to you shortly.")
        return redirect('contact')

    return render(request, 'contact.html')
