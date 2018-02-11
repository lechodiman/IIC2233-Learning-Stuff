from module_1 import module_1_f


action = 'opened'
title = 'a title'
body = 'A super body message'

message_to_send = ''
message_to_send += 'Action: {} \n'.format(action)
message_to_send += 'Title: {} \n'.format(title)
message_to_send += 'Body: {}'.format(body)

message = '/get #4'
print(message.startswith('/get'))
message_split = message.split(' ')
command = message_split[0]
num_issue = message_split[1]
if num_issue.startswith('#'):
    num_issue = num_issue.replace('#', '')
print(num_issue)

message = '/post #4 *Hola como estas'
print(message.split(' ', maxsplit=2))
