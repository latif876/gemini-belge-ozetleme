"""
Gemini API ile PDF Belge Özetleme

PDF dosyasındaki metni okuyarak Gemini API'ye gönderir ve Türkçe bir özet
oluşturur. Özet; belgenin kısa amacını, ana maddelerini, önemli sonuç veya
kararlarını ve varsa dikkat edilmesi gereken noktaları içerir.

Adımlar:
    1. Gerekli kütüphaneleri içe aktar.
    2. .env dosyasından API anahtarını ve model ayarını oku.
    3. Gemini istemcisini oluştur ve model parametrelerini ayarla.
    4. Komut satırından PDF dosyasının yolunu al.
    5. PDF içindeki metni sayfa sayfa oku.
    6. PDF bulunamazsa, açılamazsa veya metin okunamazsa anlaşılır hata göster.
    7. Türkçe özet için prompt hazırla.
    8. PDF metnini Gemini API'ye gönder.
    9. Düşük temperature ile daha tutarlı özet üret.
    10. Özeti terminalde düzenli biçimde göster.

Kurulum:
    pip install google-genai pymupdf python-dotenv

API anahtarı:
    Proje klasöründe .env dosyası oluştur ve şu satırı ekle:
    GEMINI_API_KEY=API_ANAHTARINIZ

Çalıştırma:
    python assignment_gemini_document_summary.py belge.pdf
"""

# 1. Gerekli kütüphaneleri içe aktar
import os
import sys
from pathlib import Path

import pymupdf
from dotenv import load_dotenv
from google import genai
from google.genai import types


# 2. .env dosyasından API anahtarını ve model ayarını oku
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model_name = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY bulunamadı. Proje klasöründeki .env dosyasını kontrol edin."
    )

print("API anahtarı bulundu.")


# 3. Gemini istemcisini oluştur ve model parametrelerini ayarla
client = genai.Client(api_key=api_key)

generation_config = types.GenerateContentConfig(
    temperature=0.2,
    max_output_tokens=2500,
)


# 4. Komut satırından PDF dosyasının yolunu al
if len(sys.argv) < 2:
    raise ValueError(
        "PDF dosyasının yolunu belirtin. Örnek: "
        "python assignment_gemini_document_summary.py belge.pdf"
    )

pdf_path = Path(sys.argv[1])

if not pdf_path.is_file():
    raise FileNotFoundError(f"PDF dosyası bulunamadı: {pdf_path}")


# 5 ve 6. PDF içindeki metni oku; açılmazsa veya metin yoksa hata göster
try:
    with pymupdf.open(pdf_path) as pdf:
        pdf_text = "\n\n".join(page.get_text("text") for page in pdf)
except Exception as error:
    raise ValueError(f"PDF açılamadı veya okunamadı: {error}") from error

if not pdf_text.strip():
    raise ValueError(
        "PDF içinde okunabilir metin bulunamadı. "
        "Dosya taranmış bir PDF olabilir; bu durumda OCR gerekir."
    )


# 7. Türkçe özet için prompt hazırla
prompt = f"""
Belge hangi dilde olursa olsun, özeti Türkçe olarak hazırla.
Özeti yalnızca belgede yer alan bilgilere dayanarak oluştur.
Belgede olmayan bilgi veya sonuçları ekleme.

Özeti şu başlıklarla düzenle:
1. Belgenin kısa amacı
2. Ana maddeler
3. Önemli sonuçlar veya kararlar
4. Varsa dikkat edilmesi gereken noktalar

Belge metni:
{pdf_text}
"""


# 8 ve 9. Metni Gemini'ye gönder ve ayarlanan model parametrelerini kullan
response = client.models.generate_content(
    model=model_name,
    contents=prompt,
    config=generation_config,
)

summary = response.text

if not summary:
    raise ValueError("Gemini boş bir yanıt döndürdü.")


# 10. Özeti terminalde göster
print("\n===== BELGE ÖZETİ =====\n")
print(summary)
