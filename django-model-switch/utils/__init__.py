class AttrDict(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__