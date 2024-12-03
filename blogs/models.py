from django.db import models


class Blogs(models.Model):
    id = models.AutoField(null= False, blank= False, primary_key= True)
    blog_title = models.CharField(null= False, blank= False, default= '', max_length= 25)
    blog_content = models.TextField(null= False, blank= False, default= '')
    blog_image = models.ImageField(null= False, blank= False, upload_to= 'blogs/')
    is_archived = models.BooleanField(null= False, blank= False, default= False)
    views = models.PositiveIntegerField(null= False, blank= False, default= 0)
    created_at = models.DateTimeField(null= False, blank= False, auto_now_add= True)

    def __str__(self):
        return self.blog_title