from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.StudentListView.as_view(), name= 'students'),
    path('student/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
    path('portfolio/', views.PortfolioListView.as_view(), name= 'portfolio'),
    path('portfolio/<int:pk>', views.PortfolioDetailView.as_view(), name='portfolio-detail'),
    path('projects/', views.ProjectListView.as_view(), name= 'projects'),
    path('project/<int:pk>', views.ProjectDetailView.as_view(), name= 'project-detail'),
    path('portfolio/<int:portfolio_id>/create_project/', views.create_project, name='create_project'),
    path("portfolio/project/<int:project_id>/delete/", views.deleteProject, name="delete_project"),
    path("projects/<int:project_id>/update/", views.updateProject, name="update-project"),
    path("student/<int:student_id>/update_portfolio/", views.updatePortfolio, name="update-portfolio"),


]   