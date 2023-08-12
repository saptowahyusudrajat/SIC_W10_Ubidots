import requests

id = "64d70cc303c304000d7d4a1d"
API_URL = f"https://industrial.api.ubidots.com/api/v1.6/devices/{id}"
API_TOKEN = f"BBFF-ukR92Vl50IFsotNWPO420m0FRPmVxs"

def cek_koneksi():
    headers = {
        "X-Auth-Token": API_TOKEN
    }

    try:
        response = requests.get(API_URL, headers=headers)
        if response.status_code == 200:
            print("Connected to Ubidots")
        else:
            print("Failed to connect to Ubidots. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Connection error:", e)

if __name__ == "__main__":
    cek_koneksi()
