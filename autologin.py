import subprocess, requests

ip_route=subprocess.Popen(["ip", "route"], stdout=subprocess.PIPE)
ip_route=ip_route.communicate()[0]
ip_route=str(ip_route)

default_pos_ip_route = ip_route.find('via ')
default =  ip_route[(default_pos_ip_route+4):]
default = default.split(' dev')[0]
default = str(default)

my_ip_pos = ip_route.find('src ')
my_ip = ip_route[(my_ip_pos+4):]
my_ip = my_ip.split(' metric')[0]
my_ip = str(my_ip)

if default:
	print("Gateway: " + default)
	print("local ip: " + my_ip)

	try:
		url="http://"+default+"/"+"login"
		r=requests.post(url, {
			'username': '',
			'password': '',
			'radius1-44115'	:'12'
		},timeout=(1,1))

		if r.text.find("You are logged in"):
				print("Log in success!")
	except:
			print("=>Time-out<=")

else:
	print("=>Bad Gateway<=")
