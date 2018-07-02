import re

class Replacer(object):

    def __init__(self, source_code, func_names):
        self.source_code = source_code
        self.func_names = func_names

    def replace(self):
        replaced = re.sub(r'({})'.format("|".join(sorted(self.func_names.keys(), reverse=True))),
            lambda x: self.func_names[x.group(1)], self.source_code)
        return replaced