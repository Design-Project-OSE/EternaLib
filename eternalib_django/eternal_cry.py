import hashlib
import binascii

class eternalCry:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def hashing(nontext: str) -> str:
        nontext=eternalCry.salt(nontext)
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
        nontext=nontext[:len_text]+sec_text+third_text+first_text+nontext[len_text:]
        return nontext
    

        
    
    
