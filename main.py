import requests

# ввод номера персонажа

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