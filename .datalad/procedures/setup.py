#!/usr/bin/env python3

import sys
import os
import re

import datalad.api
from datalad.distribution.dataset import require_dataset

import argparse

parser = argparse.ArgumentParser(description='setup the dataset siblings')
parser.add_argument('path', help = 'path')
parser.add_argument('--confidential', help = 'setup access to confidential data', action = 'store_true')

args = parser.parse_args()

ds = require_dataset(
    args.path,
    check_installed = True,
    purpose = 'configuration'
)

datalad.api.siblings(
    name = 'origin',
    dataset = ds,
    action = 'configure',
    annex_wanted = '(include=*) and (exclude=**/confidential/*)',
    annex_required = '(include=*) and (exclude=**/confidential/*)'
)

if args.confidential:
    url = datalad.api.siblings(name = 'origin', dataset = ds)[0]['url']
    confidential_url = os.path.splitext(url)[0] + '-confidential.git'

    datalad.api.siblings(
        name = 'confidential',
        dataset = ds,
        action = 'add',
        url = confidential_url
    )

    datalad.api.siblings(
        name = 'confidential',
        dataset = ds,
        action = 'configure',
        annex_wanted = 'include=**/confidential/*',
        annex_required = 'include=**/confidential/*'
    )

    datalad.api.siblings(
        name = 'origin',
        dataset = ds,
        action = 'configure',
        publish_depends = 'confidential'
    )
    

