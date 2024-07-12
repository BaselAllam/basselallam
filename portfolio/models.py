from django.db import models
from utils import shared_choises



class Portfolio(models.Model):

    id = models.AutoField(null= False, blank= False, primary_key= True)
    portfolio_service = models.CharField(null= False, blank= False, default= shared_choises.ServicesChoises.multi_services, choices= shared_choises.ServicesChoises.choices, max_length= 25)
    portfolio_title = models.CharField(null= False, blank= False, default= '', max_length= 25)
    portfolio_description = models.CharField(null= False, blank= False, default= '', max_length= 225)
    portfolio_image = models.ImageField(null= False, blank= False, upload_to= 'portfolio/')
    is_archived = models.BooleanField(null= False, blank= False, default= False)


    def __str__(self):
        return self.portfolio_title