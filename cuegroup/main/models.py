from django.db import models


class IndiviualRequest(models.Model):
    email = models.EmailField(null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.first_name


class CompanyRequest(models.Model):
    main_email = models.EmailField(null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    main_phone = models.IntegerField(null=True, blank=True)
    DOC = models.DateField(null=True, blank=True)
    area_created = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.company_name
