import uuid
from django.contrib.auth.models import User
from django.db import models

business_field = (
    ('B', 'Branding'),
    ('L', 'Leads'), ('BU', 'Brand unlead'))


class Requirements(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    si_no = models.IntegerField()
    month = models.CharField(max_length=50, null=False)
    business_type = models.CharField(max_length=100, choices=business_field, null=False)
    posters = models.CharField(max_length=60, null=False)
    followers = models.IntegerField()
    leads = models.IntegerField()
    likes = models.IntegerField()
    budget = models.IntegerField()
    page_id = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.id


class Report(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    req = models.ForeignKey(Requirements, on_delete=models.CASCADE)
    si_no = models.IntegerField()
    month = models.CharField(unique=True, max_length=200, null=False)
    business_type = models.CharField(max_length=100, null=False)
    posters = models.CharField(max_length=60, null=False)
    followers = models.IntegerField()
    leads = models.IntegerField()
    likes = models.IntegerField()
    feedback = models.CharField(max_length=200)
    page_id = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.id


class LeadsManagement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lead_name = models.CharField(max_length=200, null=False)
    company = models.CharField(max_length=200, null=False)
    email = models.EmailField()
    phone = models.IntegerField()
    lead_source = models.CharField(max_length=250)
    lead_owner = models.OneToOneField(User, on_delete=models.CASCADE)


