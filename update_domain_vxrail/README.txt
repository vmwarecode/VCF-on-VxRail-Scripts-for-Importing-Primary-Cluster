INTRODUCTION:
------------

This module contains script files to create a cluster.


REQUIREMENTS:
------------

This module requires the following modules:

  * Python 3 Libraries
  * requests
  * sys
  * json
  * time

 * The scripts must be run outside sddc-manager environment.

 * DNS resolution must be done for sddc-manager.



USAGE:
-----

Sample specification file "update_domain_spec_vxrail.json" will be used for domain updation operation.
For more information on the provided sample file, please refer to API reference documentation.

Usage:  python3 update_domain_vxrail.py <domainId> <hostname> <username> <password>
