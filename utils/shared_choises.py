from django.db import models


class ServicesChoises(models.TextChoices):
    mobile_app = 'Mobile App', 'Mobile App'
    web_dev = 'Web Development', 'Web Development'
    erp_sys = 'ERP Systems', 'ERP Systems'
    digital_marketing = 'Digital Marketing', 'Digital Marketing'
    graphic_design = 'Graphic Design', 'Graphic Design'
    multi_services = 'Multi Service', 'Multi Service'
