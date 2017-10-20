from __future__ import unicode_literals
from django.db import models
from django.forms import ComboField

class question(models.Model):
	#choices for fields
	#first choice of tuple in the list is the name of any choice (question.subject)and the second object of tuple is what we see in form
	Subject_choices=[('English','English'),('SocialScience','SocialScience'),('Maths','Mathematics'),('Science','Science')]
	Class_choices = [('5', '5th'), ('6', '6th'), ('7','7th'), ('8', '8th')]
	Topic_choices = [('1', 'WhatWhereAndWhen'),('2', 'OntheTrailoftheEarliestPeople'),('3','FromGatheringtoGrowingFood'),('4', 'WhoDidPatrickHomeworkAHouseAHome'),('5','HowtheDogFoundHimselfaNewMaster'),('6','TarosReward')]
	Difficulty_choices=[('Easy','Easy'),('Medium','Medium'),('Hard','Hard')]
	#form fields
	#the below written order is seen by admin in database after opening question
	Question = models.TextField()
	Subject=models.CharField(max_length=50,choices=Subject_choices,default=' ')
	Class=models.CharField(max_length=10,choices=Class_choices,default=' ')
	topic=models.CharField(max_length=50,choices=Topic_choices,default=' ')
	difficulty = models.CharField(max_length=10, choices=Difficulty_choices, default=' ')
	Question_Image=models.FileField(upload_to='images')
	Number_of_Questions=models.CharField(max_length=50,default='0')
	       #upload_to give location for image storage
	#status = models.CharField(max_length=10, choices=Strings_choices,default=' ')
	# Strings_choices=[(str(i), calendar.month_name[i]) for i in range(1,13)]
	def __str__(self):
		return self.Class+'-'+self.Subject+'-'+self.topic+'-'+self.difficulty	