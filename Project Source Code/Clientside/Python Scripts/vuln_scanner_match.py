"""
The vuln_scanner function takes two arguments: rule_file and rule. It reads each line from the rule_file, treating each line as a shell command. For each command, 
it executes the command using the run_commands function, capturing the result. The validate_result_match function is then called to check if the rule keyword is 
present in the output (stdout or stderr) of the command. If the keyword is not found in the output, indicating  that the command failed to meet the expected 
criteria specified by the  rule, the command is printed. In the given example, the rule keyword is "Failed," so if the grep command in the rule_file does not find 
the expected dpattern in the /etc/shadow file, the command "grep -Eq '^root:$[0-9]' /etc/shadow" will be printed, indicating that the password entry for the root 
user did not follow the expected pattern.

"""

from subprocess import run, PIPE

def validate_result_match(result, rule):
    """
    Validate if the given 'rule' keyword exists in the stdout or stderr of the 'result'.

    Args:
        result (CompletedProcess): The result of a command execution.
        rule (str): The keyword to search for in the command output.

    Returns:
        int: 1 if the rule is not found in stdout or stderr, 0 if found.
    """
    found = result.stdout.find(rule)
    found2 = result.stderr.find(rule)
    if found == -1 and found2 == -1:
        return 1
    else:
        return 0

def run_commands(command):
    """
    Run the given shell 'command' and capture the stdout and stderr.

    Args:
        command (str): The shell command to execute.

    Returns:
        CompletedProcess: The result of the command execution.
    """
    result = run(command, shell=True, stdout=PIPE, stderr=PIPE, text=True)
    return result

def vuln_scanner(rule_file, rule):
    """
    Scan a rule_file containing shell commands for the given 'rule' keyword in the output.

    Args:
        rule_file (str): The path to the file containing shell commands.
        rule (str): The keyword to search for in the command output.

    Returns:
        None: Prints commands from the rule_file where the 'rule' keyword was not found in output.
    """
    with open(rule_file) as file:
        for line in file:
            if line:
                code = line.split("|||")
                command = code[1].rstrip()
                result = run_commands(command)
                validated_result = validate_result_match(result, rule)
                if validated_result == 1:
                    print(f"{code[0]}<input type='checkbox'></input><br>")


"""
run (subprocess.run):
The run function from the subprocess module in Python allows you to run shell commands and capture their output, exit status, and other information. Here are the 
key points:

-->Command Execution: It takes a shell command as input and executes it.
-->Flexibility: Can run both simple and complex commands with arguments and options.
-->Capturing Output: Captures the standard output and standard error streams of the executed command.
-->Exit Status: Returns a CompletedProcess object that includes the exit code of the command.
-->Text Mode: By default, run operates in text mode, allowing you to work with strings as input and output.
-->Blocking: The function blocks until the command completes.

PIPE (subprocess.PIPE):
The PIPE constant from the subprocess module is used to create pipes for handling the standard input, standard output, and standard error streams in subprocess 
calls. Important points about PIPE:

-->Pipe Creation: Used as a value for the stdout and stderr parameters when calling run. It creates a new pipe for the corresponding stream.
-->Capturing Output: When a pipe is used for stdout or stderr, the output of the command is captured and can be accessed from the CompletedProcess object.
-->Communication: Allows interaction with the subprocess through the pipes, enabling input and output communication between the parent and child processes.
-->Text or Bytes: Can work with both text and binary data, depending on the encoding used.
-->Convenient: Provides a clean way to work with the input and output of subprocesses.

"""
