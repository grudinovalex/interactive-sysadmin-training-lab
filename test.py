from fabric import Connection


def process_list(c, process):
    return c.run(f" ps aux | grep -i {process}", hide=True).stdout.strip()

def alt_process_list(c, process):
    return c.run(" ps aux | grep -i '{process}'", hide=True).stdout.strip()


fedora = Connection(host = "trainee@localhost:2222", connect_kwargs = {"password" : "istl2024"})


print(process_list(fedora, '17804'))
print("========================")
print(alt_process_list(fedora, '17804'))