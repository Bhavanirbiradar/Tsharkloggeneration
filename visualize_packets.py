import pandas as pd
import matplotlib.pyplot as plt

# Load the analyzed packet data
data = pd.read_csv("packet_analysis.csv")

# Rename columns for easier use (optional)
data.rename(columns={
    'Source IP': 'Source',
    'Destination IP': 'Destination'
}, inplace=True)

# --- Protocol Distribution ---
plt.figure(figsize=(8, 5))
data['Protocol'].value_counts().plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Protocol Distribution")
plt.xlabel("Protocol")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# --- Top 5 Source IPs ---
plt.figure(figsize=(8, 5))
data['Source'].value_counts().head(5).plot(kind='bar', color='lightgreen', edgecolor='black')
plt.title("Top 5 Source IPs")
plt.xlabel("Source IP")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# --- Packet Length Distribution ---
plt.figure(figsize=(8, 5))
plt.hist(data['Length'], bins=10, color='salmon', edgecolor='black')
plt.title("Packet Length Distribution")
plt.xlabel("Packet Length")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
