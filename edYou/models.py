from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	pass


class Course(models.Model):

	DIFFICULTY_CHOICES = [
		('Beginner', 'beginner'),
		('Intermediate', 'intermediate'),
		('Advanced', 'advanced')
	]

	teacher = models.ForeignKey("User", on_delete=models.CASCADE)
	name = models.CharField(max_length=64)
	subject = models.CharField(max_length=32)
	language = models.CharField(max_length=32)
	difficulty = models.CharField(max_length=12, choices=DIFFICULTY_CHOICES)
	duration = models.CharField(max_length=16)
	description = models.TextField()
	img = models.ImageField(upload_to="photos/%Y/%m/%d")


class Chapter(models.Model):

	course = models.ForeignKey("Course", on_delete=models.CASCADE)
	name = models.CharField(max_length=64)


class Video(models.Model):

	chapter = models.ForeignKey("Chapter", on_delete=models.CASCADE)
	name = models.CharField(max_length=64)
	video = models.TextField()


class Enrolled(models.Model):

	user = models.ForeignKey("User", on_delete=models.CASCADE)
	course = models.ForeignKey("Course", on_delete=models.CASCADE)


class Notes(models.Model):

	user = models.ForeignKey("User", on_delete=models.CASCADE)
	course = models.ForeignKey("Course", on_delete=models.CASCADE)
	content = models.TextField()
