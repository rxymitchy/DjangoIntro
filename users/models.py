from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #one user is entitled to one profile and if user is deleted, so is the profile

    #adding other fields
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    #return content of object instead of the string
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        #resizing image
        img = Image.open(self.image.path) #opens image of current instance

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path) #saves and overrides current image
