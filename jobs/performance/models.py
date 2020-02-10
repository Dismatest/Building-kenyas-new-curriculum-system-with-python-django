from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
from school.models import Pre_primary, Lower_primary, Upper_primary


class Pre_primary_performance(models.Model):
    valid = RegexValidator(regex=r'\d{2}+\s', message="only digits are required.")
    Student_name = models.OneToOneField(Pre_primary, on_delete=models.CASCADE)
    Language_activities = models.CharField(validators=[valid], max_length=255)
    Mathematical_activities = models.CharField(validators=[valid], max_length=255)
    Environmental_activities = models.CharField(validators=[valid], max_length=255)
    Psychomotor_and_creative_activities = models.CharField(validators=[valid], max_length=255)
    Religious_education_activities = models.CharField(validators=[valid], max_length=255)
    Teachers_comment = models.TextField()

    def __str__(self):
        return str(self.Student_name)

    def get_absolute_url(self):
        return reverse("pre-primary-performance-details", kwargs={"pk": self.pk})


class Lower_primary_performance(models.Model):
    Student_name = models.OneToOneField(Lower_primary, on_delete=models.CASCADE)
    English_language_activities = models.CharField(max_length=255)
    Literacy_activities = models.CharField(max_length=255)
    Kiswahili_language_activities = models.CharField(max_length=255)
    Mathematical_activities = models.CharField(max_length=255)
    Hygiene_and_nutrition_activities = models.CharField(max_length=255)
    Environmental_activities = models.CharField(max_length=255)
    Indigenous_language_activities = models.CharField(max_length=255)
    Movement_and_creative_activities = models.CharField(max_length=255)
    Religious_education_activities = models.CharField(max_length=255)
    Teachers_comment = models.TextField()

    def __str__(self):
        return str(self.Student_name)

    def get_absolute_url(self):
        return reverse("lower-primary-performance-details", kwargs={"pk": self.pk})


class Upper_primary_performance(models.Model):
    Student_name = models.OneToOneField(Upper_primary, on_delete=models.CASCADE)
    English = models.CharField(max_length=255)
    Kiswahili_or_Kenya_Sign_Language = models.CharField(max_length=255)
    Home_Science = models.CharField(max_length=255)
    Mathematical = models.CharField(max_length=255)
    Agriculture = models.CharField(max_length=255)
    Science_and_Technology = models.CharField(max_length=255)
    Creative_Arts = models.CharField(max_length=255)
    Physical_and_Health_Education = models.CharField(max_length=255)
    Religious_education_activities = models.CharField(max_length=255)
    Social_Studies = models.CharField(max_length=255)
    Teachers_comment = models.TextField()

    def __str__(self):
        return str(self.Student_name)

    def get_absolute_url(self):
        return reverse("upper-primary-performance-details", kwargs={"pk": self.pk})




