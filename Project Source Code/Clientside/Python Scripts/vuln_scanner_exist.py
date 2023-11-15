import subprocess

def validate_result_exists(process_type, result, rule):
    """
    Validate if a given result matches a rule based on process type.

    Args:
        process_type (int): 1 for a match, 0 for a non-match.
        result (str): The result to validate.
        rule (str): The rule to compare the result with.

    Returns:
        int: 1 if the result matches the rule, 0 otherwise.
    """
    if process_type == 1:
        if result == rule:
            return 1
        else:
            return 0
    else:
        if result != rule:
            return 1
        else:
            return 0

def run_commands(command):
    """
    Run a shell command and return the captured output as a string.

    Args:
        command (str): The shell command to execute.

    Returns:
        str: The captured output of the command.
    """
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

def vuln_scanner(rule_file, rule):
    """
    Scan for vulnerabilities based on rules and command files.

    Args:
        rule_file (str): The file containing rules and commands.
        rule (str): The rule to validate the results against.

    Prints:
        str: HTML code for checkboxes indicating matched rules.
    """
    with open(rule_file) as file:
        for line in file:
            if line:
                code = line.split("|||")
                command = code[1].rstrip()
                result = run_commands(command)
                if rule_file == "output_not_found.txt":
                    process_type = 1
                else:
                    process_type = 0
                validated_result = validate_result_exists(process_type, result, rule)
                if validated_result == 1:
                    print(f"{code[0]} <input type='checkbox'></input> <br>")
