from django.db import models


class Applicant(models.Model):
    ROLE_CHOICES = [
        ('Intern', 'Intern'),
        ('Volunteer', 'Volunteer'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    reason = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.role})"
