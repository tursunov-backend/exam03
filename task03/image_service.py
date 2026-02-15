from api_client import APIClient


class ImageService:
    def __init__(self):
        self.api = APIClient()

    def fetch_random_image(self, image_type: str) -> str:
        if image_type == "dog":
            return self.api.get_dog_image()
        if image_type == "cat":
            return self.api.get_cat_image()
        if image_type == "fox":
            return self.api.get_fox_image()
        raise ValueError("Noto'g'ri image_type")
