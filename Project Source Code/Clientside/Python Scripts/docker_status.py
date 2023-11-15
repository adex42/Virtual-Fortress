import subprocess

def check_docker_status():
    """
    Check the status of Docker containers by running the 'docker ps' command.
    
    Returns:
        CompletedProcess: An object containing the result of the subprocess run.
    """
    command = "docker ps"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result

def docker_status():
    """
    Check the Docker container status and return a status code.
    
    Returns:
        int: 1 if there are running containers, 0 if there are no running containers.
    """
    docker_status = check_docker_status()
    rule = ""
    if docker_status == rule:
        return 0
    else:
        return 1
