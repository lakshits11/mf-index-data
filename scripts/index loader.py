import json
import subprocess

def read_json_file(filename):
    with open(filename, 'r', encoding='utf-8-sig') as file:
        return json.load(file)

index_list = read_json_file('../index list.json')["d"]
index_mapping = read_json_file('../index mapping.json')

index_dict = {item['Index_long_name'].upper(): item['Trading_Index_Name'] for item in index_mapping}

with open('curl to be used in python.sh', 'r') as file:
    curl_command = file.read()

for i, index in enumerate(index_list):
    print("fetching data for index: ", i, " of ", len(index_list), " - ", index['indextype'])
    index_name = index['indextype']
    trading_index_name = index_dict.get(index_name, index_name)
    command = curl_command\
        .replace('<INDEX_NAME>', trading_index_name)\
        .replace('<INDEX_NAME_FILE>', index_name)
    subprocess.run(command, shell=True, check=True)
    print()