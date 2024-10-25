import json
import requests
requests.packages.urllib3.disable_warnings()

# Router IP Address is 10.0.15.181-184
api_url = "https://10.0.15.181/restconf/data"

# the RESTCONF HTTP headers, including the Accept and Content-Type
# Two YANG data formats (JSON and XML) work with RESTCONF 
headers = {
    "Accept": "application/yang-data+json",
    "Content-type": "application/yang-data+json",
}
basicauth = ("admin", "cisco")
studentID = "65070037"

def create():
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": f"Loopback{studentID}",
            "description": f"{studentID}",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [{"ip": "172.30.37.1", "netmask": "255.255.255.0"}]
            },
            "ietf-ip:ipv6": {},
        }
    } 

    resp = requests.put(
        # <!!!REPLACEME with URL!!!>,
        api_url + f"/ietf-interfaces:interfaces/interface=Loopback{studentID}",
        data=json.dumps(yangConfig),
        auth=basicauth,
        headers=headers,
        verify=False,
    )

    if resp.status_code == 204:
        print("STATUS OK Already Created: {}".format(resp.status_code))
        return f"Cannot create: Interface loopback {studentID}"
    if resp.status_code >= 200 and resp.status_code <= 299:
        print("STATUS OK: {}".format(resp.status_code))
        return f"Interface loopback {studentID} is created successfully"
    else:
        print("Error. Status Code: {}".format(resp.status_code))


def delete():
    resp = requests.delete(
        # <!!!REPLACEME with URL!!!>,
        api_url + f"/ietf-interfaces:interfaces/interface=Loopback{studentID}",
        auth=basicauth,
        headers=headers,
        verify=False,
    )

    if resp.status_code == 404:
        print("Error. Status NOT FOUND: {} ".format(resp.status_code))
        return f"Cannot delete: Interface loopback {studentID}"

    if resp.status_code >= 200 and resp.status_code <= 299:
        print("STATUS OK: {}".format(resp.status_code))
        return f"Interface loopback {studentID} is deleted successfully"
    else:
        print("Error. Status Code: {}".format(resp.status_code))


def enable():
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": f"Loopback{studentID}",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
        }
    }

    resp = requests.patch(
        # <!!!REPLACEME with URL!!!>,
        api_url + f"/ietf-interfaces:interfaces/interface=Loopback{studentID}",
        data=json.dumps(yangConfig),
        auth=basicauth,
        headers=headers,
        verify=False,
    )

    if resp.status_code == 404:
        print("Error. Status NOT FOUND: {} ".format(resp.status_code))
        return f"Cannot enable: Interface loopback {studentID}"
    if resp.status_code >= 200 and resp.status_code <= 299:
        print("STATUS OK: {}".format(resp.status_code))
        return f"Interface loopback {studentID} is enabled successfully"
    else:
        print("Error. Status Code: {}".format(resp.status_code))
        # return f"Cannot enable: Interface loopback {studentID}"


def disable():
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": f"Loopback{studentID}",
            "type": "iana-if-type:softwareLoopback",
            "enabled": False,
        }
    }

    resp = requests.patch(
        # <!!!REPLACEME with URL!!!>,
        api_url + f"/ietf-interfaces:interfaces/interface=Loopback{studentID}",
        data=json.dumps(yangConfig),
        auth=basicauth,
        headers=headers,
        verify=False,
    )

    if resp.status_code == 404:
        print("Error. Status NOT FOUND: {} ".format(resp.status_code))
        return f"Cannot shutdown: Interface loopback {studentID}"
    if resp.status_code >= 200 and resp.status_code <= 299:
        print("STATUS OK: {}".format(resp.status_code))
        return f"Interface loopback {studentID} is shutdowned successfully"
    else:
        print("Error. Status Code: {}".format(resp.status_code))
        # return f"Cannot shutdown: Interface loopback {studentID}"


# def status():
#     api_url_status = "<!!!REPLACEME with URL of RESTCONF Operational API!!!>"

#     resp = requests.<!!!REPLACEME with the proper HTTP Method!!!>(
#         <!!!REPLACEME with URL!!!>, 
#         auth=basicauth, 
#         headers=<!!!REPLACEME with HTTP Header!!!>, 
#         verify=False
#         )

#     if(resp.status_code >= 200 and resp.status_code <= 299):
#         print("STATUS OK: {}".format(resp.status_code))
#         response_json = resp.json()
#         admin_status = <!!!REPLACEME!!!>
#         oper_status = <!!!REPLACEME!!!>
#         if admin_status == 'up' and oper_status == 'up':
#             return "<!!!REPLACEME with proper message!!!>"
#         elif admin_status == 'down' and oper_status == 'down':
#             return "<!!!REPLACEME with proper message!!!>"
#     elif(resp.status_code == 404):
#         print("STATUS NOT FOUND: {}".format(resp.status_code))
#         return "<!!!REPLACEME with proper message!!!>"
#     else:
#         print('Error. Status Code: {}'.format(resp.status_code))
