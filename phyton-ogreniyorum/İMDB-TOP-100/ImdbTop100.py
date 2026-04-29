# PROJE #15
#
# Python ile imdb top 100 film listesini (film adı, yılı, yönetmeni ve başrol oyuncuları) çekmek 
#
# Bu projeyi ChatGPT vb. Yapay Zeka araçlarından destek alarak ve Python bilginizi kullanarak yapınız!
import requests
from bs4 import BeautifulSoup
import json
import time

headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0"
}

# IMDb Top 250 ana sayfası
main_url = "https://www.imdb.com/chart/top"
response = requests.get(main_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# JSON içeren <script> etiketlerini bul
scripts = soup.find_all("script", type="application/ld+json")

# İlk 100 filmin adlarını ve linklerini topla
movie_links = []
for s in scripts:
    try:
        data = json.loads(s.string)
        if isinstance(data, dict) and "itemListElement" in data:
            for item in data["itemListElement"][:100]:
                movie = item["item"]
                title = movie.get("name")
                url = movie.get("url", "")  # ✔️ URL zaten tam, ekleme yapma
                movie_links.append((title, url))
            break
    except Exception as e:
        print("Ana sayfa JSON hatası:", e)

print("🎬 Toplam film bulundu:", len(movie_links))

# Her film için detay sayfasına girerek bilgi topla
for i, (title, url) in enumerate(movie_links, 1):
    try:
        print(f"\n⏳ {i}. {title} detay sayfası yükleniyor: {url}")
        time.sleep(0.5)  # IMDb'yi yormamak için küçük bekleme

        detail_response = requests.get(url, headers=headers)
        detail_soup = BeautifulSoup(detail_response.text, "html.parser")

        # JSON verisini çek
        script_tag = detail_soup.find("script", type="application/ld+json")
        if not script_tag:
            raise ValueError("JSON script tag bulunamadı")

        json_data = json.loads(script_tag.string)

        # Yapım yılı
        year = json_data.get("datePublished", "Yıl yok")

        # Yönetmen(ler)
        directors = json_data.get("director", [])
        if isinstance(directors, dict):  # tek yönetmense dict döner
            directors = [directors]
        director_names = [d.get("name", "") for d in directors]

        # Başrol oyuncuları
        actors = json_data.get("actor", [])[:2]
        actor_names = [a.get("name", "") for a in actors]

        # Yazdır
        print(f"{i}. {title} ({year})")
        print(f"   🎬 Yönetmen: {', '.join(director_names) if director_names else 'Yok'}")
        print(f"   👤 Başrol: {', '.join(actor_names) if actor_names else 'Yok'}")

    except Exception as e:
        print(f"❌ Hata: {e}")
        print(f"{i}. {title} - [Detaylar alınamadı] ❌")













