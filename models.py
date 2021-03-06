from django.db import models

class ResumeOfStudent(models.Model):
    name = models.CharField(max_length = 50)
    designation = models.CharField(max_length = 50)
    email = models.EmailField()
    contact_no = models.IntegerField()
    Expertise_and_Experience = models.TextField()
    Professional_Experience = models.CharField(max_length = 50)
    education_details = models.TextField()
    technical_skills = models.CharField(max_length = 50)
    frameworks = models.CharField(max_length = 50)
    databases = models.CharField(max_length = 50)
    operating_system = models.CharField(max_length = 50)
    project_title = models.CharField(max_length = 50)
    client = models.CharField(max_length = 50)
    role = models.CharField(max_length = 50)
    environment = models.CharField(max_length = 50)
    project_description = models.TextField()
    responsibilities = models.TextField()
    date_of_birth =models.DateField()
    languages = models.CharField(max_length = 50)
    marital_status = models.CharField(max_length = 50)
    declaration = models.CharField(max_length = 50)
    