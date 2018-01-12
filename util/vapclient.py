#!/usr/bin/env python
# -*- coding: utf-8 -*- vim:fileencoding=utf-8:
#

import sys
import json
import socket


CTRL_SOCKET = "/var/run/vncauthproxy/vncproxy.sock"

def request_forwarding(sport, daddr, dport, password):
    assert(len(password) > 0)
    req = {
        "source_port": int(sport),
        "destination_address": daddr,
        "destination_port": int(dport),
        "password": password
    }

    ctrl = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    ctrl.connect(CTRL_SOCKET)
    ctrl.send(json.dumps(req))

    response = ctrl.recv(1024)
    res = json.loads(response)
    return res

if __name__ == '__main__':
    res = request_forwarding(*sys.argv[1:])
    if res['status'] == "OK":
        sys.exit(0)
    else:
        sys.exit(1)


def request_novnc_forwarding(server, daddr, dport, password, sport=None, tls=True, auth_user='', auth_password=''):
    """
    Ask TVAP/VNCAP for a forwarding port.

    The control socket on TVAP wants a JSON dictionary containing at least the
    destination port and address, and VNC password. It optionally can accept a
    requested source port, whether WebSockets should be used, and whether TLS
    (SSL/WSS) should be used.
    """

    try:
        host, port = server
        port = int(port)
        dport = int(dport)
        if not password:
            return False

        request = {
            "auth_user": auth_user,
            "auth_password": auth_password,
            "source_port": sport or 0,
            "destination_address": daddr,
            "destination_port": dport,
            "password": password,
            "type": "vnc-wss" if tls else "vnc-ws",
        }

        request = json.dumps(request)

        ctrl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ctrl.connect((host, port))
        ctrl.send("%s\r\n" % request)
        response = json.loads(ctrl.recv(1024).strip())
        ctrl.close()

        if response['status'] != 'OK':
            return False
        else:
            return response['source_port']

    # XXX bare except
    except:
        return False
