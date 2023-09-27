# Effective enumeration of Tor URLs implemnted on a psuedo-Tor network with a simple bot for enumeration

Welcome to the effective enumeration using bot project! This project aims to create a safe way to moderate the onion addresses of Tor without compromising the privacy and anonymity of the user. The primary goal is to demonstrate how a simple bot can work on a basic Tor - like network and enumerate the data sent through the private network.

## Features

- **Simplified Tor Network**: A private Tor-like network is set up using Python sockets, allowing data to be routed through multiple nodes for enhanced privacy and anonymity.

- **Simple Bot**: A basic bot is implemented within the network to scan and check data being sent for suspicious activity. The bot can report malicious data to a central server.

## Prerequisites

Before running the code, make sure you have the following prerequisites:

- Python 3.x
- Paramiko (for SSH communication)
- Other required libraries (install using `pip` as needed)

## Getting Started

1. Clone this repository to your local machine.

2. Configure the network settings and SSH connection parameters in the code to match your setup.

3. Run the code for the respective components (entry node, middle nodes, exit node, server, bot, report server) following the provided instructions in the code comments.

## Usage

- Run the various components of the pseudo Tor network, including the entry node, middle nodes, exit node, server, and bot.

- Monitor the network traffic and bot activity as data is routed through the network.

- Customize the bot's logic to detect suspicious activity in the data being sent.


## License

