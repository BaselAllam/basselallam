from django.db import models
from courses.models import Courses


class Certificate(models.Model):

    id = models.AutoField(null= False, blank= False, primary_key= True)
    certificate_id = models.IntegerField(null= False, blank= False, unique= True, default= 0)
    std_name = models.CharField(null= False, blank= False, default= '', max_length= 75, unique= True)
    std_email = models.EmailField(null= False, blank= False, unique= True)
    course = models.ForeignKey(Courses, null= False, blank= False, on_delete= models.RESTRICT)
    issued_at = models.DateTimeField(null= False, blank= False)
    is_archived = models.BooleanField(null= False, blank= False, default= False)



    def __str__(self):
        return self.std_name