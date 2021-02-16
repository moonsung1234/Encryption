
# Encryption (only with RSA)

*****

## main.ipynb

> python```target_data = int(input("input data : "))```
> ```python pub_key, pri_key = Encrypted.createRSAKey(round_of_decimal=1000)```
> ```python encrypted_data = Encrypted.encryptByPublicKey(target_data, pub_key)```
> ```python decrypted_data = Encrypted.decryptByPrivateKey(encrypted_data, pri_key)```
> ```python print("enc data : ", encrypted_data)```
> ```python print("dec data : ", decrypted_data)```
