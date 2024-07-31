from django.db import models



class CoursesCategoryChoices(models.TextChoices):
    mobile_app = 'Mobile App', 'Mobile App'
    back_end = 'Back-end', 'Back-end'
    front_end = 'Front-end', 'Front-end'
    database = 'Database', 'Database'
    other = 'Other', 'Other'
    programming_language = 'Programming Language', 'Programming Language'



class Courses(models.Model):

    id = models.AutoField(null= False, blank= False, primary_key= True)
    course_title = models.CharField(null= False, blank= False, default= '', max_length= 125)
    course_description = models.TextField(null= False, blank= False, default= '')
    course_image = models.ImageField(null= False, blank= False, upload_to= 'course_images/')
    course_link = models.URLField(null= False, blank= False, default= '', unique= True)
    course_hours = models.IntegerField(null= False, blank= False, default= 0)
    course_price = models.FloatField(null= False, blank= False, default= 0.0)
    course_price_currency = models.CharField(null= False, blank= False, default= '', max_length= 3)
    course_category = models.CharField(null= True, blank= True, default= '', max_length= 25)
    is_archived = models.BooleanField(null= False, blank= False, default= False)



    def __str__(self):
        return self.course_title