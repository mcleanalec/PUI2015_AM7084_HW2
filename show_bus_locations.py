import json
import sys
import urllib2

if __name__=='__main__':
    mta_key = sys.argv[1]
    bus_code = sys.argv[2]
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (mta_key, bus_code)
    request = urllib2.urlopen(url)
    data = json.loads(request.read())
    loc_bus = data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
    print "Busline:",  bus_code
    bus_count = len(loc_bus)
    print "The number of active bus lines are: ", bus_count
    
    index = 0
    for bus in loc_bus:
        long = bus["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
        lat =  bus["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
        print "Bus %d is at Latitude: %s and Longitude: %s"  % (index, lat, long) 
        index += 1
        
