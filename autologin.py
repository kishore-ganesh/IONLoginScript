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

username_list = ['','']
password_list = ['','']

if default:
	print("Gateway:  " + default)
	print("local ip: " + my_ip)
	i = 0
	length = len(username_list)

	while i < length:
		try:
			url="http://"+default+"/"+"login"
			r=requests.post(url, {
				'username': username_list[i],
				'password': password_list[i],
				'radius1-44115'	:'12'
			},timeout=(1,1))

			if r.text.find("You are logged in"):
				print(username_list[i] + " logged in")
				break

		except:
			print("Time-out on " + username_list[i])
			i += 1

else:
	print("=>Bad Gateway<=")