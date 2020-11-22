import pandas


#This python file for updating ansible hosts

# Read host csv file
Host_DataFrame = pandas.read_csv('__HOST_CSV_DIRECTORY__/Python_HOST.csv')

# Open ansible host file
host_file = open("/etc/ansible/hosts","w+")


# Modify ansible host file with the IP ip_adress of switches
host_file.write("[switches]\n")
i = 1
for ip_adress in Host_DataFrame.values:
    host_file.write("hostname{} ansible_host={}\n".format(i,ip_adress[0]))
    i += 1

'''
Example host file
[switches]
hostname1 X.X.X.X
hostname2 X.X.X.Y
'''

# Close host file
host_file.close()
