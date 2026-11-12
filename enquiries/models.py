from django.db import models

class Enquiry(models.Model):
    SERVICE_CHOICES = [
        ("Website development", "Website development"),
        ("Custom software", "Custom software"),
        ("Existing software improvement", "Existing software improvement"),
        ("AI / research collaboration", "AI / research collaboration"),
        ("Partnership or other enquiry", "Partnership or other enquiry"),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    organization = models.CharField(max_length=120, blank=True)
    service = models.CharField(max_length=60, choices=SERVICE_CHOICES, default="Website development")
    message = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    is_reviewed = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.service} ({self.created_at:%Y-%m-%d})"

class Project(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    summary = models.TextField()
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class OpenSourceProject(models.Model):

    division = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    repository_url = models.URLField()

    status = models.CharField(
        max_length=100,
        default="In Development"
    )

    is_published = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["division", "title"]

    def __str__(self):
        return self.title