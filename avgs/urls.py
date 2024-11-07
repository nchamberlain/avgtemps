from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("daily/<int:id>", views.daily, name="daily"),
    path('summary/<int:id>/', views.summary_view, name='summary'),
    path('report/<int:id>/', views.report_view, name='report'),
]