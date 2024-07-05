from fabric import Connection

def process_list(c, process):
    return c.run(f" ps aux | grep -i {process}", hide=True).stdout.strip()

def alt_process_list(c, process):
    return c.run(" ps aux | grep -i '{process}'", hide=True).stdout.strip()

# fedora = Connection(host = "trainee@localhost:2222")
# print(process_list(fedora, '17804'))
# print("\n========================\n")
# print(alt_process_list(fedora, '17804'))

fedora = Connection(host = "trainee@localhost:2222", connect_kwargs = {"key_filename" : [r"/Users/sasa/.ssh/id_rsa"]})
output = fedora.run("find / -maxdepth 3", hide=True).stderr

print(output)