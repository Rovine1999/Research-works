from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import pre_save
from django.dispatch import receiver

from onlinewriting.utils import unique_order_id_generator


class Project(models.Model):
    posted_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL,
                                  related_name='project_posted_by')
    project_name = models.TextField(max_length=100, blank=True, null=True)
    topic = models.TextField(max_length=100, blank=True, null=True)
    subject = models.TextField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=10000, blank=True, null=True)
    pages = models.CharField(max_length=5, blank=True, null=True)
    files = models.ManyToManyField('ProjectFile', blank=True, null=True, related_name='project_files')
    cost = models.TextField(max_length=10, blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    posted_on = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, default='pending')
    bidders = models.ManyToManyField(User, blank=True, related_name='project_bidders')
    winner_bidder = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL,
                                      related_name='project_winner_bidder')
    is_assigned = models.BooleanField(default=False)
    expires_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.project_name}_{self.subject}"

    def setIsAssigned(self):
        self.is_assigned = True
        self.save()
        return self.is_assigned


class FreelanceOrder(models.Model):
    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.SET_NULL)
    ordered_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=30, default='pending')
    order_amount = models.CharField(max_length=30, blank=True, null=True)
    order_placed_on = models.DateTimeField()
    order_id = models.CharField(max_length=20, blank=True, null=True)

    @receiver(pre_save, sender='onlinewriting.FreelanceOrder')
    def pre_save_create_freelanceorder_order_id(sender, instance, *args, **kwargs):
        if not instance.order_id:
            instance.order_id = unique_order_id_generator(instance)

        pre_save.connect(FreelanceOrder, sender=instance)


class ProjectFile(models.Model):
    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.SET_NULL)
    file = models.FileField()
