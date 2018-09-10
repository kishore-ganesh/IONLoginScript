import subprocess, requests

output=subprocess.Popen(["ip", "addr", "show", "wlp2s0"], stdout=subprocess.PIPE)
output=output.communicate()[0];
output=str(output)
print("HELLO" + output)
ind1=output.find("inet")

output=output[ind1:]

ind2=output.find(" brd")
output=output[5:ind2]
output=output.split('/')[0]
output=output.split(".")
output[len(output)-1]="1";
output[len(output)-2]="0"
s="."
s=s.join(output)
url="http://"+s+"/"+"login"

r=requests.post(url, {

    'username': '',
    'password': '',
    'radius1-44115'	:'12'
})

print(r.text)
