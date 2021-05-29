from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def onlinewriting(request):
    projects = Project.objects.all()
    projects_ = [
        {
            'id': project.id,
            'posted_by': project.posted_by,
            'project_name': project.project_name,
            'topic': project.topic,
            'subject': project.subject,
            'description': project.description,
            'pages': project.pages,
            'files': project.files.all(),
            'cost': project.cost,
            'due_date': project.due_date,
            'posted_on': project.posted_on,
            'status': project.status,
            'bidders': project.bidders.all(),
            'winning_bidder': project.winner_bidder,
            'is_assigned': project.is_assigned,
            'expires_on': project.expires_on
        } for project in projects
    ]

    for project in projects_:
        print(project)

    context = {
        'page': 'onlinewriting',
        'projects': projects_
    }
    return render(request, template_name='user/onlinewriting/onlinewriting.html', context=context)


def onlinewriting_post_project(request):
    if request.method == 'POST':
        user = request.user
        project = 2
        files = request.FILES.getlist('files')
        project = Project.objects.get(project_name='Web development')
        for f in files:
            file_instance = ProjectFile(file=f, project=project)
            file_instance.save()
            project.files.add(file_instance)

        messages.success(request, 'You have successfully added files to your project')
        return redirect('post_project')
    return render(request, template_name='user/onlinewriting/postproject.html', context={})


def onlinewriting_orders_pending(request):
    return render(request, template_name='user/onlinewriting/orders-pending.html', context={'page': 'orders_pending'})


def onlinewriting_orders_completed(request):
    return render(request, template_name='user/onlinewriting/orders-completed.html',
                  context={'page': 'orders_completed'})


def onlinewriting_orders_revisions(request):
    return render(request, template_name='user/onlinewriting/orders-revisions.html',
                  context={'page': 'orders_revisions'})


def onlinewriting_orders_rated(request):
    return render(request, template_name='user/onlinewriting/orders-rated.html', context={'page': 'orders_rated'})


def onlinewriting_orders_feedback(request):
    return render(request, template_name='user/onlinewriting/orders-feedback.html', context={'page': 'orders_feedback'})


def onlinewriting_payments_history(request):
    return render(request, template_name='user/onlinewriting/payments-history.html', context={'page': 'payments_history'})


def onlinewriting_payments_bonuses(request):
    return render(request, template_name='user/onlinewriting/payments-bonuses.html', context={'page': 'payments_bonuses'})


def onlinewriting_payments_upcoming(request):
    return render(request, template_name='user/onlinewriting/payments-upcoming.html', context={'page': 'payments_upcoming'})
