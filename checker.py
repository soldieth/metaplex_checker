import requests

with open('wallets.txt', 'r') as f:
    wallets = f.read()
    wallets = wallets.split(sep='\n')
for i in range((len(wallets))):
    r = requests.get(url=f'https://claim.metaplex.com/api/{wallets[i]}').json()
    if r['creator']:
        print(f"{wallets[i]} alligable for {r['creator']['amount']//1000000} tokens")
    elif r['collector']:
        print(f"{wallets[i]} alligable for {r['collector']['amount']//1000000} tokens")
    else:
        print(wallets[i], 'not alligable')
