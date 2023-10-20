from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import *
from .forms import *

#Create your views here.
def index(request):
    student_active_portfolios = Student.objects.select_related('portfolio').all().filter(portfolio__is_active=True)
    print("active portfolio query set", student_active_portfolios)
    return render( request, 'portfolio_app/index.html', {'student_active_portfolios':student_active_portfolios})

def create_project(request, portfolio_id):
    form = ProjectForm()
    portfolio = Portfolio.objects.get(pk=portfolio_id)

    if request.method == 'POST':
        # Create a new dictionary with form data and portfolio_id
        project_data = request.POST.copy()
        project_data['portfolio_id'] = portfolio_id

        form = ProjectForm(project_data)
        if form.is_valid():
            # Save the form without committing to the database
            project = form.save(commit=False)
            # Set the portfolio relationship
            project.portfolio = portfolio
            project.save()

            # Redirect back to the portfolio detail page
            return redirect('portfolio-detail', portfolio_id)

    context = {'form': form}
    return render(request, 'portfolio_app/project_form.html', context)


# Def to delete a project
def deleteProject(request, project_id):

    project = get_object_or_404(Project, pk=project_id) # attempt to get the project, or return 404 if failed

    if request.method == "POST":
        if request.POST.get("confirm") == "yes": # delete confirmation and redirect to portfolio detail page

            project.delete()
            return redirect("portfolio-detail", pk=project.portfolio.pk)

        elif request.POST.get("cancel") == "yes": # If the user cancels deletion, return to portfolio detail page
            return redirect("portfolio-detail", pk=project.portfolio.pk)

    return render(request, "portfolio_app/project_delete.html", {"project": project}) # Confirmation if request is not POST


def updateProject(request, project_id):
    
    project = get_object_or_404(Project, pk=project_id) # get the project

    if request.method == "POST":
        
        form = ProjectForm(request.POST, instance=project)
        
        if form.is_valid(): # if form is valid, save new update and redirect to portfolio detail page
            
            form.save()
            return redirect("portfolio-detail", pk=project.portfolio.pk)
    else:
        # If HTTP method is not POST, create a form with the current project data
        form = ProjectForm(instance=project)

        return render(request, "portfolio_app/project_update.html", {"form": form, "project": project})


def updatePortfolio(request, student_id):
    
    student = get_object_or_404(Student, pk=student_id) # get student and associated portfolio
    portfolio = student.portfolio

    if request.method == "POST":
       
        form = PortfolioForm(request.POST, instance=portfolio)
        if form.is_valid():
            
            form.save() # if valid, save new update and redirect to student page
            return redirect("student-detail", pk=student_id)
    else:
        # Create a form with the existing portfolio data
        form = PortfolioForm(instance=portfolio)

    return render(
        request, "portfolio_app/portfolio_form.html", {"form": form, "student": student}
    )

class StudentListView(generic.ListView):
    model = Student
class StudentDetailView(generic.DetailView):
    model = Student
class PortfolioListView(generic.ListView):
    model = Portfolio
class PortfolioDetailView(generic.DetailView):
    model = Portfolio

    def get_context_data(self, **kwargs):
        context = super(PortfolioDetailView, self).get_context_data(**kwargs)
        projects = Project.objects.filter(portfolio_id=self.object)
        context["projects"] = projects
        return context
    
class ProjectListView(generic.ListView):
    model = Project
class ProjectDetailView(generic.DetailView):
    model = Project