import csv

with open('data.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    headers = reader.next()

    # MAC,SSID,AuthMode,FirstSeen,Channel,RSSI,CurrentLatitude,CurrentLongitude,AltitudeMeters,AccuracyMeters,Type

    # Get the strongest reading for each Mac address
    macs = {}
    for line in reader:
        mac = line[0]
        if mac in macs:
            if macs[mac][5] < line[5]:
                macs[mac] = line
        else:
            macs[mac] = line

    # Get a count for each latlng:
    latlngs = {}
    for mac in macs:
        latlng = macs[mac][6] + macs[mac][7]

        if latlng in latlngs:
            latlngs[latlng][2] += 1
        else:
            latlngs[latlng] = [macs[mac][6], macs[mac][7], 1]

    with open('unique_locations.csv', 'wb') as f:
        writer = csv.writer(f)
        # writer.writerow(headers)
        writer.writerow(['lat', 'lng', 'count'])
        writer.writerows(latlngs.itervalues())

    with open('unique_macs.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(macs.itervalues())
