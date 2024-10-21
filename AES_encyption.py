from cryptography.hazmat.primitives.ciphers import  Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def get_AESkey_from_qrng(qrng_output):
    with open(qrng_output, 'r') as file:
        qrng_bits = file.read().strip()

    # extract the first 256 bits (32 bytes) for AES-256
    aes_key = qrng_bits[:256]

    # convert the binary string to bytes
    aes_key_bytes = int(aes_key, 2).to_bytes(32, 'big') # 32 bytes for 256 bits
    return aes_key_bytes


def aes_encrypt(plaintext, key):
    """
   Generate a random IV ( Initialization Vector), block of random or pseudo-random data used as
   an input to the first block of encryption in block cipher modes. It used to be ensure that the same
   plaintext will encrypt to different ciphertexts even when the same key is used, provides semantic security.
    """
    iv = os.urandom(16)
    backend = default_backend()
    # create AES cipher in CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend)
    encyptor = cipher.encryptor()

    # padding plaintext to be a multiple of block size (AES block size is 16 bytes)
    padding_length = 16 - (len(plaintext)%16)
    padded_plaintext = plaintext + (chr(padding_length) * padding_length).encode()

    ciphertext = encyptor.update(padded_plaintext) + encyptor.finalize()

    return iv, ciphertext

aes_key = get_AESkey_from_qrng("random_bits.txt")
plaintext = b"this is a plaintext"
iv, ciphertext = aes_encrypt(plaintext, aes_key)

print("IV:", iv.hex())
print("Ciphertext:", ciphertext.hex())

