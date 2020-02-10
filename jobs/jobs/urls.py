from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from user import views as user_views
from school import views as school_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('school.urls')),
    path('', include('performance.urls')),
    path('', include('messaging.urls')),
    path('register/', user_views.register, name='register'),
    path('home/', school_views.home, name='home'),
    path('home/profile/', user_views.profile, name='profile'),
    path('home/dashboard/', school_views.dashboard, name='dashboard'),
    #start of pre_primary urls
    path('home/export-excel/', school_views.export_pre_primary_xls, name='pre-primary-export-excel'),
    path('home/students/', school_views.StudentsListView.as_view(), name='students'),
    path('home/students/new/', school_views.StudentsCreateView.as_view(), name='student-create'),
    path('home/students/<int:pk>/', school_views.StudentsDetailView.as_view(), name='student-details'),
    path('home/students/<int:pk>/update', school_views.StudentsUpdateView.as_view(), name='student-update'),
    path('students/<int:pk>/delete', school_views.StudentsDeleteView.as_view(), name='student-delete'),
    #lower primary urls
    path('home/lower-primary-students/lower-primary-export-excel/', school_views.export_lower_primary_xls, name='lower-primary-export-excel'),
    path('home/lower-primary-students/', school_views.LowerPrimaryStudentsListView.as_view(), name='lower-primary-students'),
    path('home/lower-primary-students/<int:pk>/', school_views.LowerPrimaryStudentsDetailView.as_view(), name='lower-primary-student-details'),
    path('home/lower-primary-students/new/', school_views.LowerPrimaryStudentsCreateView.as_view(), name='lower-primary-student-create'),
    path('home/lower-primary-students/<int:pk>/update', school_views.LowerPrimaryStudentsUpdateView.as_view(), name='lower-primary-student-update'),
    path('lower-primary-students/<int:pk>/delete', school_views.LowerPrimaryStudentsDeleteView.as_view(), name='lower-primary-student-delete'),
    #end of lower primary uls
    path('home/upper-primary-students/upper-primary-export-excel/', school_views.export_upper_primary_xls, name='upper-primary-export-excel'),
    path('home/upper-primary-students/', school_views.UpperPrimaryStudentsListView.as_view(), name='upper-primary-students'),
    path('home/upper-primary-students/<int:pk>/', school_views.UpperPrimaryStudentsDetailView.as_view(), name='upper-primary-student-details'),
    path('home/upper-primary-students/new/', school_views.UpperPrimaryStudentsCreateView.as_view(), name='upper-primary-student-create'),
    path('home/upper-primary-students/<int:pk>/update', school_views.UpperPrimaryStudentsUpdateView.as_view(), name='upper-primary-student-update'),
    path('upper-primary-students/<int:pk>/delete', school_views.UpperPrimaryStudentsDeleteView.as_view(), name='upper-primary-student-delete'),
    #end of upper primary urls
    path('home/track-progress/', school_views.track_progress, name='track-progress'),
    path('home/fees-status/', school_views.fees_status, name='fees-status'),
    path('home/change-password/', school_views.change_password, name='change-password'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'), name='password-reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
