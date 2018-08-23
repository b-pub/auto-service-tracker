#
# Vehicle maintenance tracker.
# Framework and code to track and display scheduled maintenance tasks.
#

taskNames = sorted([
    # These are more of the scheduled, routine maintenance tasks
    'engine-oil',
    'engine-oil-filter',
    'engine-air-filter',
    'engine-coolant',
    'engine-spark-plugs',
    'engine-pcv-valve',
    'brake-fluid',
    'brake-pads',
    'brake-inspect-linings',
    'brake-lube-caliper-pins',
    'windshield-fluid',
    'windshield-wiper-front-left',
    'windshield-wiper-front-right',
    'windshield-wiper-rear',
    'transmission-fluid',
    'transmission-filter',
    'transaxle-fluid',
    'front-axle-fluid',
    'rear-axle-fluid',
    'transfercase-fluid',
    'cabin-air-filter',
    'tire-rotation',
    # And these are common, unscheduled repairs
    'tire-replacement',
    'ac-refrigerant',
    'ac-evaporator-core',
    'powersteering-fluid',
    'battery-replacement',
    'front-axle-rebuild',
    'rear-axle-rebuild',
    'state-inspection',
    'brake-rotor-replacement',
    'brake-master-cylinder',
    'engine-water-pump',
    'engine-thermostat',
    'steering-gearbox',
    'engine-oil-pressure-sensor',
    'tire-mounting',
    'engine-tuneup',
    'engine-fuel-injector-cleaning',
    'radiator-replacement',
    ])

class Vehicle(object):
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.serviceCosts = 0.00
        # intervals maps tasknames to distance intervals (miles or km)
        self.intervals = {}
        for tn in taskNames:
            self.intervals[tn] = 0
        # completedTasks records the times that a task has been performed
        #self.completedTasks[taskname] = [list of mileages]
        self.completedTasks = {}
        for tn in taskNames:
            self.completedTasks[tn] = [0] # performed at manufacturing time, 0 miles
        # serviceTimes is a list of [mileage, date, cost] tuples
        self.serviceTimes = [(0, '06/24/2004', 0.00)]

    def printSchedule(self):
        print("Maintenance Schedule: %d %s" % (self.year, self.name))
        for k in taskNames:
            if self.intervals[k] != 0:
                print("  %24s: %5d" % (k, self.intervals[k]))

    def whatsDue(self, mileage):
        '''Display tasks that are due for service at mileage'''
        print("Here's what's due for service at %d:" % mileage)
        nothingDue = True
        for tn in taskNames:
            isDue = (self.intervals[tn] > 0) and (mileage > self.intervals[tn] + self.completedTasks[tn][-1])
            if isDue:
                nothingDue = False
                print("  Service %s needed: last done at %d" %
                      (tn, self.completedTasks[tn][-1]))
        if nothingDue:
            print("  All maintenance tasks are currently up to date")

    def service(self, mileage, mmddyyyy, cost, taskList):
        '''Record maintenance tasks at this mileage and date, and at what cost'''
        # add entry to serviceTimes
        self.serviceTimes.append( (mileage, mmddyyyy, cost) )
        # add cost to serviceCosts
        self.serviceCosts += cost
        # for each task append mileage to completedTasks
        # ensure all tasks in taskList are valid
        for tn in taskList:
            if tn not in taskNames:
                print("**Invalid task %s included in service of %d on %s" %
                      (tn, mileage, mmddyyyy))
                continue
            self.completedTasks[tn].append(mileage)

    def printReport(self):
        '''Print maintenance history of the vehicle'''
        print("Maintenance History of %d %s" % (self.year, self.name))
        for (miles, when, cost) in self.serviceTimes:
            if miles == 0:
                continue
            print("  %6d: %s $%.2f" % (miles, when, cost))
            for tn in taskNames:
                if tn in self.completedTasks and miles in self.completedTasks[tn]:
                    print("          %s" % (tn))
            print('')
        print("Total maintenance cost: $%.2f" % (self.serviceCosts))

    def whatsNext(self, miles):
        '''Show which tasks are scheduled during the next 'miles' interval'''
        startMileage = self.serviceTimes[-1][0] # get most recent service miles
        endMileage = startMileage + miles
        print("Upcoming Maintenance for the next %d miles" % (miles))
        # mark when each task is next due, in miles
        nextDue = {}
        for tn in taskNames:
            if tn in self.completedTasks and self.intervals[tn] > 0:
                nextDue[tn] = self.completedTasks[tn][-1] + self.intervals[tn]
        # loop from startMileage, advancing each task by its interval until endMileage
        while startMileage < endMileage:
            # find next tasks due by searching for minimum of mileages in nextDue
            startMileage = min(nextDue.values())
            if startMileage > endMileage:
                break
            print("%6d:" % (startMileage))
            for tn in taskNames:
                if tn in nextDue and nextDue[tn] == startMileage:
                    print("       %s" % (tn))
                    nextDue[tn] += self.intervals[tn]

