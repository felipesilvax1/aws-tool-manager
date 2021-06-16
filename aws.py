#!/usr/bin/python3

import os, subprocess, sys

def menu():
    pass
    os.system('clear')
    print(f'\n***AWS - EC2***\n')
    #print('Put Your AWS token here')1
    print("Choose an option:\n")
    print('1 ==> List instances Ec2')
    print('2 ==> Create instance Ec2')
    print('3 ==> Stop instances Ec2')
    print('4 ==> Terminate instances Ec2')
    print('5 ==> Exit')
    op = int(input("\nChoose an Option:"))

    if op == 1:
        listInstances()
    elif op == 2:
        createInstance()
    elif op == 3:
        stopInstances()
    elif op == 4: 
         terminateInstances()
    else:
        sys.exit()
        

                
def createInstance():
    os.system("clear")
    print("\n Working on... ")
    os.system('aws ec2 run-instances --image-id ami-0b0af3577fe5e3532 --instance-type t2.micro --key-name nunesgay --count 2 --security-groups awscli --region us-east-1')
def listInstances():
    os.system("clear")
    print("\n The Instances in Execution: ")
    os.system('aws ec2 describe-instances --filters Name=instance-state-name,Values=running --query "Reservations[].Instances[].InstanceId" --region us-east-1')
def stopInstances():
    pass

def terminateInstances():
    pass

menu()
 