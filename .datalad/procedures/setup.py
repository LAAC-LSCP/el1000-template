#!/usr/bin/env python3

import sys
import os
import re

import datalad.api
from datalad.distribution.dataset import require_dataset

import argparse

parser = argparse.ArgumentParser(description='setup the dataset siblings')
parser.add_argument('path', help = 'path')
parser.add_argument('--confidential', help = 'setup access to confidential remote', action = 'store_true')
parser.add_argument('--public', help = 'setup access to public remote', action = 'store_true')

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

url = datalad.api.siblings(name = 'origin', dataset = ds)[0]['url']
confidential_url = os.path.splitext(url)[0] + '-confidential.git'
public_url = os.path.splitext(url)[0] + '-public.git'

if args.confidential:

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
    
if args.public:

    datalad.api.siblings(
        name = 'public',
        dataset = ds,
        action = 'add',
        url = public_url
    )

    datalad.api.siblings(
        name = 'public',
        dataset = ds,
        action = 'configure',
        annex_wanted = '(include=annotations/vtc/converted/* or include=annotations/vcm/converted/* or include=annotations/alice/converted/* or include=annotations/alice/output/converted/* or include=annotations/its/converted/*) and exclude=**/confidential/*',
        annex_required = '(include=annotations/vtc/converted/* or include=annotations/vcm/converted/* or include=annotations/alice/converted/* or include=annotations/alice/output/converted/* or include=annotations/its/converted/*) and exclude=**/confidential/*'
    )

if args.public and args.confidential:
    datalad.api.siblings(
        name = 'origin',
        dataset = ds,
        action = 'configure',
        publish_depends = ['confidential','public']
    )
elif args.public:
    datalad.api.siblings(
        name = 'origin',
        dataset = ds,
        action = 'configure',
        publish_depends = 'public'
    )
elif args.confidential:
    datalad.api.siblings(
        name = 'origin',
        dataset = ds,
        action = 'configure',
        publish_depends = 'confidential'
    )
    

