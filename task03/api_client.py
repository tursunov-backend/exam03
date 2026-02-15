import requests


class APIClient:
    def get_dog_image(self) -> str:
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        response.raise_for_status()
        return response.json()["message"]

    def get_cat_image(self) -> str:
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        response.raise_for_status()
        return response.json()[0]["url"]

    def get_fox_image(self) -> str:
        response = requests.get("https://randomfox.ca/floof/")
        response.raise_for_status()
        return response.json()["image"]
