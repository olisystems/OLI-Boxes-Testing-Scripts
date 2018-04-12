import requests
from requests_oauthlib import OAuth1Session
from requests_oauthlib import OAuth1
def rest_power():
        #URL for the RestAPI
        url='https://api.discovergy.com'
        #URL for the Consumer Token
        consumer_token_url=url+'/public/v1/oauth1/consumer_token'
        head={'Accept':'text/html, image/gif, image/jpeg, *;q=.2, */*;q=.2','Content-Type':'application/x-www-form-urlencoded'}
        #Client name
        data='client=OLITEST'
        #Post Request to get Client Secret and Key
        ret = requests.post(consumer_token_url,data=data,headers=head)
        response=ret.json()
        client_secret=response.get('secret')
        client_key=response.get('key')
        owner=response.get('owner')
        #Request token URL
        request_token_url=url+'/public/v1/oauth1/request_token'
        oauth=OAuth1(client_key,client_secret=client_secret)
        #Post request to get Resource Owner Key and Secret
        r=requests.post(url=request_token_url, auth=oauth)
        from urllib.parse import parse_qs
        credentials = parse_qs(r.content)
        resource_owner_key = str(credentials[b'oauth_token'][0], 'utf-8')
        resource_owner_secret= str(credentials[b'oauth_token_secret'][0],'utf-8')
        #Base Authorization URL
        base_authorization_url= url+'/public/v1/oauth1/authorize'
        authorize_url= base_authorization_url + '?oauth_token='
        #add credentials
        authorize_url=authorize_url+resource_owner_key+'&email=""&password=""'
        import urllib
        rsp=urllib.request.urlopen(authorize_url)
        rr=str(rsp.read(),'utf-8')
        ident,verifier=rr.split("=")
        #Access Token URL
        access_token_url=url+'/public/v1/oauth1/access_token'
        oauth=OAuth1(client_key,client_secret=client_secret,resource_owner_key=resource_owner_key,resource_owner_secret=resource_owner_secret,verifier=verifier)
        r=requests.post(url=access_token_url, auth=oauth)
        credentials= parse_qs(r.content)
        resource_owner_key=str(credentials[b'oauth_token'][0],'utf-8')
        resource_owner_secret=str(credentials[b'oauth_token_secret'][0],'utf-8')
        #URL for the Meter
        meters_url=url+'/public/v1/meters'
        oauth=OAuth1(client_key,client_secret,resource_owner_key,resource_owner_secret)
        r=requests.get(url=meters_url, auth=oauth)
        devices_url= url+'/public/v1/last_reading'
        #add meterID
        parameter={'meterId':'""'}
        oauth1=OAuth1(client_key,client_secret,resource_owner_key,resource_owner_secret)
        r=requests.get(url=devices_url,params=parameter,auth=oauth1)
        response= r.json()
        power=response.get('values')['power']
        return power
def print_function():
        print(rest_power())

print_function()        
