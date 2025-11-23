import requests, time

def track_contract_creators():
    print("BSC Contract Creator Tracker — who launches the next 1000x (or rug)")
 вполне    seen = set()
    while True:
        r = requests.get("https://api.bscscan.com/api?module=account&action=txlist&address=0x0000000000000000000000000000000000000000&sort=desc")
        for tx in r.json()["result"][:30]:
            txid = tx["hash"]
            if txid in seen or tx["contractAddress"] == "": continue
            seen.add(txid)
            creator = tx["from"]
            contract = tx["contractAddress"]
            print(f"NEW CONTRACT DEPLOYED!\n"
                  f"Creator: {creator}\n"
                  f"Contract: {contract}\n"
                  f"Block: {tx['blockNumber']}\n"
                  f"https://bscscan.com/tx/{txid}\n"
                  f"https://bscscan.com/address/{contract}\n"
                  f"→ This wallet just birthed a new token. Track it early.\n"
                  f"{'✨'*25}")
        time.sleep(3.5)

if __name__ == "__main__":
    track_contract_creators()
