from django.shortcuts import render

from users.models import AppUser

def dashboard(request):
    app_user = AppUser.objects.get(user=request.user)
    context = {
        'events': app_user.events.all()
    }
    return render(request,'dashboard.html',context)
