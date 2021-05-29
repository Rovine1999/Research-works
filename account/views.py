from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user
from django.contrib import messages
from .forms import *

import pytz


@unauthenticated_user
def account_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Login failed! Check your username and password.')
            return render(request, template_name='user/account/login.html', context={'page': 'login'})

    return render(request, template_name='user/account/login.html', context={'page': 'login'})


def account_signup(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if password == password1:
            try:
                user1 = User.objects.get(username=username)
            except ObjectDoesNotExist:
                user1 = None
            try:
                user2 = User.objects.get(email=email)
            except ObjectDoesNotExist:
                user2 = None

            try:
                if user1 or user2:
                    context = {'page': 'signup',
                               'error': 'signup failed',
                               'fname': fname,
                               'lname': lname,
                               'email': email,
                               'username': username
                               }
                    messages.error(request, 'A user with this username or email already exists')
                    return render(request, template_name='user/account/signup.html', context=context)
                else:
                    user = User.objects.create_user(username=username, email=email)
                    # if validate_pa
                    user.set_password(password)
                    user.first_name = fname
                    user.last_name = lname
                    res = user.save()
                    messages.success(request, 'You successfully signed up. You can now login!')
                    return render(request, template_name='user/account/login.html', context={'page': 'login'})

            except ValidationError:
                messages.error(request, 'Password error, it should contain atleast 8 character, should not match your username, and should contain letters, characters and numbers')
                context = {'page': 'signup',
                           'error': 'signup failed',
                           'fname': fname,
                           'lname': lname,
                           'email': email,
                           'username': username
                           }
                return render(request, template_name='user/account/signup.html', context=context)

    return render(request, template_name='user/account/signup.html', context={'page': 'signup'})


def account_logout(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def account_change_profile_pic(request):
    if request.method == 'POST':
        userp = request.user.userprofile
        pic = request.FILES.get('profile_photo')
        print(pic)
        userp.profile_photo = pic
        userp.save()
        messages.success(request, 'You have successfully changed your profile picture')
        return redirect('profile')


@login_required(login_url='login')
def account_change_password(request):
    if request.method == 'POST':
        user = request.user
        old_pass = request.POST.get('old_password')
        new_pass = request.POST.get('new_password')
        new_pass_repeat = request.POST.get('new_password_repeat')
        if user.check_password(old_pass):
            if new_pass == new_pass_repeat:
                try:
                    pass_validate = validate_password(new_pass, user=None, password_validators=None)
                    if pass_validate is None:
                        user.set_password(new_pass)
                        messages.success(request, 'Password change was successful')
                        return redirect('profile')
                except ValidationError:
                    messages.error(request,
                                   'The new password you entered does not meet the minimum requirements(8 characters minimum, should contain numbers, and characters)')
                    return redirect('profile')
            else:
                messages.error(request, 'Passwords do not match')
                return redirect('profile')
        else:
            messages.error(request, 'The old password you gave is incorrect')
            return redirect('profile')


@login_required(login_url='login')
def account_profile(request):
    skills = request.user.userprofile.skills or 'no skills'
    specialities = request.user.userprofile.specialities or 'no specialities'
    skills_array = []
    specialities_array = []

    for skill in skills.split(','):
        skills_array.append(skill)

    for speciality in specialities.split(','):
        specialities_array.append(speciality)

    context = {
        'page': 'profile',
        'skills': skills_array,
        'specialities': specialities_array
    }

    return render(request, template_name='user/account/profile.html', context=context)


@login_required(login_url='login')
def account_edit_profile(request):

    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        # password = request.POST.get('password')
        # password1 = request.POST.get('password1')

        address = request.POST.get('address')

        postal_code = request.POST.get('postal_code')
        city = request.POST.get('city')
        phone_number = request.POST.get('phone_number')
        alt_phone_number = request.POST.get('alt_phone_number')

        sec_email = request.POST.get('sec_email')
        prof_field = request.POST.get('prof_field')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        skills = request.POST.get('skills')
        specialities = request.POST.get('specialities')
        bio = request.POST.get('bio')
        timezone = request.POST.get('timezone')

        web = request.POST.get('web')
        facebook = request.POST.get('facebook')
        twitter = request.POST.get('twitter')
        instagram = request.POST.get('instagram')
        github = request.POST.get('github')

        user = request.user

        if user:
            user.first_name = fname
            user.last_name = lname
            user.email = email
            user.username = username
            user.save()

            user.userprofile.address = address
            user.userprofile.postal_code = postal_code
            user.userprofile.city = city
            user.userprofile.phone_number = phone_number
            user.userprofile.alt_phone_number = alt_phone_number
            user.userprofile.secondary_email = sec_email
            user.userprofile.skills = skills
            user.userprofile.specialities = specialities
            user.userprofile.professional_field = prof_field
            # user.userprofile.bio = bio
            user.userprofile.age = age
            user.userprofile.gender = gender
            # user.userprofile.time_zone = timezone
            user.userprofile.set_timezone(timezone)
            user.userprofile.set_bio(bio)

            user.userprofile.personal_website = web
            user.userprofile.facebook = facebook
            user.userprofile.twitter = twitter
            user.userprofile.instagram = instagram
            user.userprofile.github = github

            user.userprofile.save()

        return redirect('profile')

    return render(request, template_name='user/account/editprofile.html', context={'page': 'editprofile', 'timezones': pytz.common_timezones})
