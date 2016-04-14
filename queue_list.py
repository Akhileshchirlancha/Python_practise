from collections import deque
queue = deque(["eric","john","michael"])
print queue
queue.append("terry")
queue.append("graham")
print queue
print '-' * 50 
queue.popleft()
print 'queue.popleft()==>', queue
queue.popleft()
print 'queue.popleft()==>', queue
print queue
