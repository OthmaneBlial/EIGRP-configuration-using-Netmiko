from netmiko import ConnectHandler
import data

def config_interface(interface, address):
	return ['int '+ interface, 'ip add '+ address +' 255.255.255.0', 'no sh']

def config_eigrp(id, network='0.0.0.0'):
	return ['router eigrp '+  id, 'network '+ network, 'no auto']

def config_eigrp_auto_summary(id, mode='auto'):
	return ['router eigrp '+ id, mode]

def config_key_chain(name, key):
	return ['key chain '+ name, 'key 1', 'key string '+ key]

def config_interface_eigrp_key_chain(interface, eigrp_id , key_chain_name):
	return ['int '+ interface, 'ip authen mode eigrp '+ eigrp_id + ' md5', 'ip authen key-chain eigrp '+ eigrp_id +' '+ key_chain_name]

def configure_routers(ROUTERS):
	idx = 0
	for ROUTER in ROUTERS:
		idx += 1
		print("Applying interface configuration to ROUTER " + str(idx))
		net_connect = ConnectHandler(**ROUTER[0])
		config_commands = []
		for router_id, interface in ROUTER[1].items():
			min_value, max_value = min(idx, int(router_id)), max(idx, int(router_id))
			config_commands += config_interface(interface, '10.10.'+ str(min_value) + str(max_value) +'.'+ str(idx))
		config_commands += config_eigrp('1')
		config_commands += config_key_chain('the_chain', '123456')
		for router_id, interface in ROUTER[1].items():
			config_commands += config_interface_eigrp_key_chain(interface, '1', 'the_chain')
		net_connect.send_config_set(config_commands)
		print('Router '+ str(idx) +' has been configured!')


ROUTERS = [data.R1, data.R2, data.R3, data.R4, data.R5]

configure_routers(ROUTERS)