# Xractz
# IndoSec

from requests import Session
import re, sys
s = Session()
try:
        print("\n\n * SMS Gratis by BlueZRX - IndoSec\n * Gunakan kode negara (ex: 628xxxxx)\n")
        no = int(input(" Nomor : "))
        msg = input(" Pesan : ")
except:
        print("\n\t* Cek nomermu atau pesanmu! *")
        sys.exit()

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 9; Redmi Note 6 Pro Build/PKQ1.180904.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36',
    'Referer': 'https://alpha.payuterus.biz/'
}

bypass = s.get("https://alpha.payuterus.biz/?a=keluar", headers=headers).text
key = re.findall(r'value="(\d+)"', bypass)[0]
jml = re.findall(r'<span>(.*?) = </span>', bypass)[0]
captcha = eval(jml.replace("x", "*").replace(":", "/"))

data = {
        'nohp':no,
        'pesan':msg,
        'captcha':captcha,
        'key':key
}

send = s.post("https://alpha.payuterus.biz/send.php", headers=headers, data=data).text

if 'SMS Gratis Telah Dikirim' in send:
        print(f"\n  [ Pengiriman sukses ]\n  [ {no} : {msg} ]\n")
elif 'MAAF....!' in send:
        print("\n  [ Mohon tunggu 15 menit untuk mengirim pesan yg sama ]\n")
else:
        print("\n  [ Pengiriman gagal ]\n")

