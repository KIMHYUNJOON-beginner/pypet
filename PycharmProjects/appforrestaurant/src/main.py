import googlemaps

# Google Maps API 키 (자신의 API 키로 변경)
API_KEY = "AIzaSyBXJeyHQG4SEG-tzg0MABC9OopQfu-KBHQ"  # "YOUR_API_KEY"를 실제 API 키로 교체하세요.
gmaps = googlemaps.Client(key=API_KEY)

# 예시: 도쿄 타워의 위치 정보 가져오기
location = gmaps.geocode("도쿄 타워")
print(location[0]['geometry']['location'])

class Restaurant:
    def __init__(self, name, address, menu, rating=0, reviews=None):
        self.name = name
        self.address = address
        self.menu = menu
        self.rating = rating
        self.reviews = reviews if reviews else []

    def add_review(self, review, rating):
        self.reviews.append({"review": review, "rating": rating})
        self.rating = sum([r['rating'] for r in self.reviews]) / len(self.reviews)  # 평균 평점 계산

