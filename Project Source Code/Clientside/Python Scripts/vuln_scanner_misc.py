from subprocess import run, PIPE
#subprocess module in Python provides methods for running external commands
#PIPE class is used to create pipes for connecting the streams formed by the subprocess

def validate_result_match(result, rule):
    """
    Validate if a given rule is present in the stdout or stderr streams of the result.

    Args:
        result: The result of the subprocess execution.
        rule(string): The rule to search for within the captured streams.

    Returns:
        integer: 1 if the rule is not found in either stdout or stderr,
        0 if the rule is found in either of the streams.
    """
    found = result.stdout.find(rule)    #if the rule is not found, -1 is returned, the index of the first alphabet otherwise 
    found2 = result.stderr.find(rule)   #same as the above but for stderr file
    if found == -1 and found2 == -1:
        return 1    #if rule not found in either stdout or stderr
    else:
        return 0    #if rule found in either stdout or stderr


def run_commands(command):
    """
    Run a command as a subprocess and capture its output and error streams.
    The command is executed in a shell environment with the 'shell' parameter set to True.

    Args:
        command: This variable contains the command that is to be executed.

    Returns:
        CompletedProcess: An object that is composed of the execution of the command including
        the standard output and standard error.
    """
    result = run(command, shell=True, stdout=PIPE, stderr=PIPE, text=True)
    # 'text=True' ensures output is treated as text and not as bytes increasing readability
    return result


def vuln_scanner(rule_file): #match = 0 if you dont need it to match , match = 1 if you need it to be in the statement
    """
    Scan the result of a command for the presence of a rule.

    This function runs a given command as a subprocess, captures its output
    and error streams, and then checks for the presence of a specified rule
    within the captured streams (using other functions defined in this file)

    Returns:
        The command if rule match not satisfied.
        Nothing otherwise
    """
    with open(rule_file) as file:
        for line in file:
            if line:
                code = line.split("|||")
                result = run_commands(code[1])
                validated_result = validate_result_match(result, code[2])
                match = code[3].rstrip()
                if validated_result == 1 and match == "1":
                    print(f"{code[0]}<input type='checkbox'></input><br>")
                elif validated_result == 0 and match == "0":
                    print(f"{code[0]}<input type='checkbox'></input><br>")

