from django.urls import path
from performance import views as performance_view


urlpatterns = [
   path('home/pre-primary-performance/', performance_view.PrePrimaryListView.as_view(), name="pre-primary-performance"),
   path('home/pre-primary-performance-create/', performance_view.PrePrimaryCreateView.as_view(), name="pre-primary-performance-create"),
   path('home/pre-primary-performance/<int:pk>/', performance_view.PrePrimaryDetailView.as_view(), name='pre-primary-performance-details'),
   path('home/pre-primary-performance/<int:pk>/update', performance_view.PrePrimaryUpdateView.as_view(), name='pre-primary-performance-update'),
   #lower primary urls
   path('home/lower-primary-performance/', performance_view.LowerPrimaryListView.as_view(), name="lower-primary-performance"),
   path('home/lower-primary-performance-create/', performance_view.LowerPrimaryCreateView.as_view(), name="lower-primary-performance-create"),
   path('home/lower-primary-performance/<int:pk>/update', performance_view.LowerPrimaryUpdateView.as_view(), name='lower-primary-performance-update'),
   path('home/lower-primary-performance/<int:pk>/', performance_view.LowerPrimaryDetailView.as_view(), name='lower-primary-performance-details'),
   #upper primary urls
   path('home/upper-primary-performance/', performance_view.UpperPrimaryListView.as_view(), name="upper-primary-performance"),
   path('home/upper-primary-performance-create/', performance_view.UpperPrimaryCreateView.as_view(), name="upper-primary-performance-create"),
   path('home/upper-primary-performance/<int:pk>/update', performance_view.UpperPrimaryUpdateView.as_view(), name='upper-primary-performance-update'),
   path('home/upper-primary-performance/<int:pk>/', performance_view.UpperPrimaryDetailView.as_view(), name='upper-primary-performance-details'),
]
