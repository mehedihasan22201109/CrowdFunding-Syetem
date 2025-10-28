from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    # ... other url patterns ...
    path("profile/", views.profile, name="profile"),
    path("history/", views.history, name="history"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("varify/", TemplateView.as_view(template_name="Auth/varify.html"), name="varify"),
    path("massage/", TemplateView.as_view(template_name="Auth/massage.html"), name="massage"),
    path("donarlist/", views.donarlist, name="donarlist"),
]
