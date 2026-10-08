# 🌐 Multi-Client Chat System using Socket Programming

A real-time multi-client communication system developed in Python demonstrating low-level socket programming and multithreading concepts.

---

## 📌 Project Overview
This project establishes a local network chat server where multiple clients can connect simultaneously to communicate. Key functionalities include:
- **Broadcasting:** Send messages to all connected users (`/all <message>`).
- **Private Messaging:** Direct private chat between specific users (`/pm <username> <message>`).
- **Group Messaging:** Send messages to a subset of users (`/group <user1,user2> <message>`).
- **Active Users Tracking:** Query current online clients (`/users`).
- **Connection Management:** Graceful exit and disconnection handling (`/exit`).

---

## 📁 Repository Structure
```text
├── client.py        # Client socket connection and thread listener
├── server.py        # Central socket server managing client connections
└── README.md        # Documentation and running guide