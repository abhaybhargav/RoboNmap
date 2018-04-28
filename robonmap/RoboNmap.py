import os
from libnmap.process import NmapProcess
from libnmap.parser import NmapParser, NmapParserException
from robot.api import logger


class RoboNmap(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        '''
        Nmap Initialize the API
        '''
        self.results = None

    def nmap_default_scan(self, target, file_export = None):
        '''
        Runs a basic nmap scan on nmap's default 1024 ports. Performs the default scan
        - file_export is an optional param that exports the file to a txt file with the -oN flag

        Examples:
        | nmap default scan  | target | file_export |


        '''
        target = str(target)
        if file_export == None:
            nmproc = NmapProcess(target)
        else:
            nmproc = NmapProcess(target, '-oN {0}'.format(file_export), safe_mode=False)
        rc = nmproc.run()
        if rc != 0:
            raise Exception('EXCEPTION: nmap scan failed: {0}'.format(nmproc.stderr))
        try:
            parsed = NmapParser.parse(nmproc.stdout)
            print parsed
            self.results = parsed
        except NmapParserException as ne:
            print 'EXCEPTION: Exception in Parsing results: {0}'.format(ne.msg)


    def nmap_all_tcp_scan(self, target, file_export = None):
        '''
        Runs nmap scan against all TCP Ports with version scanning. Options used -Pn -sV -p1-65535
        Examples:
        | nmap default scan  | target | file_export |

        file_export is an optional param that exports the file to a txt file with the -oN flag
        '''
        target = str(target)
        if file_export == None:
            nmproc = NmapProcess(target, '-p1-65535 -sV')
        else:
            cmd = '-p1-65535 -sV -oN {0}'.format(file_export)
            nmproc = NmapProcess(target, cmd, safe_mode=False)
        rc = nmproc.run()
        if rc != 0:
            raise Exception('EXCEPTION: nmap scan failed: {0}'.format(nmproc.stderr))
        try:
            parsed = NmapParser.parse(nmproc.stdout)
            print parsed
            self.results = parsed
        except NmapParserException as ne:
            print 'EXCEPTION: Exception in Parsing results: {0}'.format(ne.msg)

    def nmap_specific_udp_scan(self, target, portlist, file_export = None):
        '''
        Runs nmap against specified UDP ports given in the portlist argument.
        Arguments:
            - ``target``: IP or the range of IPs that need to be tested
            - ``portlist``: list of ports, range of ports that need to be tested. They can either be comma separated or separated by hyphen
            example: 121,161,240 or 1-100
            - ``file_export``: is an optional param that exports the file to a txt file with the -oN flag
        Examples:
        | nmap specific udp scan  | target | portlist | file_export |
        '''
        target = str(target)
        if file_export == None:
            nmproc = NmapProcess(target, '-p1-65535 -sV')
        else:
            cmd = '-sU -sV -p {0} -oN {1}'.format(portlist, file_export)
            nmproc = NmapProcess(target, cmd, safe_mode=False)
        rc = nmproc.run()
        if rc != 0:
            raise Exception('EXCEPTION: nmap scan failed: {0}'.format(nmproc.stderr))
        try:
            parsed = NmapParser.parse(nmproc.stdout)
            print parsed
            self.results = parsed
        except NmapParserException as ne:
            print 'EXCEPTION: Exception in parsing results: {0}'.format(ne.msg)


    def nmap_os_services_scan(self, target, portlist=None, version_intense = 0, file_export = None):
        '''
        Runs
        Arguments:
            - ``target``: IP or the range of IPs that need to be tested
            - ``portlist``: list of ports, range of ports that need to be tested. They can either be comma separated or separated by hyphen
            example: 121,161,240 or 1-100
            - ``version_intense``: Version intensity of OS detection
            - ``file_export``: is an optional param that exports the file to a txt file with the -oN flag
        Examples:
        | nmap os services scan  | target | portlist | version_intense | file_export |
        '''
        target = str(target)
        if portlist:
            nmap_proc_cmd = "-Pn -sV --version-intensity {0} -p {1}".format(portlist, version_intense)
        else:
            nmap_proc_cmd = "-Pn -sV --version-intensity {0}".format(portlist)

        if file_export:
            nmap_proc_cmd += " -oN {0}".format(file_export)

        nmproc = NmapProcess(target, nmap_proc_cmd, safe_mode=False)
        rc = nmproc.run()
        if rc != 0:
            raise Exception('EXCEPTION: nmap scan failed: {0}'.format(nmproc.stderr))
        try:
            parsed = NmapParser.parse(nmproc.stdout)
            print parsed
            self.results = parsed
        except NmapParserException as ne:
            print 'EXCEPTION: Exception in parsing results: {0}'.format(ne.msg)


    def nmap_script_scan(self, target, portlist=None, version_intense="0", script_name=None, file_export = None):
        '''
        Runs nmap with the -sC arg or the --script arg if script_name is provided. Options used are: -sV --version-intensity <default:0> -sC|--script=<script_name>
        Arguments:
            - ``target``: IP or the range of IPs that need to be tested
            - ``portlist``: list of ports, range of ports that need to be tested. They can either be comma separated or separated by hyphen
            example: 121,161,240 or 1-100
            - ``version_intense``: Version intensity of OS detection
            - ``script_name``: Script Name that needs to be referenced
            - ``file_export``: is an optional param that exports the file to a txt file with the -oN flag
        Examples:
        | nmap script scan  | target | portlist | version_intense | script_name |
        '''
        target = str(target)
        if portlist and script_name:
            nmap_proc_cmd = "-Pn -sV --version-intensity {0} --script={1} -p {2}".format(version_intense, script_name, portlist)
        elif portlist and not script_name:
            nmap_proc_cmd = "-Pn -sV --version-intensity {0} -sC -p {1}".format(version_intense, portlist)
        elif script_name and not portlist:
            raise Exception('EXCEPTION: If you use specific script, you have to specify a port')
        else:
            nmap_proc_cmd = "-Pn -sV --version-intensity {0} -sC".format(version_intense)

        if file_export:
            nmap_proc_cmd += " -oN {0}".format(file_export)

        nmproc = NmapProcess(target, nmap_proc_cmd, safe_mode=False)
        rc = nmproc.run()
        if rc != 0:
            raise Exception('EXCEPTION: nmap scan failed: {0}'.format(nmproc.stderr))
        try:
            parsed = NmapParser.parse(nmproc.stdout)
            print parsed
            self.results = parsed
        except NmapParserException as ne:
            print 'EXCEPTION: Exception in parsing results: {0}'.format(ne.msg)



    def nmap_print_results(self):
        '''
        Retrieves the results of the most recent results
        Examples:
        | nmap print results |
        '''
        for scanned_hosts in self.results.hosts:
            logger.info(scanned_hosts)
            logger.info("  PORT     STATE         SERVICE")
            for serv in scanned_hosts.services:
                pserv = "{0:>5s}/{1:3s}  {2:12s}  {3}".format(
                    str(serv.port),
                    serv.protocol,
                    serv.state,
                    serv.service)
                if len(serv.banner):
                    pserv += " ({0})".format(serv.banner)
                logger.info(pserv)
                if serv.scripts_results:
                    for output in serv.scripts_results:
                        logger.info("\t Output: {0}, Elements: {1}, ID: {2}".format(output['output'], output['elements'], output['id']))



