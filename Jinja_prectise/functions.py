import requests


def get_blogs():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    contents = requests.get(url)
    return contents.json()


def get_age(user_name):
    url = "https://api.agify.io"
    params = {'name': user_name}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        name = data.get("name")
        age = data.get("age")
        return name, age
    except Exception as e:
        return None, None


def get_gender(user_name):
    url = "https://api.genderize.io"
    params = {'name': user_name}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        gender = data.get("gender")
        return gender
    except Exception as e:
        return None