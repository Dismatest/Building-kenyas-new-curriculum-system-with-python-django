from django.shortcuts import render
from .models import Pre_primary_performance, Lower_primary_performance, Upper_primary_performance
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView


class PrePrimaryListView(ListView):
    model = Pre_primary_performance
    context_object_name = 'students'


class PrePrimaryCreateView(LoginRequiredMixin, CreateView):
    model = Pre_primary_performance
    fields = '__all__'
    success_url = '/home/pre-primary-performance'

    def form_valid(self, form):
        if self.request.user:
            return super().form_valid(form)


class PrePrimaryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pre_primary_performance
    fields = ['Language_activities', 'Mathematical_activities', 'Environmental_activities', 'Psychomotor_and_creative_activities', 'Religious_education_activities', 'Teachers_comment']

    def form_valid(self, form):
        if self.request.user:
            return super().form_valid(form)

    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False


class PrePrimaryDetailView(DetailView):
    model = Pre_primary_performance

# lower primary views


class LowerPrimaryListView(ListView):
    model = Lower_primary_performance
    context_object_name = 'students'


class LowerPrimaryCreateView(LoginRequiredMixin, CreateView):
    model = Lower_primary_performance
    fields = '__all__'
    success_url = '/home/lower-primary-performance'

    def form_valid(self, form):
        if self.request.user:
            return super().form_valid(form)


class LowerPrimaryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Lower_primary_performance
    fields = ['English_language_activities', 'Literacy_activities', 'Kiswahili_language_activities', 'Mathematical_activities', 'Hygiene_and_nutrition_activities', 'Environmental_activities', 'Indigenous_language_activities', 'Movement_and_creative_activities', 'Religious_education_activities', 'Teachers_comment']

    def form_valid(self, form):
        if self.request.user:
            return super().form_valid(form)

    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False


class LowerPrimaryDetailView(DetailView):
    model = Lower_primary_performance

# upper primary performance view


class UpperPrimaryListView(ListView):
    model = Upper_primary_performance
    context_object_name = 'students'


class UpperPrimaryCreateView(LoginRequiredMixin, CreateView):
    model = Upper_primary_performance
    fields = '__all__'
    success_url = '/home/upper-primary-performance'

    def form_valid(self, form):
        if self.request.user:
            return super().form_valid(form)


class UpperPrimaryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Upper_primary_performance
    fields = ['English', 'Kiswahili_or_Kenya_Sign_Language', 'Home_Science', 'Mathematical', 'Agriculture', 'Science_and_Technology', 'Creative_Arts', 'Physical_and_Health_Education', 'Religious_education_activities', 'Social_Studies', 'Teachers_comment']

    def form_valid(self, form):
        if self.request.user:
            return super().form_valid(form)

    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False


class UpperPrimaryDetailView(DetailView):
    model = Upper_primary_performance
