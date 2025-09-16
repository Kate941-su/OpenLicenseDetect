from enum import Enum

class OSSType(Enum):
    APACHE_2_0 = "Apache-2.0"
    MIT = "MIT"
    GPL_3_0 = "GPL-3.0"
    GPL_2_0 = "GPL-2.0"
    BSD_3_CLAUSE = "BSD-3-Clause"
    BSD_2_CLAUSE = "BSD-2-Clause"
    ISC = "ISC"
    LGPL_3_0 = "LGPL-3.0"
    LGPL_2_1 = "LGPL-2.1"
    MPL_2_0 = "MPL-2.0"
    EPL_2_0 = "EPL-2.0"
    CDDL_1_1 = "CDDL-1.1"
    CC0_1_0 = "CC0-1.0"
    AGPL_3_0 = "AGPL-3.0"
    UNLICENSE = "Unlicense"
    OTHER = "Other"