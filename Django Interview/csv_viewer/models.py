from django.db import models

# Create your models here.


class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class AssessmentArea(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class Award(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class Class(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100)

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=100)
    subject_score = models.FloatField()

class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    answer = models.CharField(max_length=100)
