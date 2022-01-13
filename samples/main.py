'''
:Authors:         Shashank Agrawal
:Date:            5/2016
'''

from charm.toolbox.pairinggroup import PairingGroup, GT
from ABE.ac17 import AC17CPABE

class ABEOperations:

    def __init__(self) -> None:
        # instantiate a bilinear pairing map
        self.__pairing_group = PairingGroup('MNT224')

        # AC17 CP-ABE under DLIN (2-linear)
        self.__cpabe = AC17CPABE(self.__pairing_group, 2)

    def setup(self):
         # run the set up, pk is public key, msk is master secret key
        (pk, msk) = self.__cpabe.setup()
        self.__pk = pk
        self.__msk = msk
        # TODO: save private key and master key if flags are present

    def keygen(self, attr_list):
        # key is distributed to content receivers
        return self.__cpabe.keygen(self.__pk, self.__msk, attr_list)

    # make a random message
    def msg(self):
        return self.__pairing_group.random(GT)

    def encrypt(self, policy_str, msg):
        return self.__cpabe.encrypt(self.__pk, msg, policy_str)

    def decrypt(self, ctxt, key):
        return self.__cpabe.decrypt(self.__pk, ctxt, key)



def main(inputfile, outputfile, encrypt, pk_file, msk_file, key_file, debug):

    ops = ABEOperations()
    ops.setup()
    key = ops.keygen(['ONE', 'TWO', 'THREE'])
   
    # choose a random message
    msg = ops.msg()

    # generate a ciphertext
    ctxt = ops.encrypt('((ONE and THREE) and (TWO OR FOUR))', msg)

    # decryption
    rec_msg = ops.decrypt(ctxt, key)

    if debug:
        if rec_msg == msg:
            print ("Successful decryption.")
        else:
            print ("Decryption failed.")



import sys, getopt   

if __name__ == "__main__":

    main()
    exit()

    # skip all the stuff below for now

    inputfile = ''
    outputfile = ''
    # operations are: generate, key, encrypt, decrypt
    operation = None
    keyfile = ''

    try:
        opts, args = getopt.getopt(sys.argv,"hdei:o:k:",["ifile=","ofile=","encrypt=", "keyfile="])
    except getopt.GetoptError:
        print('main.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('main.py -d <direction> -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-k", "--keyfile"):
            keyfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-e", "--encrypt"):
            encrypt = arg
        elif opt in ("-d", "--debug"):
            debug = arg
    print('Input file is '), inputfile
    print('Output file is '), outputfile
    main(inputfile, outputfile, op, pk_file, msk_file, key_file, debug)

