from constants import Constants
import hashlib

class Generator:
    _SALT = ''
    def generate_id(obj):
        dict_obj = obj.__dict__ 
        to_hash = Constants.SALT
        for val in dict_obj.values():
            to_hash += val
        return hashlib.sha256(to_hash.encode('utf-8')).hexdigest()