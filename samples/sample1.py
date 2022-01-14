from typing_extensions import ParamSpecKwargs
from charm.schemes.pkenc.pkenc_cs98 import CS98
from charm.toolbox.eccurve import prime192v1
from charm.toolbox.ecgroup import ECGroup
from charm.toolbox.paddingschemes import PKCS7Padding

from pudb import set_trace; set_trace()

groupObj = ECGroup(prime192v1)
pkenc = CS98(groupObj)

(pk, sk) = pkenc.keygen()

M = b'Hello World!'

pad = PKCS7Padding()

M_pad = pad.encode(bytes(M), 20)

ciphertext = pkenc.encrypt(pk, M_pad)

message = pkenc.decrypt(pk, sk, ciphertext)

print(pad.decode(message))
