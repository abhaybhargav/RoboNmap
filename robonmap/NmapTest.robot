*** Settings ***
Library  ./RoboNmap.py
Library  Collections

*** Variables ***
${TARGET}  example.com

*** Test Cases ***
Run Basic Port Scan
    nmap default scan  ${TARGET}  file_export=nmap.txt
    nmap print results