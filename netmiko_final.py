from netmiko import ConnectHandler
from pprint import pprint

device_ip = "10.0.15.181"
username = "admin"
password = "cisco"

device_params = {
    "device_type": "cisco_ios",
    "ip": device_ip,
    "username": username,
    "password": password,
}


def gigabit_status():
    ans = ""
    with ConnectHandler(**device_params) as ssh:
        up = 0
        down = 0
        admin_down = 0
        interface_statuses = []
        result = ssh.send_command("show interfaces status", use_textfsm=True)
        for status in result:
            if status['interface'].startswith('GigabitEthernet'):
                status_str = status['status'].lower()
                interface_name = status['interface']
                
                if status_str == "up":
                    up += 1
                    interface_statuses.append(f"{interface_name} up")
                elif status_str == "down":
                    down += 1
                    interface_statuses.append(f"{interface_name} down")
                elif "admin" in status_str:
                    admin_down += 1
                    interface_statuses.append(f"{interface_name} administratively down")
        status_str = ", ".join(interface_statuses)            
        ans = f"{status_str} -> {up} up, {down} down, {admin_down} administratively down"
        pprint(ans)
        return ans
