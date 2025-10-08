import pyshark
import pandas as pd

pcap_file = r"C:\Users\ADMIN\Desktop\NetworkPacketAnalyzer\capture\test.pcap"
output_csv = r"C:\Users\ADMIN\Desktop\NetworkPacketAnalyzer\capture\output.csv"

print("Reading packets... please wait ⏳")

cap = pyshark.FileCapture(pcap_file, keep_packets=False)

packets = []
for pkt in cap:
    try:
        packets.append({
            'No': pkt.number,
            'Time': pkt.sniff_time,
            'Source': pkt.ip.src if hasattr(pkt, 'ip') else '',
            'Destination': pkt.ip.dst if hasattr(pkt, 'ip') else '',
            'Protocol': pkt.highest_layer,
            'Length': pkt.length,
            'Info': pkt.info if hasattr(pkt, 'info') else ''
        })
    except Exception as e:
        print("Skipping packet due to error:", e)
        continue

cap.close()

df = pd.DataFrame(packets)
df.to_csv(output_csv, index=False)
print(f"✅ Done! {len(df)} packets saved to CSV → {output_csv}")
