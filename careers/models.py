from django.db import models

# Create your models here.
from django.db import models


class CareerHero(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    background_image = models.ImageField(upload_to='career_hero/')

    def __str__(self):
        return self.title


class WhyJoinUs(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title


class JobOpening(models.Model):
    title = models.CharField(max_length=200)

    department = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    location = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    experience = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    salary = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    description = models.TextField()

    skills = models.TextField(
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Internship(models.Model):
    title = models.CharField(max_length=200)

    duration = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    stipend = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    description = models.TextField()

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class CompanyCulture(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='culture/')

    def __str__(self):
        return self.title


class HRContact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.email


class CareerApplication(models.Model):
    job = models.ForeignKey(
        JobOpening,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    full_name = models.CharField(max_length=200)

    email = models.EmailField()

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    cover_letter = models.TextField(
        blank=True,
        null=True
    )

    resume = models.FileField(upload_to='resumes/')

    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name