# Gemini ile PDF Belge Özetleme

Bu Python ödevi, PDF içindeki metni Gemini API'ye gönderir ve Türkçe bir özet üretir. PDF hangi dilde olursa olsun özet Türkçe hazırlanır.

Özet şu bölümleri içerir:
- Belgenin kısa amacı
- Ana maddeler
- Önemli sonuçlar veya kararlar
- Varsa dikkat edilmesi gereken noktalar

## Kurulum

Python sanal ortamı oluşturun:

```powershell
python -m venv .venv
```

Sanal ortamı etkinleştirin. CMD kullanıyorsanız:

```cmd
.venv\Scripts\activate.bat
```

PowerShell kullanıyorsanız:

```powershell
.\.venv\Scripts\Activate.ps1
```

Paketleri yükleyin:

```powershell
python -m pip install -r requirements.txt
```

## API anahtarı

Proje klasöründe `.env` adlı dosya oluşturup Gemini API anahtarınızı ekleyin:

```env
GEMINI_API_KEY=API_ANAHTARINIZ
GEMINI_MODEL=gemini-3.6-flash
```

`GEMINI_MODEL` isteğe bağlıdır. Atlanırsa kod varsayılan olarak `gemini-3.6-flash` kullanır. Gerçek API anahtarınızı GitHub'a yüklemeyin; `.env` dosyası `.gitignore` tarafından yok sayılır.

## Çalıştırma

PDF dosyasının yolunu komuta ekleyin:

```powershell
python assignment_gemini_document_summary.py belge.pdf
```

PDF aynı klasörde değilse tam dosya yolunu yazabilirsiniz. Metin katmanı bulunmayan, taranmış PDF'lerde önce OCR gerekir.
