"""
This code imports modules for file integrity checking, patch management, and vulnerability scanning. 
It checks if configuration files have been modified, then scans for miconfigurations based on expected outputs
defined in rules files, checking for things like open ports, weak permissions, outdated packages. 
It also checks for available security updates and prints any findings or failures.
"""

import patch_management  # This module allows us to check for new security patches available
import vuln_scanner_match  # This module allows us to match the output of our bash scripts with a desired outcome
import vuln_scanner_exist  # This module allows us to see if a particular service exists or not
import vuln_scanner_misc  # This module allows us to check if a particular term is present in the result of our a bash
import file_integrity_check
import docker_status
import vmware_status

def main():
    integrity_score = file_integrity_check.integrity_check()# Checking to see if the rule files have been modified or not
    if integrity_score == 1:  # The integrity score 1 here implies that the files have not been modified
        is_docker_running = docker_status.docker_status()
        is_vmware_running = vmware_status.vmware_status()
        if is_docker_running : 
            print("""<!DOCTYPE html>
            <html>
            <head>
            <title>Vulnerability Report</title>
            </head>

            <body bgcolor="#ffffff", text = "#000000">""")
            print("<center><h1 style='background-color : #ffffff ;border: solid 3px #000; padding: 5px;'>Docker Vulnerability Report</h1></center>")
            print("<a href='https://www.cisecurity.org/cis-benchmarks'>Download the offical CIS documentation</a>")
            print("<h2>Things to configure :</h2>")
            print("<h3>Refer to the documentation for the following errors :</h3> ")
            vuln_scanner_exist.vuln_scanner("Docker_output_not_found_rules.txt", "")  # This line checks for controls that should not
            # be giving us an output when checked for
            print("<h3>Refer to the documentation for the following errors : </h3>")
            vuln_scanner_exist.vuln_scanner("Docker_output_found_rules.txt", "")  # This line checks for controls that should
            # be giving us an output when checked for
            vuln_scanner_misc.vuln_scanner("Docker_misc.txt")
            print("<h3>Patch Management:</h3>")
            print("</body></html>")
        
        elif is_vmware_running:
            print("""<!DOCTYPE html>
            <html>
            <head>
            <title>Vulnerability Report</title>
            </head>

            <body bgcolor="#ffffff", text = "#000000">""")
            print("<center><h1 style='background-color : #ffffff ;border: solid 3px #000; padding: 5px;'>VMware Vulnerability Report</h1></center>")
            print("<a href='https://www.cisecurity.org/cis-benchmarks'>Download the offical CIS documentation</a>")
            print("<h2>Things to configure :</h2>")
            print("<h3>Refer to the documentation for the following errors : </h3>")
            vuln_scanner_exist.vuln_scanner("VMware_output_found_rules.txt", "")  # This line checks for controls that should
            # be giving us an output when checked for
            print("<h3>Remove the following applications: </h3>")
            vuln_scanner_match.vuln_scanner ("VMware_ok_not_installed.txt", "no")  # This line checks for controls that should
            # be giving us an output which includes the word "no" when checked for
            print("<h3>Install the following: </h3>")
            vuln_scanner_match.vuln_scanner("VMware_ok_installed.txt", "installed")  # This line checks for controls that should
            # be giving us an output which includes the word "installed" when checked for ie the
            print("</body></html>")
        
        else: 
            print("""<!DOCTYPE html>
            <html>
            <head>
            <title>Vulnerability Report</title>
            </head>
            <body bgcolor="#ffffff", text = "#000000">""")
            print("<center><h1 style='background-color : #ffffff ;border: solid 3px #000; padding: 5px;'>Vulnerability Report</h1></center>")
            print("<a href='https://www.cisecurity.org/cis-benchmarks'>Download the offical CIS documentation</a>")
            print("<h2>Things to configure :</h2>")
            print("<h3>Refer to the documentation for the following errors :</h3> ")
            vuln_scanner_exist.vuln_scanner("output_not_found_rules.txt", "")  # This line checks for controls that should not
            # be giving us an output when checked for
            print("<h3>Refer to the documentation for the following errors : </h3>")
            vuln_scanner_exist.vuln_scanner("output_found_rules.txt", "")  # This line checks for controls that should
            # be giving us an output when checked for
            print("<h3>Remove the following applications: </h3>")
            vuln_scanner_match.vuln_scanner ("ok_not_installed.txt", "no")  # This line checks for controls that should
            # be giving us an output which includes the word "no" when checked for
            print("<h3>Install the following: </h3>")
            vuln_scanner_match.vuln_scanner("ok_installed.txt", "installed")  # This line checks for controls that should
            # be giving us an output which includes the word "installed" when checked for ie the
            print("<h3>Enable the following: </h3>")
            vuln_scanner_match.vuln_scanner("enabled.txt", "enabled")  # This line checks for controls that should
            # be giving us an output which includes the word "enabled" when checked for ie the services should be enabled
            print("<h3>Access to non root user:</h3>")
            vuln_scanner_match.vuln_scanner("root_user.txt", "Uid: (    0/    root)   Gid: (    0/    root)")  # This line checks for controls that should
            # be giving us an output which includes the words "Uid: (    0/    root)   Gid: (    0/    root)" when checked for ie only the root user should have the access to it
            print("<h3>There is no failed in the output:</h3>")
            vuln_scanner_match.vuln_scanner("failed.txt", "Failed")  # This line checks for controls that should
            # be giving us an output which includes the word "enabled" when checked for ie the services should be enabled
            print("<h3>Misc:</h3>")
            vuln_scanner_misc.vuln_scanner("misc.txt")
            print("<h3>Patch Management:</h3>")
            patch_management.show_update_available()  # This line runs the show update available function from patch management and allows us to see if there are any new security updates
            print("</body></html>") 
    else:
        print("Integrity Check Failed")  # Incase a rule file has been modified , we stop the scan

if __name__ == "__main__":
    main()
