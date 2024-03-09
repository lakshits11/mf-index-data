import json
import subprocess

def read_json_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

index_list = read_json_file('index list.json')["d"]
index_mapping = read_json_file('index mapping.json')

index_dict = {item['Index_long_name'].upper(): item['Trading_Index_Name'] for item in index_mapping}

curl_command = """
curl --compressed --location 'https://www.niftyindices.com/Backpage.aspx/getTotalReturnIndexString' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0' \
--header 'Accept: application/json, text/javascript, */*; q=0.01' \
--header 'Accept-Language: en-US,en;q=0.5' \
--header 'Accept-Encoding: gzip, deflate, br' \
--header 'Content-Type: application/json; charset=utf-8' \
--header 'X-Requested-With: XMLHttpRequest' \
--header 'Origin: https://www.niftyindices.com' \
--header 'Connection: keep-alive' \
--header 'Referer: https://www.niftyindices.com/reports/historical-data' \
--header 'Cookie: ASP.NET_SessionId=dbytdbokotunxqrrhxwsuk23; ak_bmsc=75E6D167E511AD04B5F24873A32F00A8~000000000000000000000000000000~YAAQxI9lX8zKyfCNAQAAWTmYIhdjagQdt/7Psj300/HNVfqfDguk69z8gFH2+xRvapJnCK9N9cIBVGvbdVcuIFet+ME2n2mSExpZQxuv8aBtq0eZFbibd6skzkMfzKNwMLnRBEXxyZ4Uq5C7/YTERjm4SzvRq08l8wQ7jRn+bxKXFzbCLxz4Iq0y4Uq3CMEjcfED/CgWv+zGANS3QCdqNMxsowiD96L7kMNCPXcuIcRCO/OtFpUrLNRnsGIbh6MU1sH9jtwsZCcieyBakk9Qfas4hPZkYGFotTi20AdkUzwwMwob+8DCgkWr4JWPIZvtruxqw43YrFxoBc+IpkJNna8dzZ7eiR4zwA0hlvp3YLt5baCeo5kUTrJ49kFaPs7xU52ZwNMs; bm_sv=06F24F30ADE214DA2D834A0920328BBB~YAAQxI9lXwnLyfCNAQAAKtSYIhcZZzxINjTuJOndoW14jkrpA/An2LNNpmjybCtr7ZTlt9S8NvFjooq/h/E4P9jQvAHMX4FZR8bepJOKY5Hw1FIU9QQblntQFmnjsAT7VE0cB4lp5Cqhph11vQ8rPk/QB6Mor/gkvlvtMsccSKvXIMpuyDMMIsPE/Flc7oaHtlEfKDQhWmDU5/30tQt3xj02pGNfEhRXtNUWwemO3Ufk9wt42HfDFMUix6/uvZxcLeDj6Y18~1; bm_mi=773C461F1C36057972371F13120031E4~YAAQxI9lX9vKyfCNAQAAMVKYIhc/6Enabe6OcShwsYHKWowZnGSc6O8qKvNPi/SO0sAMjj/yZ3B7JFikreVEMciTrWglB80UZjMi9/qN6vLYe2sz9y6r57SpTyz0Z0jawAD/nHSiJRk0/w8PzHI/ynmdwZEfTgk22HlQbpwHtN6yEz4fsVx25FDxdJB00x6qXxrB0D5KeV+gb6QKmAJkSDNqdvjo3S0IJSBX2QsUQ9FAFOq3mWRVHkIiu/LwEbDMchd8h3fmuXvZfv9IkXIQHA2XnMYEATDkTJzVQs2TCl802m0pUFA6brycDjjFR3kI2auPaVSzV18VvWd/0X3udDUPH3+gZECy/hwQ~1' \
--header 'Sec-Fetch-Dest: empty' \
--header 'Sec-Fetch-Mode: cors' \
--header 'Sec-Fetch-Site: same-origin' \
--data '{
    "name": "<INDEX_NAME>",
    "startDate": "01-Jan-1995",
    "endDate": "08-Mar-2024"
}' \
--output "./index data/<INDEX_NAME_FILE>.json"
"""

for i, index in enumerate(index_list):
    print("fetching data for index: ", i, " of ", len(index_list), " - ", index['indextype'])
    index_name = index['indextype']
    trading_index_name = index_dict.get(index_name, index_name)
    command = curl_command\
        .replace('<INDEX_NAME>', trading_index_name)\
        .replace('<INDEX_NAME_FILE>', index_name)
    subprocess.run(command, shell=True, check=True)
    print()