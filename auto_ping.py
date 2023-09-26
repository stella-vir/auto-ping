import subprocess
import paramiko
import telnetlib3

def send_ping(ip_address):
    try:
        result = subprocess.run(['ping', '-c', '4', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10, text=True)
        if "bytes from" in result.stdout:
            return True
        else:
            return False
    except Exception as e:
        return False

def check_ssh_port(ip_address, port):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip_address, port, timeout=10)
        ssh.close()
        return True
    except Exception as e:
        return False

def check_telnet_port(ip_address, port):
    try:
        with telnetlib3.TelnetClient() as telnet:
            telnet.connect(ip_address, port)
            return True
    except Exception as e:
        return False

if __name__ == "__main__":
    ip_address = "192.168.0.1"
    ssh_port = 22
    telnet_port = 23

    if send_ping(ip_address):
        print(f"Ping to {ip_address} successful.")
    else:
        print(f"Ping to {ip_address} failed.")

    if check_ssh_port(ip_address, ssh_port):
        print(f"SSH port {ssh_port} is open on {ip_address}.")
    else:
        print(f"SSH port {ssh_port} is closed on {ip_address}.")

    if check_telnet_port(ip_address, telnet_port):
        print(f"Telnet port {telnet_port} is open on {ip_address}.")
    else:
        print(f"Telnet port {telnet_port} is closed on {ip_address}.")
