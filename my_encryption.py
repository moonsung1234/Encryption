
from primePy import primes
import random

class Encrypted :
    @classmethod
    def __getEachotherDecimal(cls, _range, target) :
        is_break = False
        e = random.randint(2, _range - 1)

        for i in range(2, e + 1 if e < target else target + 1) :
            if e % i == 0 and target % i == 0 :
                is_break = True
                break

        if is_break or _range % e == 0 :
            return cls.__getEachotherDecimal(_range, target)

        else :
            return e
        
                

    @classmethod
    def createRSAKey(cls, round_of_decimal=100) :
        decimal_list = primes.upto(round_of_decimal)

        p, q = random.sample(decimal_list, 2)
        n = p * q
        on = (p - 1) * (q - 1)
        e = cls.__getEachotherDecimal(on, on) # 공개키
        d = None

        for i in range(1, on) :
            if (i * e) % on == 1 and i != e :
                d = i # 개인키
                break

        return (e, n), (d, n)

    @classmethod
    def encryptByPublicKey(cls, target_data, public_key) :
        return pow(target_data, public_key[0]) % public_key[1]

    @classmethod
    def decryptByPrivateKey(cls, encrypted_data, private_key) :
        return pow(encrypted_data, private_key[0]) % private_key[1]

"""
target_data = int(input("input data : "))

pub_key, pri_key = Encrypted.createRSAKey(round_of_decimal=1000)
encrypted_data = Encrypted.encryptByPublicKey(target_data, pub_key)
decrypted_data = Encrypted.decryptByPrivateKey(encrypted_data, pri_key)
        
print("enc data : ", encrypted_data)
print("dec data : ", decrypted_data)
"""