from django.shortcuts import render, redirect
from django.urls import reverse
from .models import TBL_Usuario, TBL_Video
from .forms import UserForm, VideoForm


def index(request):
    videos = TBL_Video.objects.all()
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            payroll = form.cleaned_data["payroll"]
            name = form.cleaned_data["name"]
            quantity = form.cleaned_data["quantity"]

            user = TBL_Usuario(payroll=payroll, name=name)
            user.save()

            # Redirige a la vista videos enviando el número de videos a subir
            return redirect(reverse("videos:videos", kwargs={"quantity": quantity}))

    return render(request, "videos/index.html", {"form": form, "videos": videos})


def videos(request, quantity):
    quantity = int(quantity)  # Asegúrate de que quantity sea un entero

    form = VideoForm()
    if request.method == "POST":
        form = VideoForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            extension = form.cleaned_data["extension"]
            size = form.cleaned_data["size"]

            video = TBL_Video(name=name, extension=extension, size=size)
            video.save()

            # Restamos 1 al quantity
            quantity -= 1

            if quantity <= 0:
                # Si ya no hay más videos por subir, redirige a la página de éxito
                return redirect("videos:index")
            else:
                # Si aún quedan videos por subir, redirige a la vista videos con el nuevo quantity
                return redirect(reverse("videos:videos", kwargs={"quantity": quantity}))

    return render(request, "videos/videos.html", {"form": form, "quantity": quantity})
