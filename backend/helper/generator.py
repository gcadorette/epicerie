import hashlib
from constants import Constants

class Generator:
    _SALT = ''
    @staticmethod
    def generate_id(obj: object):
        dict_obj = obj.__dict__
        to_hash = Constants.salt
        for val in dict_obj.values():
            to_hash += str(val)
        return hashlib.sha256(to_hash.encode('utf-8')).hexdigest()
        