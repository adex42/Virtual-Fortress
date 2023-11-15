import re
import subprocess

def is_vmware_running():
    """
    Check if VMware virtualization software is running.

    This function checks if the VMware virtualization software is running by examining the list of active processes.

    Returns:
        bool: True if VMware is running, False otherwise.
    """
    try:
        # Use 'ps' command to list all active processes
        output = subprocess.check_output(['ps', '-A'])

        # Search for 'vmware-vmx' or 'vmware-svga' in the process list
        return bool(re.search(b'vmware-vmx|vmware-svga', output))
    except subprocess.CalledProcessError:
        # An error occurred while executing 'ps', indicating that VMware is not running
        return False

def vmware_status():
    """
    Get the VMware status.

    This function checks if VMware is running by calling the 'is_vmware_running()' function.
    
    Returns:
        int: 1 if VMware is running, 0 if it's not running.
    """
    if is_vmware_running():
        return 1
    else:
        return 0
