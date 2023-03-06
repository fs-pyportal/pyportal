from core.internal.errors import MethodNotImplemented

class Storage:
    '''
    Wrapper for interact to actual storage
    '''

    def __init__():
        raise MethodNotImplemented

    def connect(self, credential):
        raise MethodNotImplemented

    def upload(self, content, name):
        raise MethodNotImplemented

    def download(fself, file_id):
        raise MethodNotImplemented

    def stat(self, file_id):
        raise MethodNotImplemented

    def rename(self, file_id, new_name):
        raise MethodNotImplemented

    def delete(self, file_id):
        raise MethodNotImplemented

    def set_attribute(self, file_id, name, value):
        raise MethodNotImplemented

    def get_attribute(self, file_id, name):
        raise MethodNotImplemented
