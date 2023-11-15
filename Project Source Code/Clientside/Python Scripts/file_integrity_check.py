# The integrity_check function checks the integrity of a rule file by comparing the hash values stored in the "file_integrity_check.txt" file with the 
# calculated hash values of the corresponding files. It reads each line of the file, splits it into the file_name and hash_value, and calculates the hash 
# value of the file_name using the SHA-256 algorithm. If the calculated hash value does not match the stored hash value, it prints a message indicating a 
# mismatch and returns -1. Otherwise, if all hash values match, it returns 1.
import hashlib
def integrity_check():
    """
    Check the integrity of the rule file by comparing the hash values
    stored in the "file_integrity_check.txt" file with the calculated
    hash values of the corresponding files.

    :return: Returns 1 if all hash values match, -1 if any hash value does not match.
    :rtype: int
    :raises: None
    :Example:

    >>> integrity_check()
    The hash values do not match.
    -1
    """
    with open("file_integrity_check.txt", "r") as f:
        for line in f:
            file_name, hash_value = line.split()
            file_hash = hashlib.sha256(open(file_name, "rb").read()).hexdigest()
            if file_hash != hash_value:
                print("The hash values do not match.")
                return -1
    return 1

