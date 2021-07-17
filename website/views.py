from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse, response
import socket

from posts.models import Post

from .forms import UserRegistrationForm


def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect("/")
    else:
        form = UserRegistrationForm()
    return render(request, "registration/signup.html", {"form": form})


def get_visitor_details(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if(x_forwarded_for):
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    try:
        socket.inet_aton(ip)
        ip_valid = True
    except socket.error:
        ip_valid: False
    return ip, ip_valid

def get_geolocation_details(ip):
    import geoip2.database

    reader = geoip2.database.Reader('./GeoLite2-City_20210629/GeoLite2-City.mmdb')
    response = reader.city(ip)

    print("**** Ip Details *****************")
    print(response.country.iso_code)
    print(response.country.name)
    print(response.country.names['zh-CN'])
    print(response.subdivisions.most_specific.name)
    print(response.subdivisions.most_specific.iso_code)
    print(response.city.name) 
    print(response.postal.code)
    print(response.location.latitude) 
    print(response.location.longitude)
    print("**** End of Details *****************")

    reader.close() 


def welcome(request):
    ip, ip_valid = get_visitor_details(request)
    # get_geolocation_details('189.252.180.66')
    # get_geolocation_details('197.210.79.191')
    return render(
        request,
        "website/welcome.html",
        {
            "posts": Post.objects.all(),
            "count": Post.objects.count(),
            "ip": {"address":ip, "is_valid": ip_valid}
        }
    )
