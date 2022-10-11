import requests

with open('wallets.txt', 'r') as f:
    wallets = f.read()
    wallets = wallets.split(sep='\n')
total_tokens = 0
with open('alligable.txt', 'w') as f:
    with open('alligable.txt', 'a') as f1:
        for i in range((len(wallets))):
            if len(wallets[i]) > 1:
                r = requests.get(url=f'https://claim.metaplex.com/api/{wallets[i]}').json()
                if r['creator']:
                    print(f"{wallets[i]} alligable for {r['creator']['amount']//1000000} tokens for creating")
                    f1.write(f"{wallets[i]} alligable for {r['creator']['amount']//1000000} tokens for creating\n")
                    total_tokens += r['creator']['amount']//1000000
                if r['collector']:
                    print(f"{wallets[i]} alligable for {r['collector']['amount']//1000000} tokens for collecting")
                    f1.write(f"{wallets[i]} alligable for {r['collector']['amount'] // 1000000} tokens for collecting\n")
                    total_tokens += r['collector']['amount'] // 1000000
                if r['collector'] is None and r['creator'] is None:
                    print(wallets[i], 'not alligable')
        f1.write(f'TOTAL TOKENS: {total_tokens}')
