from django.shortcuts import render, redirect

from .models import (
    CareerHero,
    WhyJoinUs,
    JobOpening,
    Internship,
    CompanyCulture,
    HRContact,
    CareerApplication,
)


def careers_view(request):

    hero = CareerHero.objects.first()

    why_join = WhyJoinUs.objects.all()

    jobs = JobOpening.objects.filter(
        is_active=True
    ).order_by('-created_at')

    internships = Internship.objects.filter(
        is_active=True
    )

    cultures = CompanyCulture.objects.all()

    hr_contact = HRContact.objects.first()

    if request.method == "POST":

        job_id = request.POST.get('job')

        job = None

        if job_id:
            try:
                job = JobOpening.objects.get(id=job_id)
            except:
                job = None

        CareerApplication.objects.create(
            job=job,
            full_name=request.POST.get('full_name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            cover_letter=request.POST.get('cover_letter'),
            resume=request.FILES.get('resume'),
        )

        return redirect('careers')

    context = {
        'hero': hero,
        'why_join': why_join,
        'jobs': jobs,
        'internships': internships,
        'cultures': cultures,
        'hr_contact': hr_contact,
    }

    return render(request, 'careers.html', context)