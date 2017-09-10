from netmiko import ConnectHandler
import data


def message(msg):
	print('\n\n'+80*'#')
	print('\n\n' + 20*'#' +'  '+ msg + '  '+ 20*'#' + '\n\n')
	print(80*'#'+'\n\n')


def show_eigrp_routes(ROUTERS):
	idx = 0
	for ROUTER in ROUTERS:
		idx += 1
		print(20*'*'+' Showing EIGRP ROUTES for ROUTER '+ str(idx) + ' ' + 20*'*')
		net_connect = ConnectHandler(**ROUTER)
		output = net_connect.send_command('sho ip route eigrp | begin Gate')
		print(output)



ROUTERS = [data.R1, data.R2, data.R3, data.R4, data.R5]

message('Showing EIGRP ROUTES')
show_eigrp_routes(ROUTERS)
