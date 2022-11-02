from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="user_profile")
    profilePic = models.ImageField( blank=True, null=True)
    about_me = models.CharField(max_length=400 ,blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=100 ,blank=True, null=True)
 
    def __str__(self):
         return self.user.username
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            print('Profile created')
    post_save.connect(create_profile, sender=User)
    
    def update_profile(sender, instance, created, **kwargs):
        if created == False:
            instance.save()
            print('Profile updated')
    
    
class Mynetwork(models.Model):
    user=models.OneToOneField(Profile,on_delete=models.CASCADE,related_name="myfollowers")
    myfollowers = models.ManyToManyField(Profile, related_name="following_me" )
    follow = models.ManyToManyField(Profile, related_name="i_follow")
    
    def create_mynetwork(sender, instance, created, **kwargs):
        if created:
            Mynetwork.objects.create(user=instance)
            print('Profile created')
    post_save.connect(create_mynetwork, sender=Profile)

    def add_follower(self, account):
        if account not in self.follow.all():
            self.follow.add(account)
            self.save()
            print('Yess addedd 1')

    def add_following(self, account):
            print(self)
            print('aself') 
            self.myfollowers.add(account)
            self.save()
            print('Yess addedd 2')  

    def remove_follower(self, account):
    		
    			self.follow.remove(account)

  
