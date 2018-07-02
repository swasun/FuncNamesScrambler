from crypter import Crypter

from Crypto.Hash import MD5

class Scrambler(object):

    def __init__(self, parser, password):
        self.crypter = Crypter(password)
        self.parser = parser

    def scramble_func_names(self):
        scrambled = dict()

        for func_name in self.parser.func_names:
            scrambled[func_name] = self._scramble(func_name)

        return scrambled

    def _scramble(self, str):
        data = str.encode()
        encrypted = self.crypter.encrypt(data)
        hasher = MD5.new()
        hasher.update(encrypted)
        return hasher.hexdigest()