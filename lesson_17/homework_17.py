# ===== Variant 1: import module =====
import os
import sys
import json
import math

# ===== Variant 2: import module as alias =====
import datetime as dt
import random as rnd
import pathlib as pl
import logging as log

# ===== Variant 3: from module import name =====
from collections import Counter
from itertools import chain
from statistics import mean
from functools import reduce

# ===== Variant 4: from module import name as alias (installed libs) =====
from requests import get as http_get
from dateutil.parser import parse as dt_parse
from re import compile as re_compile
from pandas import DataFrame as DF

# ===== Variant 5: own modules =====
from custom_modules import calc_utils
from custom_modules.calc_utils import add
from custom_modules.text_utils import shout
import custom_modules.text_utils as tu


if __name__ == "__main__":
    print("Imports OK")
    print(add(2, 3))
    print(shout("hello"))
