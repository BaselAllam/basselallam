from django.db import models



class Gallery(models.Model):

    id = models.AutoField(null= False, blank= False, primary_key= True)
    image = models.ImageField(null= False, blank= False, upload_to= 'gallery/')
    is_archived = models.BooleanField(null= False, blank= False, default= False)