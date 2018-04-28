*** Settings ***
Library  RoboNmap
Library  Collections

*** Variables ***
${TARGET}  example.com

*** Test Cases ***
Run Basic Port Scan
    nmap script scan  ${TARGET}  version_intense=3  file_export=nmap.txt
    nmap print results