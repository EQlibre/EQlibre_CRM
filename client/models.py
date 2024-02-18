from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from team.models import Team
from core.models import Address, Org
from django.utils.translation import gettext_lazy as _
from core.utils import COUNTRIES


class Client(models.Model):
    team = models.ForeignKey(Team, related_name='clients', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=3, choices=COUNTRIES, blank=True, null=True)
    organization = models.CharField(_("Organization"), max_length=255, null=True)
    title = models.CharField(_("Title"), max_length=255, default="", blank=True)
    email = models.EmailField()
    mobile_number = PhoneNumberField(null=True, unique=True)
    do_not_call = models.BooleanField(default=False)
    address = models.ForeignKey(
        Address,
        related_name="adress_clients",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    department = models.CharField(_("Department"), max_length=255, null=True)
    language = models.CharField(_("Language"), max_length=255, null=True)
    description = models.TextField(blank=True, null=True)
    linked_in_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Comment(models.Model):
    team = models.ForeignKey(Team, related_name='client_comments', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='client_comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.created_by.username


class ClientFile(models.Model):
    team = models.ForeignKey(Team, related_name='client_files', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='clientfiles')
    created_by = models.ForeignKey(User, related_name='client_files', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.created_by.username
