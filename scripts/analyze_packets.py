import pyshark
import pandas as pd

# Path to your capture file
capture_file = '../capture/test.pcap'

print("Reading capture file...")
cap = pyshark.FileCapture(capture_file)

data = []

for packet in cap:
    try:
        src = packet.ip.src
        dst = packet.ip.dst
        proto = packet.highest_layer
        length = packet.length
        data.append([src, dst, proto, length])
    except AttributeError:
        # Some packets (like ARP) may not have IP fields
        continue

# Convert to DataFrame
df = pd.DataFrame(data, columns=['Source IP', 'Destination IP', 'Protocol', 'Length'])

# Save to CSV
output_file = '../results/packet_analysis.csv'
df.to_csv(output_file, index=False)

print(f"✅ Analysis complete! Results saved to: {output_file}")
print("\nSample output:")
print(df.head())
# Save the analyzed data for visualization
data.to_csv('results/packet_analysis.csv', index=False)
print("\n✅ Analyzed data saved to results/packet_analysis.csv")
