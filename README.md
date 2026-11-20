# Gemini ile PDF Belge Özetleme

Gemini API kullanarak PDF belgelerinden metin çıkarır ve Türkçe özet üretir. Özet; belgenin kısa amacı, ana maddeler, önemli sonuçlar veya kararlar ve dikkat edilmesi gereken noktaları içerir.

## Kurulum

Python sanal ortamı oluşturup etkinleştirin:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Gerekli paketleri kurun:

```powershell
python -m pip install -r requirements.txt
```

Proje klasöründe `.env` adlı dosya oluşturun ve Gemini API anahtarınızı ekleyin:

```env
GEMINI_API_KEY=API_ANAHTARINIZ
GEMINI_MODEL=gemini-3.6-flash
```

API anahtarınızı `.env` dosyasında saklayın. Bu dosya Git tarafından yok sayılır ve depoya yüklenmez.

## Çalıştırma

PDF dosyasının yolunu komuta ekleyin:

```powershell
python assignment_gemini_document_summary.py belge.pdf
```

PDF aynı klasörde değilse tam dosya yolunu kullanabilirsiniz. Metin katmanı olmayan taranmış PDF'lerde önce OCR gerekir.

## Gereksinimler

Python dosyası için kullanılan doğrudan bağımlılıklar `requirements.txt` içinde listelenmiştir.
