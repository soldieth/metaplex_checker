import requests

with open('wallets.txt', 'r') as f:
    wallets = f.read()
    wallets = wallets.split(sep='\n')
with open('alligable.txt', 'w') as f:
    with open('alligable.txt', 'a') as f1:
        for i in range((len(wallets))):
            r = requests.get(url=f'https://claim.metaplex.com/api/{wallets[i]}').json()
            if r['creator']:
                print(f"{wallets[i]} alligable for {r['creator']['amount']//1000000} tokens for creating")
                f1.write(f"{wallets[i]} alligable for {r['creator']['amount']//1000000} tokens for creating\n")
            if r['collector']:
                print(f"{wallets[i]} alligable for {r['collector']['amount']//1000000} tokens for collecting")
                f1.write(f"{wallets[i]} alligable for {r['collector']['amount'] // 1000000} tokens for collecting\n")
            if r['collector'] is None and r['creator'] is None:
                print(wallets[i], 'not alligable')
