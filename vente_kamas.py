# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 17:49:27 2022

@author: Joseph
"""

import discord
import time
from datetime import datetime
import requests
from requests.structures import CaseInsensitiveDict

def spam_kamas(status):
    url = "https://vente.tryandjudge.com/ScriptPHP/verification.php"
    
    headers = CaseInsensitiveDict()
    headers["authority"] = "vente.tryandjudge.com"
    headers["accept"] = "/"
    headers["accept-language"] = "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7"
    headers["content-type"] = "application/x-www-form-urlencoded; charset=UTF-8"
    headers["origin"] = "https://vente.tryandjudge.com/"
    headers["referer"] = "https://vente.tryandjudge.com/dofuskamas.php"
    headers["sec-fetch-dest"] = "empty"
    headers["sec-fetch-mode"] = "cors"
    headers["sec-fetch-site"] = "same-origin"
    headers["sec-gpc"] = "1"
    headers["user-agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
    headers["x-requested-with"] = "XMLHttpRequest"
    
    data = "devise=EUR&tester=serveurcontentprices"
    
    
    resp = requests.post(url, headers=headers, data=data)
    lignes = resp.text.split("</tr>")
    res = []
    for ligne in lignes[1:]:
        splitted = ligne.split('<td>')
        if len(splitted) < 2:
            continue
        res.append({
            'name': splitted[1].split('</')[0],
            'price': splitted[2].split(' EUR')[0],
            'available': 'Stock complet' not in splitted[3],
        })
    status_update = status
    for x in res:
        if x['available'] == False:
            if res[13]['available'] == True:
                if status == False:
                    status_update = True
            else:
                if status == True:
                    status_update = False
            break
    now = datetime.now()
    if (status != status_update and (now.hour < 2 or now.hour > 9)):
        if status_update == False:
            return False
        else:
            return True
    time.sleep(3)
    spam_kamas(status_update)

class Bot(discord.Client):
    def __init__(self):
        super().__init__()
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
    async def on_message(self, message):
        if (spam_kamas(False) == True):
            message.send("STOCK DISPO SUR MERIANA")
        else:
            message.send("Stock complet sur Meriana")
if(__name__ == "__main__"):
    bot = Bot()
    bot.run("OTg1ODEzNzEyODI2OTMzMjc4.GeAjPq.HWDz4-Ux5iMLh2QCvZZ1NL2LcG_vbRpYO7DMME")
    
                                        