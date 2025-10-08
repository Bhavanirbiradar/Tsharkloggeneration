import pyshark

print("Starting live capture...")
capture = pyshark.LiveCapture(interface='wi-fi', output_file='../capture/test.pcap')


for packet in capture.sniff_continuously(packet_count=5):
    print(packet)
