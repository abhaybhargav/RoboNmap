## RoboNmap

Robot Framework Library for the Nmap Port and Vulnerability Scanner. 

### Keywords Implemented

##### Default Nmap Scan against a target
| nmap default scan  | target |

##### Default Nmap Scan against all TCP Ports
| nmap all tcp scan  | target |

##### Default Nmap UDP Scan with a Portlist Argument
Runs nmap against specified UDP ports given in the portlist argument.

Arguments:

- ``target``: IP or the range of IPs that need to be tested.
- ``portlist``: list of ports, range of ports that need to be tested. They can either be comma separated or separated by hyphen, example: 121,161,240 or 1-100
Examples:
- `| nmap specific udp scan  | target | portlist |`


##### Nmap OS Services Scan

Arguments:

- ``target``: IP or the range of IPs that need to be tested
- ``portlist``: list of ports, range of ports that need to be tested. They can either be comma separated or separated by hyphen example: 121,161,240 or 1-100
- ``version_intense``: Version intensity of OS detection
Examples:
`| nmap os services scan  | target | portlist | version_intense |`

##### Nmap Script Scan
Runs nmap with the `-sC` arg or the `--script` arg if `script_name` is provided. Options used are: `-sV --version-intensity <default:0> -sC|--script=<script_name>`

Arguments:

- ``target``: IP or the range of IPs that need to be tested
- ``portlist``: list of ports, range of ports that need to be tested. They can either be comma separated or separated by hyphen example: 121,161,240 or 1-100
- ``version_intense``: Version intensity of OS detection
- ``script_name``: Script Name that needs to be referenced
Examples:
`| nmap script scan  | target | portlist | version_intense | script_name |`

##### Print Nmap Scan Results
Retrieves the results of the current nmap scan results
Examples:

`| nmap print results |`
