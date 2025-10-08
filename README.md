Network Packet Analyzer & Visualizer

A lightweight Python-based tool to capture, analyze, and visualize live network traffic using TShark and Pandas. Built as a mini project for academic purposes, this tool provides a practical introduction to digital forensics and basic traffic analysis.

📌 Features

✅ Capture live network packets using TShark
✅ Convert PCAP to CSV for easy processing
✅ Analyze traffic protocols, source IPs, and packet sizes
✅ Visualize protocol distribution and traffic patterns using Matplotlib
✅ Beginner-friendly structure, modular and extensible

🖥️ Screenshots
Protocol Distribution	Top Source IPs	Packet Length Histogram

	
	

(Replace with actual image paths or remove this section if not applicable.)

⚙️ Setup Instructions
Prerequisites

Windows 10

Python 3.10+

TShark (part of Wireshark)

Npcap installed and enabled

Step 1: Clone the Repo
git clone https://github.com/your-username/NetworkPacketAnalyzer.git
cd NetworkPacketAnalyzer

Step 2: Install Dependencies
pip install pandas matplotlib

Step 3: Capture Network Data

Use TShark to capture live packets and save to a CSV:

tshark -i 1 -T fields -e ip.src -e ip.dst -e _ws.col.Protocol -e frame.len -E header=y -E separator=, -E quote=d -E occurrence=f > capture/packet_data.csv


Replace -i 1 with the correct interface ID (run tshark -D to list interfaces).

Step 4: Analyze Captured Data
python analyze_packets.py

Step 5: Visualize the Results
python visualize_packets.py

📊 Output Metrics

Protocol frequency count

Top 5 Source IPs

Packet length distribution

Average packet size

📁 Project Structure
NetworkPacketAnalyzer/
├── capture/
│   └── packet_data.csv         # Raw packet capture from tshark
├── results/
│   └── packet_analysis.csv     # Analyzed output
├── analyze_packets.py          # Processes and summarizes packet data
├── visualize_packets.py        # Generates charts from analysis
└── README.md                   # Project documentation

📚 Use Cases

Academic mini project (Cybersecurity, Digital Forensics, AI)

Introductory tool for analyzing PCAP data

Network anomaly or threat pattern exploration (extensible)
