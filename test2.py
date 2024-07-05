import paramiko
#
#
# hostname = "localhost"
# username = "trainee"
# password = "istl2024"
#
# # Create an SSH client instance
# client = paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# # Connect to the server
# client.connect(hostname, port=2222, username=username, password=password)
#
# # Execute commands on the server
# stdin, stdout, stderr = client.exec_command("find / -maxdepth 2")
# stdin.close()
# stdout_output = stdout.read()
# stdout_output = stdout_output.decode("utf-8").strip()
# stderr_err = stderr.read()
# stderr_err = stderr_err.decode("utf-8").strip()
#
#
# # Print the output of the command
# print(f"this is the standard output of command:\n{stdout_output}")
# print("")
# print(f"this is the standard error of command:\n{stderr_err}")
#
#
# stdout_output
# # Close the SSH connection
# client.close()

def cmd(command):
    # Define server variables
    hostname = "localhost"
    username = "trainee"
    password = "istl2024"

    # Create an SSH client instance & connect to server
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port=2222, username=username, password=password)

    # Execute commands on the server
    stdin, stdout, stderr = client.exec_command(command)
    stdin.close()
    stdout_output = stdout.read()
    stderr_output = stderr.read()
    stdout_output = stdout_output.decode("utf-8").strip()
    stderr_output = stderr_output.decode("utf-8").strip()

    # Close SSH connection
    client.close()
    return stdout_output, stderr_output

stdout, stderr = cmd("find / -maxdepth 2")

print(stderr)