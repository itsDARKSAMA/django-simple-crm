# Django Libs:
from django.urls import path
# Local Libs:
from . import views


urlpatterns = [
	path('',views.index ,name= 'index'),
	path('dashboard/', views.dashboard, name='dashboard'),
	path('new-record/', views.new_record, name='new-record'),
	path('view-record/<int:id>/',views.view_record,name='view-record'),
	path("edit-record/<int:id>/", views.edit_record, name="edit-record"),
	path("delete-record/<int:id>/", views.delete_record, name="delete-record"),
	path("search/", views.search, name="search")
]
