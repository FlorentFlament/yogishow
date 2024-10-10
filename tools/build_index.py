#!/usr/bin/env python3

import os
import sys
import json

def main():
    fnames = os.listdir(sys.argv[1])
    print(json.dumps(fnames, indent=4))

main()
