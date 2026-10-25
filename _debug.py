import struct
from Crypto.Cipher import AES

src = r"D:\CloudMusic\VipSongsDownload\蓝心羽 - 小宇.ncm"
CORE_KEY = bytes([0x68,0x7a,0x48,0x52,0x41,0x69,0x30,0x78,0x57,0x4e,0x73,0x68,0x35,0x77,0x51,0x6b])

with open(src, "rb") as f:
    f.read(8); f.read(2)
    key_len = struct.unpack("<I", f.read(4))[0]
    key_data = bytearray(f.read(key_len))
    for i in range(len(key_data)):
        key_data[i] ^= 0x63
    crypt = AES.new(CORE_KEY, AES.MODE_ECB)
    dk = crypt.decrypt(bytes(key_data))
    print("decrypted key raw hex:", dk.hex())
    print("decrypted key str:", dk)
