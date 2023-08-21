from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('insert', views.insertData, name="insertData"),
    path('add_review/<int:pk>/', views.add_review, name='add_review'),  # Add this line
]
    # path('add_review/<int:pk>/', add_review, name='add_review'),
    # path('update/<int:id>', views.updateData, name="updateData"),
    # path('delete/<int:id>', views.deleteData, name="deleteData"),


