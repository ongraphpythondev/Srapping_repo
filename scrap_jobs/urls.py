from django.urls import path
from .views import ScrapJobs
urlpatterns= [
    path('scrap_times/', ScrapJobs.as_view())
]