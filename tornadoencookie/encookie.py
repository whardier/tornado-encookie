from Crypto.Cipher import AES
import base64

class EncookieManager(object):

    BLOCK_SIZE = 32
    PADDING = '\0'

    def __init__(self, handler):
        self.handler = handler
        self.secret = ''
        self.__setup_encookie()

    def __setup_encookie(self):
        self.__setup_settings()
        self.cipher = AES.new(self.secret)

    def __setup_settings(self):
        self.handler.require_setting("encookie_secret", "encrypted cookies")
        self.secret = self.handler.settings.get('encookie_secret')

    def _pad(self, value):
        return value + (self.BLOCK_SIZE - len(value) % self.BLOCK_SIZE) * self.PADDING

    def _encrypt(self, value):
        return base64.b64encode(self.cipher.encrypt(self._pad(value))).decode('utf-8')

    def _decrypt(self, value):
        return self.cipher.decrypt(base64.b64decode(value.encode('utf-8'))).decode('utf-8').rstrip(self.PADDING)

    def get_cookie(self, name, default=None):
        encrypted_value = self.handler.get_cookie(name)
        if not encrypted_value:
            return default
        return self._decrypt(encrypted_value)

    def set_cookie(self, name, value, domain=None, expires=None, path="/",
                   expires_days=None, **kwargs):
        encrypted_value = self._encrypt(value)
        self.handler.set_cookie(name, encrypted_value, domain=domain, expires=expires, path=path,
                                expires_days=expires_days, **kwargs)

    def set_secure_cookie(self, name, value, expires_days=30, **kwargs):
        encrypted_value = self._encrypt(value)
        self.handler.set_secure_cookie(name, encrypted_value,
                        expires_days=expires_days, **kwargs)

    def get_secure_cookie(self, name, value=None, max_age_days=31):
        if value is None:
            value = self.handler.get_cookie(name)
        encrypted_value = self.handler.get_secure_cookie(name, value, max_age_days=max_age_days)
        if encrypted_value:
            return self._decrypt(encrypted_value.decode('utf-8'))
        else:
            return None

class EncookieMixin(object):
    @property
    def encookie(self):
        '''
        Returns an encookie instance
        '''

        return create_mixin(self, '__encookie_manager', EncookieManager)

class ConfigurationError(Exception):
    pass

def create_mixin(context, manager_property, manager_class):
    if not hasattr(context, manager_property):
        setattr(context, manager_property, manager_class(context))
    return getattr(context, manager_property)

