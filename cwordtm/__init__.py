# __init__.py
#
# Root package
#
# Copyright (c) 2024 CWordTM Project 
# Author: NLP 2024 <nlp202403@gmail.com>
#
# Updated: 20 March 2024
#
# URL: https://github.com/nlp202403/cwordtm.git
# For license information, see LICENSE.TXT

#: Package version information
from .version import __author__
from .version import __copyright__
from .version import __credits__
from .version import __version__
from .version import __email__
from .version import __url__
from .version import __docs__

from .meta import addin_all

#: Add the additional features (timing and showing code) to all functions
#:   of the module "cwordtm"
addin_all()
