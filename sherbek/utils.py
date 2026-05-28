import requests
from django.conf import settings

def send_sms_via_eskiz(phone_number, otp):
    url = "https://notify.eskiz.uz/api/message/sms/send"
    payload = {
        "mobile_phone": phone_number,
        "message": f"Sizning tasdiqlash kodingiz: {otp}",
        "from": "4546"
    }
    # Tokenni settings.py dan olish tavsiya etiladi
    headers = {"Authorization": f"Bearer {settings.ESKIZ_TOKEN}"}
    
    try:
        response = requests.post(url, data=payload, headers=headers)
        return response.status_code == 200
    except Exception as e:
        print(f"SMS yuborishda xatolik: {e}")
        return False