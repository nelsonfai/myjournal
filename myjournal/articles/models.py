from time import time
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from accounts.models import Profile
from django.utils import timezone
import math
from django.utils.text import slugify
from taggit.managers import TaggableManager

# Create your models here.
def timefunction(time):
        now = timezone.now()
        diff= now - time
        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            if seconds == 1:
                return str(seconds) +  "second ago"
            else:
                return str(seconds) + " seconds ago"
        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)
            if minutes == 1:
                return str(minutes) + " minute ago"
            else:
                return str(minutes) + " minutes ago"
        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)
            if hours == 1:
                return str(hours) + " hour ago"
            else:
                return str(hours) + " hours ago"
        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
            if days == 1:
                return str(days) + " day ago"
            else:
                return str(days) + " days ago"
        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"
        if diff.days >= 365:
            years= math.floor(diff.days/365)
            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"


statusChoice=(
    ('publish','publish'), ('draft','draft'))
class Articles(models.Model):
    author= models.ForeignKey( Profile, related_name='author' ,on_delete= models.CASCADE )
    title = models.CharField( max_length=100)
    body = RichTextUploadingField( blank=True, null=True)
    date =models.DateTimeField(auto_now_add=True)
    likes =models.ManyToManyField(User, default=None,blank=True, related_name='liked')
    status=models.CharField(choices =statusChoice, default='draft', max_length=10)
    tags=TaggableManager()

    def __str__(self):
        return self.title 
    def snippet(self):
        return self.body[:100] + "..."  
    def slug(self):
        return slugify(self.title)
    
    def __str__(self):
        return self.title

    def writestreak(self):
            return self
    def whenpublished (self):
        return timefunction(self.date)

    
    @property
    def num_likes(self):
        return self.liked.all().count()

class Comments (models.Model):
    article= models.ForeignKey(Articles, related_name='comments' ,on_delete= models.CASCADE)
    comment= models.TextField()
    date= models.DateTimeField(auto_now=True)
    author=models.ForeignKey(Profile, related_name='userprofile' ,on_delete= models.CASCADE, default=None)
    
    

    def __str__(self):
        return f'{self.author.id} commented on {self.article.title}' 
    
LIKE_CHOICES=(
    ('Like','Like'), ('Unlike','Unlike'))

class Like(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE)
    article=models.ForeignKey(Articles,on_delete=models.CASCADE)
    value =models.CharField(choices =LIKE_CHOICES, default='Like', max_length=10)



from calendar import HTMLCalendar
from datetime import date
from itertools import groupby

from django.utils.html import conditional_escape as esc

class WorkoutCalendar(HTMLCalendar):

    def __init__(self, workouts):
        super(WorkoutCalendar, self).__init__()
        self.workouts = self.group_by_day(workouts)
        print(1)
        

    def formatday(self, day,weekday):
        print(2)
        print(day)
        print('--------')
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += ' today'
                print(3)

           
            if day in self.workouts:
                    
                    cssclass += ' filled'
                    body = ['<ul>']
                   
                    print(4)
            return self.day_cell(cssclass, day)
        return self.day_cell('noday', '&nbsp;')

    def formatmonth(self, year, month,withyear=True):
        self.year, self.month = year, month
        print(5)
        return super(WorkoutCalendar, self).formatmonth(year, month)

    def group_by_day(self, workouts):
        field = lambda workouts: workouts.date.day
        print(6)
        
        
        return dict(
            [(day, list(items)) for day, items in groupby(workouts, field)]
        )

    def day_cell(self, cssclass, body):
        print(7)
        return '<td class="%s">%s</td>' % (cssclass, body)
 
 


class Calendar(HTMLCalendar):
    def __init__(self,profile, year=None, month=None):
        self.year = year
        self.month = month
        self.profile=profile
        
       
        super(Calendar, self).__init__()

    def formatday(self, day, events):
            
        events_per_day = events.filter(date__day=day)
        d = ''
        for event in events_per_day:
                return f"<td><span class='filled'>{day}</span><ul> {d} </ul></td>"
        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td > </td>'
    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'
    def formatmonth(self, withyear=True,*arg):
        events = Articles.objects.filter(author=self.profile).filter(date__year=self.year, date__month=self.month)
        cal = f'<table border="0" cellpadding="0" cellspacing="0"     class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        return cal

class Prompts(models.Model):
    topic = models.CharField( max_length=200)
    date =models.DateTimeField(auto_now_add=True )
    def __str__(self):
        return self.topic
    def whenpublished (self):
        return timefunction(self.date)

class Writeups(models.Model):
    author=models.ForeignKey( Profile, related_name='prompt_author' ,on_delete= models.CASCADE )
    prompt=models.ForeignKey( 'Prompts', related_name='prompt' ,on_delete= models.CASCADE )
    title = models.CharField( max_length=200,null =True,blank=True)
    body=RichTextUploadingField( blank=False, null=False)
    likes =models.ManyToManyField(User, default=None,blank=True, related_name='writeupsLikes')
    date =models.DateTimeField(auto_now_add=True )
   
    def whenpublished (self):
        return timefunction(self.date)




class Writeups_Comments (models.Model):
    writeups= models.ForeignKey(Writeups, related_name='writeupsComments' ,on_delete= models.CASCADE)
    comment= models.TextField()
    date= models.DateTimeField(auto_now=True)
    author=models.ForeignKey(Profile, related_name='writeupprofile' ,on_delete= models.CASCADE, default=None)
    
    def __str__(self):
        return f'{self.author.id} commented on {self.article.title}' 
    
