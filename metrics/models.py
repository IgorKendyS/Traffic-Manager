from django.db import models
from django.contrib.auth.models import User

class FacebookAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='facebook_accounts')
    account_id = models.CharField(max_length=100, unique=True)
    account_name = models.CharField(max_length=255)
    access_token = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.account_name} ({self.account_id})"

class FacebookAdsData(models.Model):
    account = models.ForeignKey(FacebookAccount, on_delete=models.CASCADE, null=True, default=None)
    campaign_id = models.CharField(max_length=255, null=True, default=None)
    campaign_name = models.CharField(max_length=255, null=True, default=None)
    clicks = models.IntegerField(null=True, default=None)
    cpc = models.FloatField(null=True, default=None)
    cpm = models.FloatField(null=True, default=None)
    ctr = models.FloatField(null=True, default=None)
    data = models.DateField(null=True, default=None)
    impressions = models.IntegerField(null=True, default=None)
    spend = models.FloatField(null=True, default=None)
    utm = models.TextField(null=True, default=None)

    def __str__(self):
        return f"{self.campaign_name} - {self.data}"

class GoogleAdsData(models.Model):
    campaign_id = models.CharField(max_length=255, null=True, default=None)
    clicks = models.IntegerField(null=True, default=None)
    cpc = models.FloatField(null=True, default=None)
    ctr = models.FloatField(null=True, default=None)
    day = models.DateField(null=True, default=None)
    dominio = models.CharField(max_length=255, null=True, default=None)
    total_cost = models.FloatField(null=True, default=None)
    utm = models.TextField(null=True, default=None)

    def __str__(self):
        return f"{self.campaign_id} - {self.day}"