from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.index), name='index'),

    path('add/', login_required(views.add), name='add'),

    path('delete/<int:empleado_id>/', login_required(views.delete), name='delete'),

    path('edit/<int:empleado_id>/', login_required(views.edit), name='edit')
]