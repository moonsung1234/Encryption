
# Encryption (only with RSA)

*****

## main.ipynb

```python 
>  from my_encryption import Encrypted as En

>  target_data = int(input("input data : "))
input data : 100

>  pub_key, pri_key = Encrypted.createRSAKey(round_of_decimal=1000)
>  encrypted_data = Encrypted.encryptByPublicKey(target_data, pub_key)
>  decrypted_data = Encrypted.decryptByPrivateKey(encrypted_data, pri_key)
>  print("enc data : ", encrypted_data)
>  print("dec data : ", decrypted_data)
23818
100
```
