from abc import ABCMeta, abstractmethod


class BaseGenerator(ABCMeta):
    @abstractmethod
    def get_classname(cls):
        raise NotImplementedError()

    @abstractmethod
    def get_prefix(cls):
        raise NotImplementedError()

    @abstractmethod
    def get_attr(cls):
        raise NotImplementedError()

    @abstractmethod
    def get_suffix(cls):
        raise NotImplementedError()

    @abstractmethod
    def stream_params(cls):
        raise NotImplementedError()

    @abstractmethod
    def generate_field(cls):
        raise NotImplementedError()
