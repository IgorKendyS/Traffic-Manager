from django.db import models

class GoogleAdsData(models.Model):
    date = models.DateField()
    campaign_name = models.CharField(max_length=255)
    clicks = models.IntegerField()
    impressions = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    conversions = models.IntegerField()

    def __str__(self):
        return f"{self.campaign_name} - {self.date}"

class FacebookAdsData(models.Model):
    date = models.DateField()
    campaign_name = models.CharField(max_length=255)
    reach = models.IntegerField()
    impressions = models.IntegerField()
    spend = models.DecimalField(max_digits=10, decimal_places=2)
    link_clicks = models.IntegerField()

    def __str__(self):
        return f"{self.campaign_name} - {self.date}"