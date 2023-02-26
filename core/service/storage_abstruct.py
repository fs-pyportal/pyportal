from core.internal.errors import MethodNotImplemented

class StorageAbstruct:
    '''
    Required minimal number of methods that file service must contain
    '''
    
    def connect(credential):
        raise MethodNotImplemented

    def upload(content, name):
        raise MethodNotImplemented

    def download(file_id):
        raise MethodNotImplemented

    def stat(file_id):
        raise MethodNotImplemented

    def rename(file_id, new_name):
        raise MethodNotImplemented

    def delete(file_id):
        raise MethodNotImplemented

    def set_attribute(file_id, name, value):
        raise MethodNotImplemented

    def get_attribute(file_id, name):
        raise MethodNotImplemented
