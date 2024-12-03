import socket, getpass, platform, os, subprocess, re, shutil

def get_cpu_name():
    cmd = "cat /proc/cpuinfo"
    cpu_info = subprocess.check_output(cmd, shell=True).decode().strip()
    for line in cpu_info.split("\n"):
        if "model name" in line:
            return re.sub(".*model name.*:", "", line, 1).removeprefix(" ")

def get_total_ram():
    cmd = "cat /proc/meminfo"
    cpu_info = subprocess.check_output(cmd, shell=True).decode().strip()
    for line in cpu_info.split("\n"):
        if "MemTotal" in line:
            return re.sub(".*MemTotal.*:", "", line, 1).removeprefix("        ").removesuffix(" kB")

def get_total_disk():
    total, used, free = shutil.disk_usage("/")
    return str((total // (2**30)))

def get_shell():
    cmd = "echo $SHELL"
    shell = subprocess.check_output(cmd, shell=True).decode().removesuffix("\n")
    return shell

hostname = socket.gethostname()
user = getpass.getuser()
os = platform.platform()
cpu = get_cpu_name()
ram = get_total_ram()
disk = get_total_disk()
shell = get_shell()


print("MEOFETCH")

print("hostname: " + hostname)
print("user: " + user)
print("os: " + os)
print("cpu: " + cpu)
print("ram: " + ram)
print("disk: " + disk)
print("shell: " + shell)
print("R.I.P. neofetch")