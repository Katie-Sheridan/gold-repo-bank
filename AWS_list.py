# create an empty list of AWS services
services=[]

#Add items to the list, using +
services+=['EC2', 'VPC', 'Lambda']
print(services)

#Add another item to the list
services.append('Kinesis')
print(services)

#Print the list and the length of the list.
print(len(services))

#Remove two specific services from the list by name or by index.
services.remove('Lambda')
services.remove('Kinesis')

#Print the new list and the new length of the list.
print(services)
print(len(services))