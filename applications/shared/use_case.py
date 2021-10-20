from abc import abstractmethod, ABCMeta
#from config.config_loader import Config
#from src.shared import response_object


class UseCase(object):
    __metaclass__ = ABCMeta

    def execute(self, request_object):
        if not request_object:
            return "No Request Object"
        #    return response_object.CommonResponse.build_from_invalid_request_object(request_object)
        try:
            return self.process_request(request_object)
        except Exception as exc:
            return str(exc)
            #if Config.DEBUG: raise exc
            #return response_object.CommonResponse.build_common_message(
            #    "{}: {}".format(exc.__class__.__name__, "{}".format(exc)), Config.SYSTEM_ERROR
            #)

    @abstractmethod
    def process_request(self, request_object): pass
