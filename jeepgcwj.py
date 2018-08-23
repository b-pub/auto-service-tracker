#
# Vehicle definition for a
# 2004 Jeep Grand Cherokee (WJ)
#

from vehicle import Vehicle

# Define a particular vehicle type with its own maintenance schedule
class JeepGCWJ(Vehicle):
    def __init__(self, name, year):
        Vehicle.__init__(self, name, year)
        self.intervals['engine-oil'] = 5000
        self.intervals['engine-oil-filter'] = 5000
        self.intervals['engine-air-filter'] = 15000
        self.intervals['transmission-fluid'] = 12000
        self.intervals['transmission-filter'] = 12000
        self.intervals['engine-spark-plugs'] = 30000
        self.intervals['transfercase-fluid'] = 30000
        self.intervals['engine-pcv-valve'] = 30000
        self.intervals['front-axle-fluid'] = 12000
        self.intervals['rear-axle-fluid'] = 12000
        self.intervals['tire-rotation'] = 5000
        self.intervals['brake-inspect-linings'] = 12000
        self.intervals['brake-lube-caliper-pins'] = 12000

