from django.db import models
from django.forms import ModelForm, TextInput

# Create your models here.
class Artist(models.Model):
    artistid = models.IntegerField(primary_key=True)
    artist = models.CharField(max_length=765)
    alias = models.TextField()
    class Meta:
        db_table = u'artist'
    def __unicode__(self):
    	return self.artist
	
class Album(models.Model):
    albumid = models.IntegerField(primary_key=True)
    album = models.CharField(max_length=765)
    artistid = models.ForeignKey(Artist, db_column='artistid', to_field='artistid')
    class Meta:
        db_table = u'album'

class Song(models.Model):
    songid = models.IntegerField(primary_key=True)
    albumid = models.ForeignKey(Album, db_column='albumid', to_field='albumid')
    title = models.CharField(max_length=765)
    lyrics = models.TextField()
    artistid = models.ForeignKey(Artist, db_column='artistid', to_field='artistid')

    class Meta:
        db_table = u'song'
    def __unicode__(self):
    	return self.title
        
class Snippet(models.Model):
    snippetid = models.IntegerField(primary_key=True)
    songid = models.ForeignKey(Song, db_column='songid', to_field='songid')
    chunk = models.TextField()
    user_answer = models.CharField(max_length=765)
    decoded = models.CharField(max_length=765)
    comments = models.TextField()
    def __unicode__(self):
    	return self.chunk

class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        fields = ('user_answer', 'chunk')

