# Ansible_with_Python

I used CENTOS 7 for this project.!

This ansible playbook is used for checking ntp status of devices.

This playbook consists of 3 tasks. 

1-Pre Task : To modify Ansible Host File.(Host File contains IP Addresses of Devices)
2-Main Task: To connect and get ntp status of each devices in the host file 
3-Post Task: To build a single report file from the device outputs
