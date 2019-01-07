from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from django import forms
# Create your models here.

class Member(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Director(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter director name')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Sector(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter Industry Sector')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Stage(models.Model):
    """Model representing an author."""
    stage_name = models.CharField(max_length=100)


    def get_absolute_url(self):
        """Returns the url to access a particular stage instance."""
        return reverse('stage-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.stage_name

class DealStage(models.Model):
    """Model representing an author."""
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, help_text='Enter summary')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Engagement(models.Model):
    """Model representing an author."""
    engagement_name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, help_text='Enter summary')

    def __str__(self):
        """String for representing the Model object."""
        return self.engagement_name

class Investor(models.Model):
    """Model representing an author."""
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    fund_size = models.CharField(max_length=100)

    def get_absolute_url(self):
        """Returns the url to access a particular engagement instance."""
        return reverse('investor-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Dialouge(models.Model):
    project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True)
    member = models.ForeignKey('Member', on_delete=models.SET_NULL, null=True)
    comment = models.CharField(max_length=200)
    date = models.DateField(null=True, blank=True, auto_now=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.comment

    def get_absolute_url(self):
        """Returns the url to access a particular engagement instance."""
        return reverse('dialouge-detail', args=[str(self.id)])

class Doc(models.Model):
    name =  models.CharField(max_length=200)
    project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True)
    document = models.FileField(upload_to='projects/documents/', null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular engagement instance."""
        return reverse('doc-detail', args=[str(self.id)])

class VDcomp(models.Model):
    """Model representing an author."""
    name = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Location(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=20)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Source(models.Model):
    name = models.CharField(max_length = 20)
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class OStatus(models.Model):
    name = models.CharField(max_length = 20)
    def __str__(self):
        """String for representing the Model object."""
        return self.name


class pDesignation(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=20)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Partner(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200)
    investor = models.ForeignKey('Investor', on_delete=models.SET_NULL, null=True)
    sector = models.ManyToManyField(Sector)
    designation = models.ForeignKey('pDesignation', on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    investments = models.IntegerField('No. Of Investments', null=True, help_text='Portfolio/Investments')
    companies = models.TextField(max_length=1000)


    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('partner-detail', args=[str(self.id)])

class Project(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    name = models.CharField(max_length=200)
    city = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    sector = models.ManyToManyField(Sector)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    source = models.ForeignKey('Source',  on_delete=models.SET_NULL, null=True)
    dealstage = models.ForeignKey('DealStage', on_delete=models.SET_NULL, null=True)
    overall_Status = models.ForeignKey('OStatus', on_delete=models.SET_NULL, null=True)
    funding_Round = models.ForeignKey('Stage', on_delete=models.SET_NULL, null=True)
    engagement = models.ForeignKey('Engagement', on_delete=models.SET_NULL, null=True)
    updated_at = models.DateField(null=True, blank=True, auto_now = True)
    date = models.DateField(null=True, blank=True, auto_now_add=True)
    description = models.CharField(max_length=500,blank=True)
    metric = models.CharField(max_length=100,blank=True, help_text='Total funding received till date or Company valuation')
    investor = models.ManyToManyField(Investor, blank=True)
    if_other_investor = models.CharField(max_length=100, blank=True)
    partner = models.ManyToManyField(Partner, blank=True, help_text='Only Select partners relevant to this engagement')
    competitor = models.ManyToManyField(VDcomp)
    amount = models.CharField(max_length=50, blank=True, help_text='Leave blank if you dont know the loan amount yet.')


    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    member = models.ManyToManyField(Member)
    director = models.ForeignKey('Director', null=True, on_delete=models.SET_NULL, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('project-detail', args=[str(self.id)])

