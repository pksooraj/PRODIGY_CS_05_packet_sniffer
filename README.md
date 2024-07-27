
# Packet Sniffer

## Overview

The `PRODIGY_CS_05_packet_sniffer` project is a Python-based packet sniffer tool that captures and analyzes network packets. It displays relevant information such as source and destination IP addresses, protocols, and payload data. This tool is intended for educational purposes to help understand network traffic and packet analysis.

## Features

- Captures network packets using Scapy.
- Displays source and destination IP addresses.
- Identifies and shows the protocol (TCP, UDP, ICMP).
- Displays a preview of the payload data.

## Prerequisites

- Python 3.x
- Scapy library
- Npcap or WinPcap (for Windows users)

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/pksooraj/PRODIGY_CS_05_packet_sniffer.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd PRODIGY_CS_05_packet_sniffer
   ```

3. **Install Required Python Packages**:

   Install the `scapy` library using pip:

   ```bash
   pip install scapy
   ```

4. **Install Npcap (Windows Users)**:

   Download and install Npcap from [Npcap's official site](https://nmap.org/npcap/). During installation, select:
   - "Install Npcap in WinPcap API-compatible Mode"
   - "Install for all users (requires a reboot)"

## Usage

1. **Open a Terminal**:
   - For Windows, you might need to run the terminal as Administrator.
   - For Linux/Mac, you might need to use `sudo`.

2. **Run the Packet Sniffer**:

   ```bash
   python packet_sniffer.py
   ```

3. **View Output**:
   - The script will display captured packets including source and destination IP addresses, protocols, and a snippet of payload data.

## Troubleshooting

- **Npcap Issues**: Ensure Npcap is installed correctly and running. Check the [Npcap troubleshooting guide](https://nmap.org/npcap/#troubleshooting) for help.
- **Permissions**: Run the script with administrative privileges if you encounter permission errors.
- **Service Status**: Verify that the Npcap service is running from the `Services` application (`services.msc`).

## License

This project is licensed under the MIT License.

## Contributions

Contributions are welcome! Please feel free to submit a pull request or open an issue.
