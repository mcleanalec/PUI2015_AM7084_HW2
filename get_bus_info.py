import json
import sys
import urllib2
import csv

if __name__=='__main__':
    mta_key = sys.argv[1]
    bus_code = sys.argv[2]
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (mta_key, bus_code)
    request = urllib2.urlopen(url)
    data = json.loads(request.read())
    
    with open(sys.argv[2], 'wb') as csvFile:
        writer = csv.writer(csvFile)
        headers = ['Latitude', 'Longitude', 'Stop Name', 'Stop Status']
        writer.writerow(headers)
        
        bus_info = data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
        
        
        for bus in bus_info:
            lat2 = bus["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
            long2 = bus["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
            if bus["MonitoredVehicleJourney"]["OnwardCalls"] == {}:
                Stop = "N/A"
                Status = "N/A"
            else:
                Stop = bus["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["StopPointName"]
                Status = bus["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["Extensions"]["Distances"]["PresentableDistance"]
    
            
            writer.writerow([lat2, long2, Stop, Status])
            print '%s, %s, %s, %s' % (lat2, long2, Stop, Status)
