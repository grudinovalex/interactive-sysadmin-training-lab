import paramiko

# Executes 'command' on the ISTL machine, returns standard output & standard error
def cmd(command):
    # Define server variables
    hostname = "istl"
    username = "trainee"
    password = "istl2024"

    # Create an SSH client instance & connect to server
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port=22, username=username, password=password)

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

if __name__ == "__main__":
    main()