from django.db import models
import uuid
from django.contrib.auth.models import User


def generate_ticket_no():
    return "TCKT-" + uuid.uuid4().hex[:8].upper()


class Ticket(models.Model):
    ticket_no = models.CharField(
        max_length=20,
        unique=True,
        default=generate_ticket_no,
        editable=False
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    issue_type = models.CharField(max_length=100)
    priority = models.CharField(max_length=20)

    tat_deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=20, default="Open")
    problem_solver = models.CharField(max_length=100, null=True, blank=True)
    solution_provided = models.TextField(null=True, blank=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.ticket_no


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class DashboardUser(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    department = models.CharField(max_length=100, blank=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.email




