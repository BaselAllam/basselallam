from django.db import models


class ReviewsRateChoises(models.TextChoices):
    one = '1', '1'
    tow = '2', '2'
    three = '3', '3'
    four = '4', '4'
    five = '5', '5'


class Reviews(models.Model):
    id = models.AutoField(null= False, blank= False, primary_key= True)
    client_name = models.CharField(null= False, blank= False, default= '', max_length= 125)
    client_review = models.CharField(null= False, blank= False, default= '', max_length= 225)
    client_rate = models.CharField(null= False, blank= False, default= ReviewsRateChoises.one, choices= ReviewsRateChoises.choices, max_length= 1)
    client_image = models.ImageField(null= False, blank= False, upload_to= 'client_image/')
    is_archived = models.BooleanField(null= False, blank= False, default= False)


    def __str__(self):
        return self.client_name
    