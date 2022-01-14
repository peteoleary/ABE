from charm.schemes.pkenc.pkenc_cs98 import CS98
from charm.toolbox.eccurve import prime192v1
from charm.toolbox.ecgroup import ECGroup

groupObj = ECGroup(prime192v1)
pkenc = CS98(groupObj)

(pk, sk) = pkenc.keygen()

M = b'Hello World!'
ciphertext = pkenc.encrypt(pk, M)

message = pkenc.decrypt(pk, sk, ciphertext)
