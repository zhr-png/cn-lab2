#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# GitHub: https://github.com/zhr-png/cn-lab2

import socket

# 目标主机信息
target_host = 'data.pr4e.org'
target_port = 80
target_path = '/romeo.txt'

# 创建TCP客户端套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接到目标主机
client_socket.connect((target_host, target_port))

# 构造符合 HTTP/1.1 规范的原始 GET 请求报文
# \r\n 是 HTTP 协议规定的换行符
request = (
    f"GET {target_path} HTTP/1.1\r\n"
    f"Host: {target_host}\r\n"
    f"Connection: close\r\n"
    f"\r\n"
)

# 发送编码后的请求数据
client_socket.send(request.encode())
while True:
    # 每次尝试接收 4096 字节的数据
    data = client_socket.recv(4096)

    # 停止条件判断：当 recv() 返回空字符串
    # 根据 TCP 协议，发送方调用 close() 后，接收方的 recv() 会返回 b'' 作为文件结束标志
    if not data:
        break

    # 将接收到的字节数据解码并打印
    print(data.decode(), end='')

# 循环结束
client_socket.close()
