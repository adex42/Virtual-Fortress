import subprocess  #This library allows for execution of shell commands from within python code
def get_security_patches():
  """
    get_security_patches function returns a formatted output of the shell command 'apt-get update'
    
    Returns:
        String of available updates for selected ubuntu system.
    """
  output = subprocess.check_output(['sudo apt-get', 'update']).decode('utf-8')  #decode method converts byte string to a readable regular string
  security_patches = [line for line in output.splitlines() if line.startswith('Security update')]  
  #The splitlines method is a string method in Python that splits a string into a list of lines
  #The above line of code splits the output of the 'apt-get update' bash command whenever 'Security update' is encountered
  return security_patches
def show_update_available():
  """
    show_update_available calls the previous function and displays the value to the user
    
    Returns:
        String of available updates for selected ubuntu system to the user
    """
  security_patches = get_security_patches()  #Output of get_security_patches function is stored here
  if not security_patches :  #If no security patches available
      print("No updates available")
  else:  #If security patches available
      print('The following security patches are available for your Ubuntu device:')
      for security_patch in security_patches:
        print(security_patch)  #Print all available patches on the screen

'''
For line 10, example is the string "Hello i am adit Hello i am Ishaan Hello i am Gaurav".
The string is to be split whenever the word Hello is encountered which is the equivalent of 'Security Update' in our code.
The output will be as shown below:
Hello i am adit
Hello i am ishaan
Hello i am Gaurav
'''
