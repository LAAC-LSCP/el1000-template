#!/usr/bin/env python3

import sys
import os

import datalad.api
from datalad.distribution.dataset import require_dataset

ds = require_dataset(
    sys.argv[1],
    check_installed=True,
    purpose = 'configuration'
)

datalad.api.siblings(
    name = 'origin',
    dataset = ds,
    action = 'configure',
    annex_wanted = '(include=*) and (exclude=**/confidential/*)',
    annex_required = '(include=*) and (exclude=**/confidential/*)'  
)