from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    protocol = "https"
    changefreq = "weekly"

    def items(self):
        return [
            "home",
            "services",
            "projects",
            "social_services",
            "contact",
            "careers",
        ]

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        priorities = {
            "home": 1.0,
            "services": 0.9,
            "projects": 0.8,
            "social_services": 0.7,
            "contact": 0.7,
            "careers": 0.6,
        }
        return priorities.get(item, 0.5)


class CareerSitemap(Sitemap):
    protocol = "https"
    priority = 0.6
    changefreq = "monthly"

    def items(self):
        return ["careers:careers"]

    def location(self, item):
        return reverse(item)