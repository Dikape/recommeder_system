import datetime
from django.shortcuts import render, redirect, reverse
from recommender_system.settings import client_id, client_secret
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import FbInfo, FacebookTokens
from materials.models import Material, UserMark
import requests


def login_(request):
    code = request.GET.get('code')
    host = request.get_host()
    token = None
    if not code:
        redirect_uri = f"https://{host}{reverse('users:login')}"
        request_url = f'https://www.facebook.com/v3.2/dialog/oauth?client_id={client_id}&' \
            f'redirect_uri={redirect_uri}&' \
            f'scope=user_birthday, user_hometown, user_location, user_likes, ' \
            f'user_photos, user_videos, user_friends, user_status, user_tagged_places,' \
            f' user_posts, user_gender, user_link, user_age_range, email'
        return redirect(request_url)
    else:
        redirect_uri = f"https://{host}{reverse('users:login')}"
        request_url = f'https://graph.facebook.com/v3.2/oauth/access_token?client_id={client_id}&' \
            f'redirect_uri={redirect_uri}' \
            f'&client_secret={client_secret}' \
            f'&code={code}'
        r = requests.get(request_url)
        if r.status_code == 200:
            data = r.json()
            token = data['access_token']

    if token:
        user_info_url = f'https://graph.facebook.com/me?' \
            f'fields=id,address,age_range,birthday,first_name,gender,hometown,last_name,' \
            f'location,middle_name,likes,music,movies,television,favorite_athletes,favorite_teams,games,books' \
            f'&access_token={token}'
        user_info = requests.get(user_info_url)
        if user_info.status_code == 200:
            json_info = user_info.json()
            print(json_info)
            username = f"{json_info['first_name'].lower()}{json_info['last_name'].lower()}"
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = User(
                    username=username,
                    first_name=json_info['first_name'],
                    last_name=json_info['last_name'],
                    email=f'{username}@gmail.com',
                    date_joined=datetime.datetime.now()
                )
                user.set_password('11111')
                user.save()
                FbInfo.objects.create(
                    home_address=json_info['hometown']['name'],
                    home_address_lat=11.22,
                    home_address_lng=32.11,
                    location=json_info['location']['name'],
                    location_lat=23.4,
                    location_lng=52.1,
                    age=json_info['age_range']['min'],
                    gender=json_info['gender'],
                    user=user,
                    friends_count=42
                )
            try:
                token = FacebookTokens.objects.get(user=user)
            except FacebookTokens.DoesNotExist:
                FacebookTokens.objects.create(user=user, token=token)
            # user = authenticate(username=user.username, password=user.password)
            login(request, user)

    return redirect(reverse('users:profile'))


def logout_(request):
    logout(request)
    return redirect(reverse('materials:index'))


def profile(request):
    if request.user.is_authenticated:
        user_token = request.user.facebooktokens.token
        user_likes_url = f'https://graph.facebook.com/me?' \
            f'fields=likes,music,movies,television,favorite_athletes,favorite_teams,games,books' \
            f'&access_token={user_token}'
        likes_r = requests.get(user_likes_url)
        likes_list = []
        if likes_r.status_code == 200:
            for like_obj in likes_r.json()['movies']['data']:
                material = Material.objects.filter(title_original__contains=like_obj['name'][:15])
                if material:
                    try:
                        mark = UserMark.objects.get(user=request.user, material=material.first())
                    except UserMark.DoesNotExist:
                        mark = UserMark.objects.create(
                            user=request.user, material=material.first(), mark=5, is_from_fb=True)
                    likes_list.append(mark)

        context = {
            'user': request.user,
            'materials': likes_list
        }
        return render(request, 'users/profile.html', context=context)
    else:
        return redirect(reverse('materials:index'))
