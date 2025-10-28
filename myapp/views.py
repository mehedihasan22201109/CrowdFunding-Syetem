from .models import Purchase
from django.db.models import Sum





from users.models import CustomUser


from .models import event


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.db import models


def home(request):
    return render(request, template_name="myapp/home.html")


def about(request):
    return render(request, template_name="myapp/about.html")


def help(request):
    return render(request, template_name="help.html")


def event_list(request):
    q = request.GET.get("q", "")
    if q:
        events = event.objects.filter(
            models.Q(event_name__icontains=q) | models.Q(description__icontains=q)
        )
    else:
        events = event.objects.all()
    context = {"events": events}
    return render(request, template_name="myapp/all_events.html", context=context)


def event_details(request, id):
    event_obj = get_object_or_404(event, id=id)
    return render(request, "myapp/details_event.html", {"event": event_obj})


def upload_event(request):
    form = eventForm()
    if request.method == "POST":
        form = eventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("all_events")
    context = {"form": form}
    return render(request, template_name="myapp/event_form.html", context=context)


def update_event(request, id):
    event_obj = event.objects.get(pk=id)
    form = eventForm(instance=event_obj)
    if request.method == "POST":
        form = eventForm(request.POST, request.FILES, instance=event_obj)
        if form.is_valid():
            form.save()
            return redirect("all_events")
    context = {"form": form}
    return render(request, template_name="myapp/event_form.html", context=context)


def delete_event(request, id):
    event_obj = event.objects.get(pk=id)
    if request.method == "POST":
        event_obj.delete()
        return redirect("all_events")
    return render(request, template_name="myapp/delete_event.html")


def purchase_event(request, event_id):
    event_obj = get_object_or_404(event, id=event_id)
    if request.method == "POST":
        if request.user.is_authenticated:
            from .models import Purchase

            amount = request.POST.get("amount")
            if amount:
                from decimal import Decimal

                amount = Decimal(amount)
                Purchase.objects.create(
                    user=request.user,
                    event=event_obj,
                    amount=amount,
                )
                # Update event's total_donated
                event_obj.total_donated += amount
                event_obj.save()
                return redirect("profile")
    amount_needed = event_obj.Amount - event_obj.total_donated
    return render(request, "donation.html", {"event": event_obj, "amount_needed": amount_needed})


def contact(request):
    return render(request, "contact.html")


def campaign_creator_list(request):
    creators = CustomUser.objects.filter(user_type="campaign_creator")
    return render(request, "Auth/campaign_creator.html", {"campaign_creators": creators})


def top_donar_list(request):
    # Aggregate total donated amount per user
    top_donars = (
        CustomUser.objects.filter(purchases__isnull=False)
        .annotate(total_donated=Sum("purchases__amount"))
        .order_by("-total_donated")[:10]
    )
    return render(request, "Auth/TopDonar.html", {"top_donars": top_donars})