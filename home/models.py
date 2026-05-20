from django.db import models
from ckeditor.fields import RichTextField


class Slider(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='slider/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title or "Slider Image"


class HomeContent(models.Model):
    content = RichTextField()

    def __str__(self):
        return "Home Page Content"



from django.db import models
from ckeditor.fields import RichTextField


# =========================
# SERVICES PAGE INTRO
# =========================
class ServicePageIntro(models.Model):

    left_content = RichTextField()
    center_image = models.ImageField(upload_to='services/intro/')
    right_content = RichTextField()

    def __str__(self):
        return "Services Page Intro"


# =========================
# SERVICES
# =========================    
class Service(models.Model):

    title = models.CharField(max_length=200)

    image = models.ImageField(upload_to='services/')

    description = RichTextField()

    bullet_points = models.TextField(
        help_text="Enter each point in new line"
    )

    is_featured = models.BooleanField(default=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    @property
    def bullet_list(self):
        return self.bullet_points.splitlines()

    def __str__(self):
        return self.title
    
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify


# =========================================
# PROJECTS PAGE HERO
# =========================================
class ProjectsPage(models.Model):

    title = models.CharField(
        max_length=200,
        default="PROJECTS"
    )

    hero_image = models.ImageField(
        upload_to='projects/hero/'
    )

    def __str__(self):
        return "Projects Page"


# =========================================
# PROJECT STATUS
# =========================================
PROJECT_STATUS = (
    ('history', 'Project History'),
    ('live', 'Live Projects'),
    ('upcoming', 'Upcoming Projects'),
)


# =========================================
# PROJECT MODEL
# =========================================
class Project(models.Model):

    title = models.CharField(max_length=250)

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    short_description = RichTextField()

    image = models.ImageField(
        upload_to='projects/'
    )

    status = models.CharField(
        max_length=20,
        choices=PROJECT_STATUS
    )

    project_date = models.DateField()

    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


# =========================================
# SOCIAL SERVICES PAGE HERO
# =========================================
class SocialServicesPage(models.Model):

    title = models.CharField(
        max_length=200,
        default="SOCIAL SERVICES"
    )

    hero_image = models.ImageField(
        upload_to='social_services/hero/'
    )

    def __str__(self):
        return "Social Services Page"


# =========================================
# SOCIAL SERVICE STATUS
# =========================================
SOCIAL_SERVICE_STATUS = (
    ('history', 'Service History'),
    ('ongoing', 'Ongoing Services'),
    ('upcoming', 'Upcoming Services'),
)


# =========================================
# SOCIAL SERVICE MODEL
# =========================================
class SocialService(models.Model):

    title = models.CharField(max_length=250)

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    short_description = RichTextField()

    image = models.ImageField(
        upload_to='social_services/'
    )

    status = models.CharField(
        max_length=20,
        choices=SOCIAL_SERVICE_STATUS
    )

    project_date = models.DateField()

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-project_date']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


