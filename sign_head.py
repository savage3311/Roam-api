import hmac
from datetime import datetime
from aut import token,secret

now = datetime.utcnow()
timestamp = now.strftime("%Y-%m-%dT%H:%M:%SZ")

def digest_mod():
    stringToSign = bytes(token + timestamp, 'utf-8')
    tokenSigning = hmac.new(key=secret, msg=stringToSign, digestmod='SHA1')
    return tokenSigning.hexdigest()

fp_auth_authorization = token + ":" + digest_mod()
fp_auth_timestamp = timestamp
headers = {"Content-Type": "application/json; charset=utf-8","fp-auth-authorization": fp_auth_authorization,"fp-auth-timestamp": fp_auth_timestamp}
