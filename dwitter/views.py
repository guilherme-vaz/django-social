from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Dweet, Profile
from .forms import DweetForm
from django.shortcuts import render, redirect

def dashboard(request):
    form = DweetForm(request.POST or None)
    if request.method == 'POST':
         if form.is_valid():
              #Cria um dweet com as informações passadas pelo form
              dweet = form.save(commit=False)
              #Associa o usuário logado ao Dweet
              dweet.user = request.user
              #Salva o dweet
              dweet.save()
              return redirect("dwitter:dashboard")
         
    followed_dweets = Dweet.objects.filter(

        user__profile__in=request.user.profile.follows.all()

    ).order_by("-created_at")

    return render(request, 'dwitter/dashboard.html', {"form": form, "dweets":followed_dweets})

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "dwitter/profile_list.html", {"profiles": profiles})

def profile(request, pk):
    # Verifica se NÃO tem profile criado, se não tiver cria um 
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        # Pega o user atual
        current_user_profile = request.user.profile
        # Pega o que está sendo enviado pelo form do Front
        data = request.POST 
        # Pega o name passado nos buttons
        action = data.get("follow")

        if action == "follow":
                current_user_profile.follows.add(profile)
        elif action == "unfollow":
             current_user_profile.follows.remove(profile)
        current_user_profile.save()

    return render(request, "dwitter/profile.html", {"profile": profile})