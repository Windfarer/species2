from weixin import WXAPPAPI
from weixin.lib.wxcrypt import WXBizDataCrypt
from django.conf import settings

wx_api = WXAPPAPI(appid=settings.WEIXIN.APP_ID,
                  app_secret=settings.WEIXIN.APP_SECRET)

def get_session_info(code):
    session_info = api.exchange_code_for_session_key(code=code)
    return session_info

def get_user_info(session_key):
    crypt = WXBizDataCrypt(wx_api.appid, session_key)
    user_info = crypt.decrypt(encrypted_data, iv)
    return user_info