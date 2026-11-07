from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Enquiry",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("organization", models.CharField(blank=True, max_length=120)),
                ("service", models.CharField(choices=[("Website development", "Website development"), ("Custom software", "Custom software"), ("Existing software improvement", "Existing software improvement"), ("AI / research collaboration", "AI / research collaboration"), ("Partnership or other enquiry", "Partnership or other enquiry")], default="Website development", max_length=60)),
                ("message", models.TextField(max_length=5000)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("is_reviewed", models.BooleanField(default=False)),
            ],
            options={"ordering": ["-created_at"]},
        ),
    ]
