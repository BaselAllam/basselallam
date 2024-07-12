from django.db import models
from utils import shared_choises


class ContactStatus(models.TextChoices):
    waiting = 'Waiting', 'Waiting'
    done = 'Done', 'Done'
    dealed = 'Dealed', 'Dealed'
    archived = 'Archived', 'Archived'



class ContactMe(models.Model):

    id = models.AutoField(null= False, blank= False, primary_key= True)
    client_name = models.CharField(null= False, blank= False, default= '', max_length= 50)
    client_email = models.EmailField(null= False, blank= False)
    client_number = models.CharField(null= False, blank= False, default= '', max_length= 20)
    client_message = models.CharField(null= False, blank= False, default= '', max_length= 225)
    client_service = models.CharField(null= False, blank= False, default= shared_choises.ServicesChoises.web_dev, choices= shared_choises.ServicesChoises.choices, max_length= 20)
    contacted_at = models.DateField(null= False, blank= False, auto_created= True, auto_now= True)
    status = models.CharField(null= False, blank= False, default= ContactStatus.waiting, choices= ContactStatus.choices, max_length= 10)


    def __str__(self):
        return self.client_name