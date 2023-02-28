"""formProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .views import *
from django.urls import path

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('done', DoneView.as_view(), name='done'),
    path('list', ListFeedBack.as_view(), name='list'),
    path('detail/<int:pk>', DetailFeedBack.as_view(), name='detail_feedback'),
    path('update/<int:pk>', FeedBackViewUpdate.as_view(), name='feedbackUpdate'),
    path('delete/<int:pk>', FeedBackViewDelete.as_view(), name='feedbackUpdate'),
    path('addfeedback', index, name='add_feedback'),
    path('classBviews', FeedBackView.as_view()),
    path('<int:id_feedback>', FeedBackUpdateView.as_view()),
]
