from django.http import HttpResponse


def robots_txt(request):
    content = """User-agent: *
Allow: /

Disallow: /admin/

Sitemap: https://newfactengineering.com/sitemap.xml
"""
    return HttpResponse(content, content_type="text/plain")


def llms_txt(request):
    content = """# New Fact Engineering

> BIM modeling, VDC coordination, engineering and shop drawing services for AEC firms.

## Main Pages

- https://newfactengineering.com/
- https://newfactengineering.com/services/
- https://newfactengineering.com/projects/
- https://newfactengineering.com/social-services/
- https://newfactengineering.com/contact/
- https://newfactengineering.com/careers/

## Services

Explore the services page for the currently published BIM and engineering services.

## Contact

https://newfactengineering.com/contact/
"""
    return HttpResponse(content, content_type="text/plain; charset=utf-8")