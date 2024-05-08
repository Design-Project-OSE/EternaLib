import hashlib
import binascii

class __cryptography__:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def hashing(nontext: str) -> str:
        hash_algorithm = hashlib.sha256()
        hash_algorithm.update(nontext.encode('utf-8'))
        hash_text = hash_algorithm.digest()
        hash_hex_text = binascii.hexlify(hash_text)
        return hash_hex_text.decode('utf-8')

        
    def salt(nontext:str)->str:
        len_text=len(nontext)//2
        first_text=nontext[:2]
        sec_text=nontext[-2:]
        third_text=nontext[len_text+1:len_text+3:1]
        nontext=third_text+nontext+sec_text+first_text
        return nontext
    
cry=__cryptography__
passw="12345fena552895"
salti=cry.salt(passw)
pse=cry.hashing(salti)
print("pass="+passw+"\nsalt="+salti+"\nhash="+pse)
        

        
    
    
