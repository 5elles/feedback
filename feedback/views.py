from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import FeedbackForm
from .models import Feedback
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
import datetime


# Create your views here.

class FeedBackViewUpdate(UpdateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = '/done'

class FeedBackViewDelete(DeleteView):
    model = Feedback
    success_url = '/list'
    template_name = 'feedback/delete_feedback.html'

class FeedBackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = '/done'


# class FeedBackView(View):
#     def get(self, request):
#         form = FeedbackForm()
#         return render(request, 'feedback/feedback.html', context={'form': form})
#
#     def post(self, request):
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/done')
#         return render(request, 'feedback/feedback.html', context={'form': form})

class DoneView(TemplateView):
    template_name = 'feedback/done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = Feedback.objects.all().order_by('-id')[0].name
        context['date'] = datetime.datetime.now()
        return context


class FeedBackUpdateView(View):
    def post(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(request.POST, instance=feed)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/done')
        return render(request, 'feedback/feedback.html', context={'form': form})


    def get(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(instance=feed)
        return render(request, 'feedback/feedback.html', context={'form': form})

def index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/done')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback.html', context={'form': form})


class ListFeedBack(ListView):
    template_name = 'feedback/list_feedback.html'
    model = Feedback
    # context_object_name = 'feedbacks'

    def get_queryset(self):
        queryset = super().get_queryset()
        # filter_qs = queryset.filter(rating__gt=4)
        return queryset


class DetailFeedBack(DetailView):
    model = Feedback
    template_name = 'feedback/detail_feedback.html'
