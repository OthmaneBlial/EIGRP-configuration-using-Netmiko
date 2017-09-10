R1_info = {
    'device_type': 'cisco_ios',
    'ip':   '192.168.1.1',
    'username': 'user',
    'password': 'pass',
}

R2_info = {
    'device_type': 'cisco_ios',
    'ip':   '192.168.1.2',
    'username': 'user',
    'password': 'pass',
}


R3_info = {
    'device_type': 'cisco_ios',
    'ip':   '192.168.1.3',
    'username': 'user',
    'password': 'pass',
}

R4_info = {
    'device_type': 'cisco_ios',
    'ip':   '192.168.1.4',
    'username': 'user',
    'password': 'pass',
}

R5_info = {
    'device_type': 'cisco_ios',
    'ip':   '192.168.1.5',
    'username': 'user',
    'password': 'pass',
}



R1_connections = {
    '2': 's2/0',
    '3': 's2/1',
    '4': 's2/2',
}

R2_connections = {
    '1': 's2/0',
    '3': 'e0/0',
    '5': 's3/0',
}


R3_connections = {
    '1': 's2/1',
    '2': 'e0/0',
    '4': 'e0/1',
    '5': 's3/1',
}

R4_connections = {
    '1': 's2/2',
    '3': 'e0/1',
    '5': 's3/2',
}

R5_connections = {
    '2': 's3/0',
    '3': 's3/1',
    '4': 's3/2',
}


R1 = (R1_info, R1_connections)
R2 = (R2_info, R2_connections)
R3 = (R3_info, R3_connections)
R4 = (R4_info, R4_connections)
R5 = (R5_info, R5_connections)