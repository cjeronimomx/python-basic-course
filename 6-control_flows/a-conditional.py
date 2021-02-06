# if/elif/else
if True:
    print("This condition is True")

if False:
    print("This condition is False so never is printed")



server = {'name': 'vm004', 'ip': '192.168.0.2', 'ram': 5.5, 'cpu_cores': 8, 'running': True}
if server['running']:
    print("The host is running")

if not server['running']:
    print("The host is off")
else:
    print("The host is running")



server['alias'] = 'frontend'
if server['alias'] == 'backend':
    print('Layer Backend')
elif server['alias'] == 'middleware':
    print("Layer middleware")
else:
    print('Other layer')

    # switch
server['alias'] = 'frontend'
if server['alias'] == 'backend':
    print('Layer Backend')
elif server['alias'] == 'middleware':
    print("Layer middleware")
elif server['alias'] == 'balancer':
    print('Layer Load balancer')
else:
    print('Other layer')