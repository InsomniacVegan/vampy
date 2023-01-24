from cls import vampire as vo
from json import JSONEncoder


class VampireEncoder(JSONEncoder):
    """Handle VAMPIRE datatypes"""

    def default(self, object):
        if type(object) in [
            vo.VParam,
            vo.VBlock,
            vo.VInput,
            vo.VMaterial,
            vo.VMaterialBlock,
        ]:
            return object.__dict__
        else:
            return super().default(object)
