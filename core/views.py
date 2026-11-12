from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from enquiries.models import Project, OpenSourceProject

def home(request): return render(request, "pages/home.html", {"page_title": "Home"})
def services(request): return render(request, "pages/services.html", {"page_title": "Services"})
def divisions(request): return render(request, "pages/divisions.html", {"page_title": "Divisions & Initiatives"})
def projects(request):
    projects = Project.objects.all().order_by("created_at")
    open_source_projects = OpenSourceProject.objects.filter(
            is_published=True,
        )

    return render(request, "pages/projects.html", {
        "page_title": "Projects & Research",
        "projects": projects,
        "open_source_projects": open_source_projects
    })
def about(request): return render(request, "pages/about.html", {"page_title": "About"})
def privacy(request): return render(request, "pages/privacy.html", {"page_title": "Privacy Notice"})
def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)

    return render(request, "pages/project_detail.html", {
        "project": project,
        "page_title": project.title,
    })
