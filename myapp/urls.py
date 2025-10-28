from django.urls import path
from . import views
from . import views

urlpatterns = [
    # ... existing code ...
    path("top_donars/", views.top_donar_list, name="top_donar_list"),
    path("appoint/", views.appoint, name="appoint"),
    path("campaign_creators/", views.campaign_creator_list, name="campaign_creator_list"),
    # ... existing code ...
]
