from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone
from registration.signals import user_registered
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

import os

def user_registered_callback(sender, user, request, **kwargs):
	aff_name = request.POST.get('name','')
	aff_city = request.POST.get('city','')
	aff_country = request.POST.get('country','')
	bio = request.POST.get('bio','')
	first_name = request.POST.get('first_name','')
	last_name = request.POST.get('last_name','')
	avatar = request.FILES.get('avatar',None)
	if first_name == 'zyx':
		first_name = user.username
		last_name = ''
	new_affiliation = Affiliation.objects.create(name=aff_name, country=aff_country, city=aff_city)
	profile = Profile.objects.create(user=user, affiliation=new_affiliation, bio=bio, first_name=first_name, last_name=last_name, avatar=avatar)

user_registered.connect(user_registered_callback)

class Affiliation(models.Model):
	name = models.CharField(max_length=100)
	country = models.CharField(max_length=50)
	city = models.CharField(max_length=50)

	def __str__(self):
		return unicode(self.name).encode('utf-8')

class Event(models.Model):
	title = models.CharField(max_length=100)
	description = RichTextField()
	# parent_event = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return unicode(self.title).encode('utf-8')

	def get_absolute_url(self):
		if Challenge.objects.filter(id=self.id).count() > 0:
			return reverse("challenge_desc", kwargs={"id": self.id})
		elif Workshop.objects.filter(id=self.id).count() > 0:
			return reverse("workshop_desc", kwargs={"id": self.id})
		elif Special_Issue.objects.filter(id=self.id).count() > 0:
			return reverse("special_issue_desc", kwargs={"id": self.id})
		else:
			return reverse("event_edit", kwargs={"id": self.id})

def user_avatar_path(instance, filename):
	return 'userpics/%s-%s/%s' % (instance.first_name, instance.last_name, filename)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	first_name = models.CharField(max_length=30, null=True)
	last_name = models.CharField(max_length=30, null=True)
	affiliation = models.OneToOneField(Affiliation, on_delete=models.CASCADE, null=True)
	bio = models.TextField(max_length=3000)
	avatar = models.ImageField(upload_to=user_avatar_path, null=True, default='/static/images/default.jpg')
	events = models.ManyToManyField(Event, through='Profile_Event')

	def __str__(self):
		return unicode(self.first_name).encode('utf-8')

	def get_absolute_url(self):
		return reverse("profile_edit", kwargs={"id": self.id})

class Proposal(models.Model):
	title = models.CharField(max_length=100)
	type = models.CharField(max_length=2, null=True)
	description = RichTextField()

	def __str__(self):
		return unicode(self.title).encode('utf-8')

class Role(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return unicode(self.name).encode('utf-8')

class Profile_Event(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, related_name='fk_profile', null=True)
	event = models.ForeignKey(Event, on_delete=models.SET_NULL, related_name='fk_event', null=True)
	role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

def partner_member_avatar_path(instance, filename):
	return 'partner/members/%s-%s/%s' % (instance.first_name, instance.last_name, filename)

class Contact(models.Model):
	first_name = models.CharField(max_length=30, null=True)
	last_name = models.CharField(max_length=30, null=True)
	bio = models.TextField(max_length=3000)
	avatar = models.ImageField(upload_to=partner_member_avatar_path, null=True, default='/static/images/default.jpg')
	email = models.CharField(max_length=100, null=True)

	def __str__(self):
		return unicode(self.first_name).encode('utf-8')

def partner_avatar_path(instance, filename):
	return 'partner/%s/%s' % (instance.name, filename)

class Partner(models.Model):
	name = models.CharField(max_length=100)
	url = models.CharField(max_length=500)
	banner = models.ImageField(upload_to=partner_avatar_path, null=True)
	events = models.ManyToManyField(Event, through='Event_Partner')
	contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return unicode(self.name).encode('utf-8')

class Event_Partner(models.Model):
	partner = models.ForeignKey(Partner, on_delete=models.SET_NULL, null=True)
	event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
	role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

class News(models.Model):
	title = models.CharField(max_length=100)
	description = RichTextField()
	upload_date = models.DateTimeField()
	event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)

	def save(self, *args, **kwargs):
		if not self.id:
			self.upload_date = timezone.now()
		return super(News, self).save(*args, **kwargs)

	def __str__(self):
		return unicode(self.title).encode('utf-8')

	def get_absolute_url(self):
		return reverse("news_edit", kwargs={"id": self.id})

class Special_Issue(Event):

	def __str__(self):
		return unicode(self.title).encode('utf-8')

	def get_absolute_url(self):
		return reverse("special_issue_desc", kwargs={"id": self.id})

class Workshop(Event):

	def __str__(self):
		return unicode(self.title).encode('utf-8')

	def get_absolute_url(self):
		return reverse("workshop_desc", kwargs={"id": self.id})

def workshop_gallery(gallery, filename):
	return 'gallery/%s/%s' % (gallery.workshop.title, filename)

class Gallery_Image(models.Model):
	image = models.ImageField(upload_to='workshop_gallery', null=True)
	description = RichTextField(null=True)
	workshop = models.ForeignKey(Workshop, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return unicode(self.id).encode('utf-8')

class Challenge(Event):

	def __str__(self):
		return unicode(self.title).encode('utf-8')

	def get_absolute_url(self):
		return reverse("challenge_desc", kwargs={"id": self.id})

class Dataset(models.Model):
	title = models.CharField(max_length=100, null=True)
	description = RichTextField()
	tracks = models.ManyToManyField(Challenge, through='Track')

	def __str__(self):
		return unicode(self.title).encode('utf-8')

	def get_absolute_url(self):
		return reverse("dataset_desc", kwargs={"id": self.id})

class Schedule_Event(models.Model):
	title = models.CharField(max_length=100, null=True)
	description = RichTextUploadingField()
	date = models.DateTimeField()
	schedule_event_parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
	event_schedule = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, related_name='event_schedule')
	event_program = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, related_name='event_program')
	dataset_schedule = models.ForeignKey(Dataset, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return unicode(self.title).encode('utf-8')

class Event_Relation(models.Model):
	challenge_relation = models.ForeignKey(Challenge, on_delete=models.SET_NULL, related_name='challenge_relation', null=True)
	issue_relation = models.ForeignKey(Special_Issue, on_delete=models.SET_NULL, related_name='issue_relation', null=True)
	workshop_relation = models.ForeignKey(Workshop, on_delete=models.SET_NULL, related_name='workshop_relation', null=True)
	dataset_relation = models.ForeignKey(Dataset, on_delete=models.SET_NULL, related_name='dataset_relation', null=True)
	event_associated = models.ForeignKey(Event, on_delete=models.SET_NULL, related_name='event_associated', null=True)
	dataset_associated = models.ForeignKey(Dataset, on_delete=models.SET_NULL, related_name='dataset_associated', null=True)
	description = RichTextField()

	def __str__(self):
		return unicode(self.id).encode('utf-8')

class Track(models.Model):
	title = models.CharField(max_length=100)
	description = RichTextField()
	metrics = RichTextField(null=True)
	baseline = RichTextField(null=True)
	challenge = models.ForeignKey(Challenge, on_delete=models.SET_NULL, null=True)
	dataset = models.ForeignKey(Dataset, on_delete=models.SET_NULL, null=True)

class Result(models.Model):
	# title = models.CharField(max_length=100)
	# score = models.DecimalField(null=True, max_digits=15, decimal_places=10)
	# user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	user = models.CharField(null=True, max_length=100)
	# dataset = models.ForeignKey(Dataset, on_delete=models.SET_NULL, null=True)
	challenge = models.ForeignKey(Challenge, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return unicode(self.user).encode('utf-8')

class Score(models.Model):
	name = models.CharField(null=True, max_length=100)
	score = models.FloatField(null=True)
	result = models.ForeignKey(Result, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return unicode(self.name).encode('utf-8')

class Data(models.Model):
	title = models.CharField(max_length=100)
	description = RichTextField()
	software = RichTextField(null=True)
	metric = RichTextField(null=True)
	dataset = models.ForeignKey(Dataset, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return unicode(self.title).encode('utf-8')

	def get_absolute_url(self):
		return reverse("data_detail", kwargs={"id": self.id, "dataset_id": self.dataset.id})

def data_path(instance, filename):
	return 'datasets/%s/%s/%s' % (instance.data.dataset.title, instance.data.title, filename)

class File(models.Model):
	name = models.CharField(max_length=100, null=True)
	file = models.FileField(upload_to=data_path, null=True)
	url = models.CharField(max_length=500, null=True)
	data = models.ForeignKey(Data, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return unicode(self.name).encode('utf-8')

	def filename(self):
		basename, extension = os.path.splitext(os.path.basename(self.file.name))
		return basename

# class Publication(models.Model):
# 	publicated = models.BooleanField()
# 	result = models.ForeignKey(Result, on_delete=models.CASCADE)