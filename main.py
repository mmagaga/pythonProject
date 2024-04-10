import requests

# ввод номера персонажа


# код, использованный для получения номеров и имён персонажей
#for i in range(200, 700):
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