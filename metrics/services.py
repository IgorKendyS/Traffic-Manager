import facebook
from .models import FacebookAccount, FacebookAdsData
from django.utils import timezone

def import_facebook_data(user):
    accounts = FacebookAccount.objects.filter(user=user)
    for account in accounts:
        access_token = account.access_token
        graph = facebook.GraphAPI(access_token=access_token)
        
        # Obter dados das campanhas
        campaigns = graph.get_object(f'{account.account_id}/campaigns', fields='id,name,insights.fields(clicks,cpc,cpm,ctr,date_start,impressions,spend)')
        
        for campaign in campaigns['data']:
            insights = campaign.get('insights', {}).get('data', [])
            for insight in insights:
                FacebookAdsData.objects.create(
                    account=account,
                    campaign_id=campaign['id'],
                    campaign_name=campaign['name'],
                    clicks=insight.get('clicks', 0),
                    cpc=insight.get('cpc', 0),
                    cpm=insight.get('cpm', 0),
                    ctr=insight.get('ctr', 0),
                    data=insight.get('date_start'),
                    impressions=insight.get('impressions', 0),
                    spend=insight.get('spend', 0),
                    utm=''  # Você precisará definir como obter o UTM
                )
    
    return True  # ou algum status de sucesso/falha