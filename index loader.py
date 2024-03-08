import json
import subprocess

def read_json_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

index_list = read_json_file('index list.json')["d"]
index_mapping = read_json_file('index mapping.json')

index_dict = {item['Index_long_name']: item['Trading_Index_Name'] for item in index_mapping}

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
--header 'Cookie: ASP.NET_SessionId=dbytdbokotunxqrrhxwsuk23; ak_bmsc=A6283F794B93AE5EA818531F9A54A130~000000000000000000000000000000~YAAQxI9lX4rhrfCNAQAAb1NHHxeN15lIM//ovDGaJ5tLhxIpYYI73bSCXyG9R5/2487cgfAHs4IoKgaVlh6UWS7hotAhx7rZogwNAsYuj9vEXt7U3lZPqQ4rpc89NXS3KeMRC39TMScD/nxw+9ECMKAmh1uNOxsyaBXQPJPZPbkxmeuYL5ZN/pJWfmRUmYD4C33OnIFWbQKaUDbChsmTvJtf6mtKn15rrFNERwMAbOeIKsSrLbhPmhHkLj98c3hpN9hTKw+Igug6TBBuDPr86yuF2+V68R3pVNDuFoATRhvv7hZnFyW4q62rUo52r+BPZd+65BLrX+cc88dttEsaUqbXAdmvWq7M23ewjC2maDXkyHs5L3OGRcAt1jrjClaszJ+TlvEX; bm_sv=560DE094CEA76FC7963F8DB12ED2D74E~YAAQxI9lX7HqrfCNAQAAA6JHHxe/c3wiA5NsNVuCm+q0ytIXVwTPJsxMq3C4LHuiSzPf3yJsJhiB4R9cqY8JMhaXKiDq2NiuHtsEDolREGO0q+iP3zXH/p+gAisjTgxm9dw9pZeJnarV0WLZKosLih/R1Z/zvTsrtvoE8BBIPDm6uo/xFr23Lw2G0y5TPi87LSk8dRdNKUu9/hhUICeDMU6Mur9CNy0uM5267FHvCNmZj+rqzWK7CvoUn9/4hkDqZbJSXHvr~1; bm_sv=CA87A949AA1FEF255B95E9BF8D905C31~YAAQxI9lXxGCrvCNAQAAnlFWHxfAxvdAaAHkKuUdxWt0TjmaUXKgV5PhDa1yTR514j84CknUglTdKwI06GhNST8vyrsPWPTK1XNoJy6j0H4BClgCErVmo8/l3Ciy7fHPg5LthCCH0DUQrvToGdj0sT/I62eW5lQH1tfclk5uOhGqF9L7nbHAYJxI1IMDbIOzNjSZKhrLK6toQ0P5vtE3ozg9R1DEM3SugsO3mn1moogkFB9QHvCDuDAr0i67QVmG38Knf0zz~1' \
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
        .replace('<INDEX_NAME_FILE>', index_name.replace('/', ':'))
    subprocess.run(command, shell=True, check=True)
    print()