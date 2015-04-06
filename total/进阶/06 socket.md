## 1 创建socket对象 ##

	socket.socket(1,2)

	参数1 AF_INET / AF_UNIX
	参数2 SOCK_STREAM SOCK_DGRAM

## 2 绑定端口 ##

	socket.bind(('localhost',8888))

	参数1 ip地址或者主机名
	参数2 端口

## 3 监听端口 ##

	socket.listen(n) 
	n代表允许多少个同时请求

## 4 接收连接 ##
 
	connection，address = sock.accept()

## 5 接收数据 ##
	
 	buf = connection.recv(100)

## 6 发送数据  ##

	connection.send(buf)

## 7 关闭连接 ##

	 connection.close()

## 8 addr reuse ##

	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)



## 9例子 ##：


	# Echo server program
	import socket
	
	HOST = ''                 # Symbolic name meaning all available interfaces
	PORT = 50007              # Arbitrary non-privileged port
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	s.listen(1)
	conn, addr = s.accept()
	print 'Connected by', addr
	while 1:
	    data = conn.recv(1024)
	    if not data: break
	    conn.sendall(data)
	conn.close()


	# Echo client program
	import socket
	
	HOST = 'daring.cwi.nl'    # The remote host
	PORT = 50007              # The same port as used by the server
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	s.sendall('Hello, world')
	data = s.recv(1024)
	s.close()
	print 'Received', repr(data)


## 10 nc工具 ##

	 [v1.10-39]
	connect to somewhere:   nc [-options] hostname port[s] [ports] ... 
	listen for inbound:     nc -l -p port [-options] [hostname] [port]
	options:
	        -c shell commands       as `-e'; use /bin/sh to exec [dangerous!!]
	        -e filename             program to exec after connect [dangerous!!]
	        -b                      allow broadcasts
	        -g gateway              source-routing hop point[s], up to 8
	        -G num                  source-routing pointer: 4, 8, 12, ...
	        -h                      this cruft
	        -i secs                 delay interval for lines sent, ports scanned
	        -k                      set keepalive option on socket
	        -l                      listen mode, for inbound connects
	        -n                      numeric-only IP addresses, no DNS
	        -o file                 hex dump of traffic
	        -p port                 local port number
	        -r                      randomize local and remote ports
	        -q secs                 quit after EOF on stdin and delay of secs
	        -s addr                 local source address
	        -T tos                  set Type Of Service
	        -t                      answer TELNET negotiation
	        -u                      UDP mode
	        -v                      verbose [use twice to be more verbose]
	        -w secs                 timeout for connects and final net reads
	        -z                      zero-I/O mode [used for scanning]
	     

简单用法

	nc -lp 8000 #启动一个服务器，监听端口8000
	nc localhost 8000 #启动一个客户端连接服务器

