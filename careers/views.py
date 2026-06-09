from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.timezone import localtime, now
from django.conf import settings

from .models import (
    CareerHero,
    WhyJoinUs,
    JobOpening,
    Internship,
    CompanyCulture,
    HRContact,
    CareerApplication,
)


def send_career_emails(application, job):
    applied_on = localtime(application.applied_at).strftime("%d %B %Y, %I:%M %p")
    job_title  = job.title if job else "General Application"

    ctx = {
        'full_name'   : application.full_name,
        'email'       : application.email,
        'phone'       : application.phone,
        'cover_letter': application.cover_letter,
        'job_title'   : job_title,
        'applied_on'  : applied_on,
    }

    # ── ADMIN EMAIL ──────────────────────────────────────────
    admin_html = render_to_string('emails/admin_notification.html', ctx)
    admin_mail = EmailMultiAlternatives(
        subject=f"[New Application] {application.full_name} applied for {job_title}",
        body=f"New application from {application.full_name} for {job_title}. Check admin panel.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[settings.DEFAULT_FROM_EMAIL],
    )
    admin_mail.attach_alternative(admin_html, "text/html")

    if application.resume:
        try:
            application.resume.open('rb')
            admin_mail.attach(
                application.resume.name.split('/')[-1],
                application.resume.read(),
                'application/octet-stream',
            )
            application.resume.close()
        except Exception:
            pass

    admin_mail.send(fail_silently=True)

    # ── USER CONFIRMATION EMAIL ───────────────────────────────
    user_html = render_to_string('emails/user_confirmation.html', ctx)
    user_mail = EmailMultiAlternatives(
        subject=f"Application Received — {job_title} | New Fact Engineering",
        body=(
            f"Dear {application.full_name},\n\n"
            f"Your application for '{job_title}' has been received. "
            f"We will contact you shortly.\n\n"
            f"Best Regards,\nNew Fact Engineering"
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[application.email],
    )
    user_mail.attach_alternative(user_html, "text/html")
    user_mail.send(fail_silently=True)


def careers_view(request):

    hero       = CareerHero.objects.first()
    why_join   = WhyJoinUs.objects.all()
    jobs       = JobOpening.objects.filter(is_active=True).order_by('-created_at')
    internships = Internship.objects.filter(is_active=True)
    cultures   = CompanyCulture.objects.all()
    hr_contact = HRContact.objects.first()

    if request.method == "POST":

        full_name    = request.POST.get('full_name', '').strip()
        email        = request.POST.get('email', '').strip()
        phone        = request.POST.get('phone', '').strip()
        cover_letter = request.POST.get('cover_letter', '').strip()
        job_id       = request.POST.get('job', '').strip()
        resume_file  = request.FILES.get('resume')

        # ── SERVER-SIDE VALIDATION ─────────────────────────────
        errors = []

        if not full_name or len(full_name) < 2:
            errors.append("Full name must be at least 2 characters.")

        if not email or '@' not in email or '.' not in email.split('@')[-1]:
            errors.append("Please enter a valid email address.")

        if phone and not phone.replace('+', '').replace('-', '').replace(' ', '').isdigit():
            errors.append("Phone number must contain only digits, +, or -.")

        if not resume_file:
            errors.append("Please upload your resume.")
        else:
            allowed_ext = ['.pdf', '.doc', '.docx']
            fname = resume_file.name.lower()
            if not any(fname.endswith(ext) for ext in allowed_ext):
                errors.append("Resume must be a PDF, DOC, or DOCX file.")
            if resume_file.size > 5 * 1024 * 1024:
                errors.append("Resume file size must not exceed 5MB.")

        if errors:
            for err in errors:
                messages.error(request, err)
            return redirect('careers')

        # ── SAVE APPLICATION ───────────────────────────────────
        job = None
        if job_id:
            try:
                job = JobOpening.objects.get(id=job_id)
            except JobOpening.DoesNotExist:
                pass

        application = CareerApplication.objects.create(
            job=job,
            full_name=full_name,
            email=email,
            phone=phone or None,
            cover_letter=cover_letter or None,
            resume=resume_file,
        )

        # ── SEND EMAILS ────────────────────────────────────────
        send_career_emails(application, job)

        messages.success(request, f"Thank you {full_name}! Your application has been submitted successfully. We'll be in touch soon.")
        return redirect('careers')

    context = {
        'hero'       : hero,
        'why_join'   : why_join,
        'jobs'       : jobs,
        'internships': internships,
        'cultures'   : cultures,
        'hr_contact' : hr_contact,
    }

    return render(request, 'careers.html', context)
