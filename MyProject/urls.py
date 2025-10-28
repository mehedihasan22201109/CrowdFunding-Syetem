from . import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include  # <-- add include
from users import views as userviews
from myapp import views as myviews


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", myviews.home, name="home"),
    path("about/", myviews.about, name="about"),
    path("events/", myviews.event_list, name="all_events"),
    path("events_details/<str:id>", myviews.event_details, name="event_details"),
    path("upload/", myviews.upload_event, name="upload_event"),
    path("update/<str:id>", myviews.update_event, name="update_event"),
    path("delete/<str:id>", myviews.delete_event, name="delete"),
    path("login/", userviews.login_view, name="login"),
    path("signup/", userviews.register_view, name="signup"),
    path("welcome/", userviews.welcome_view, name="welcome"),
    path("users/", include("users.urls")),
    path("help/", myviews.help, name="help"),
    path("purchase/<int:event_id>/", myviews.purchase_event, name="purchase_event"),
    path("contact/", myviews.contact, name="contact"),
    path("campaign_creators/", myviews.campaign_creator_list, name="campaign_creator_list"),
    path("top_donars/", myviews.top_donar_list, name="top_donar_list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
