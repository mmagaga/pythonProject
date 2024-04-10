import requests

# ввод номера персонажа


# код, использованный для получения номеров и имён персонажей
#for i in range(1, 5000):
#	n = str(i)
#	api = "https://anapioficeandfire.com/api/characters/" + n
#	
#	response_ch = requests.get(api)	
#	
#	responce_dict_ch = response_ch.json()
#	result_data_ch = responce_dict_ch
#
#	name_ch = result_data_ch["name"]
#
#	if result_data_ch["name"] and result_data_ch["culture"] and result_data_ch["born"] and result_data_ch["playedBy"]: 
#		print(i, "--", name_ch)
	

print("""
16 -- Margaery Tyrell
54 -- Aemon Targaryen
60 -- Aeron Greyjoy
148 -- Arya Stark
150 -- Asha Greyjoy
168 -- Barristan Selmy
181 -- Benjen Stark
208 -- Brandon Stark
223 -- Brynden Tully
232 -- Catelyn Stark
238 -- Cersei Lannister
326 -- Doran Martell
339 -- Eddard Stark
346 -- Edmure Tully
397 -- Galbart Glover
439 -- Grenn
506 -- Howland Reed
529 -- Jaime Lannister
547 -- Jeor Mormont
571 -- Jojen Reed
572 -- Jon Arryn
583 -- Jon Snow
585 -- Jon Umber
595 -- Jory Cassel
640 -- Loras Tyrell
649 -- Lothar Frey
667 -- Lyanna Mormont
692 -- Maege Mormont
735 -- Meera Reed
743 -- Melisandre
823 -- Petyr Baelish
849 -- Ramsay Snow
862 -- Renly Baratheon
884 -- Rickard Karstark
887 -- Rickard Stark
891 -- Rickon Stark
894 -- Robert Arryn
903 -- Robett Glover
933 -- Roose Bolton
937 -- Roslin Frey
954 -- Samwell Tarly
957 -- Sansa Stark
1022 -- Theon Greyjoy
1033 -- Torrhen Karstark
1043 -- Trystane Martell
1068 -- Vardis Egen
1079 -- Viserys Targaryen
1090 -- Walder Frey
1093 -- Walder Frey
1104 -- Waymar Royce
1166 -- Areo Hotah
1242 -- Brynden Rivers
1303 -- Daenerys Targaryen
1319 -- Davos Seaworth
1340 -- Doreah
1346 -- Drogo
1427 -- Gilly
1520 -- Illyrio Mopatis
1523 -- Irri
1548 -- Jhiqui
1560 -- Jorah Mormont
1650 -- Lyanna Stark
1666 -- Mance Rayder
1708 -- Mirri Maz Duur
1709 -- Missandei
1742 -- Mycah
1766 -- Nymeria Sand
1768 -- Obara Sand
1770 -- Oberyn Nymeros Martell
1979 -- Syrio Forel
2009 -- Timett son of Timett
2041 -- Tyene Sand
2126 -- Ygritte
""")


number = input("Введите номер персонажа: ")


api_url = "https://anapioficeandfire.com/api/characters/" + number

response = requests.get(api_url)   # Отправляем GET-запрос и сохраняем ответ в переменной response

if response.status_code == 200:    # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
    response_dict = response.json()
    result_data = response_dict

    name = result_data["name"]
    culture = result_data["culture"]
    born = result_data["born"]
    actor = result_data["playedBy"]

    print("Имя: ", name)
    print("Культура: ", culture)
    print("Дата рождения: ", born)
    print("Актёр в сериале:", actor)
else:
    print(response.status_code)