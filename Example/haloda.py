import csv

# Data to be written
data = [
    ['IncidentID', 'Date', 'Type', 'Severity', 'Description', 'Status'],
    ['1', '1/15/2023', 'Phishing', 'High', 'Phishing email targeting company employees', 'Pending'],
    ['2', '1/20/2023', 'Malware', 'Medium', 'Malware detected on employee workstation', 'Pending'],
    ['3', '2/5/2023', 'Ransomware', 'Critical', 'Ransomware attack encrypting company data', 'Pending'],
    ['4', '3/10/2023', 'Phishing', 'Low', 'Phishing email targeting external customers', 'Pending'],
    ['5', '3/15/2023', 'Data Breach', 'Critical', 'Sensitive data leaked from database', 'Pending']
]

# Writing to the CSV file
with open('incidents.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
