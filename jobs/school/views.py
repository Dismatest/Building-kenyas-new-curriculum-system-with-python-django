from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
import xlwt
from django.http import HttpResponse
from .models import Pre_primary, Lower_primary, Upper_primary


@login_required
def home(request):
    return render(request, 'school/home.html')


def dashboard(request):
    return render(request, 'school/dashboard.html')


def track_progress(request):
    return render(request, 'school/track_progress.html')


def fees_status(request):
    return render(request, 'school/fees_status.html')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your have successfully changed your password')
            return redirect('home')
        else:
            messages.error(request, 'There was an error, please try again latter')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'school/change_password.html', {"form": form})

# class based views for pre primary


class StudentsListView(ListView):
    model = Pre_primary
    template_name = 'school/addstudent.html'
    context_object_name = 'students'


class StudentsDetailView(DetailView):
    model = Pre_primary


class StudentsCreateView(LoginRequiredMixin, CreateView):
    model = Pre_primary
    fields = '__all__'
    success_url = '/home/students/'

    def form_valid(self, form):
        self.request.user
        return super().form_valid(form)


class StudentsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pre_primary
    fields = '__all__'

    def form_valid(self, form):
        self.request.user
        return super().form_valid(form)

    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False


class StudentsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pre_primary
    success_url = '/home/students/'

    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False

# class based views for lower primary


class LowerPrimaryStudentsListView(ListView):
    model = Lower_primary
    template_name = 'school/lower_primary.html'
    context_object_name = 'students'


class LowerPrimaryStudentsDetailView(DetailView):
    model = Lower_primary


class LowerPrimaryStudentsCreateView(LoginRequiredMixin, CreateView):
    model = Lower_primary
    fields = '__all__'
    success_url = '/home/lower-primary-students'

    def form_valid(self, form):
        self.request.user
        return super().form_valid(form)


class LowerPrimaryStudentsUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Lower_primary
    fields = '__all__'

    def form_valid(self, form):
        self.request.user
        return super().form_valid(form)

    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False


class LowerPrimaryStudentsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Lower_primary
    success_url = '/home/lower-primary-students/'

    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False


# class based views for upper primary

class UpperPrimaryStudentsListView(ListView):
    model = Upper_primary
    context_object_name = 'students'


class UpperPrimaryStudentsDetailView(DetailView):
    model = Upper_primary


class UpperPrimaryStudentsCreateView(LoginRequiredMixin, CreateView):
    model = Upper_primary
    fields = '__all__'
    success_url = '/home/upper-primary-students'

    def form_valid(self, form):
        self.request.user
        return super().form_valid(form)


class UpperPrimaryStudentsUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Upper_primary
    fields = '__all__'

    def form_valid(self, form):
        self.request.user
        return super().form_valid(form)

    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False


class UpperPrimaryStudentsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Upper_primary
    success_url = '/home/upper-primary-students/'

    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False


# end of class based views for upper primary

# export to excel pre primary
def export_pre_primary_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="pre_primary_students.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Pre_Primary Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Id', 'Student_name', 'Registration_number ', 'Student_class', 'Student_gender', 'Parent_name', 'Phone_number', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Pre_primary.objects.all().values_list('id', 'student_name', 'registration_number', 'student_class', 'student_gender', 'parent_name', 'phone_number')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response

# export to excel lower primary
def export_lower_primary_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="lower_primary_students.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('lower_Primary Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Id', 'Student_name', 'Registration_number ', 'Student_class', 'Student_gender', 'Parent_name', 'Phone_number', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Lower_primary.objects.all().values_list('id', 'student_name', 'registration_number', 'student_class', 'student_gender', 'parent_name', 'phone_number')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

# export to excel upper primary
def export_upper_primary_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="upper_primary_students.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Upper_Primary Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Id', 'Student_name', 'Registration_number ', 'Student_class', 'Student_gender', 'Parent_name', 'Phone_number', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Upper_primary.objects.all().values_list('id', 'student_name', 'registration_number', 'student_class', 'student_gender', 'parent_name', 'phone_number')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response
