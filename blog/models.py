from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#this connects to the db section
#each class will be its  own table in db
#each attribute will be its own field in db
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField() #unrestricted
    date_posted = models.DateTimeField(default = timezone.now) #day created and can be modified
    #auto_now=True - used mostly with last modified field
    # #auto_now_add=True - showa date when field was created, cannot be modified
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #If user is deleted the posts will

    def __str__(self):
        return self.title #prints out the title of object created in posts

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk }) #returns new blog to detailed users blogs

