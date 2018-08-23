#!/usr/bin/python
#
# Demo script of a car's service history.
# 2004 Jeep Grand Cherokee (WJ)
#

import jeepgcwj

jeep = jeepgcwj.JeepGCWJ("Example WJ", 2004)

jeep.service(1, '01/01/2005', 28.75,
             ['state-inspection'])
jeep.service(3301, '02/15/2005', 40.00,
             ['engine-oil', 'engine-oil-filter'])
jeep.service(6601, '06/15/2005', 40.00,
             ['engine-oil', 'engine-oil-filter'])
jeep.service(9901, '10/15/2005', 40.00,
             ['engine-oil', 'engine-oil-filter'])

jeep.service(10001, '01/01/2006', 28.75,
             ['state-inspection'])
jeep.service(13301, '02/15/2006', 240.00,
             ['engine-oil', 'engine-oil-filter',
              'brake-inspect-linings', 'brake-lube-caliper-pins',
              'front-axle-fluid', 'rear-axle-fluid'])
jeep.service(16601, '06/15/2006', 40.00,
             ['engine-oil', 'engine-oil-filter'])
jeep.service(19901, '10/15/2006', 40.00,
             ['engine-oil', 'engine-oil-filter'])

jeep.service(20001, '01/01/2007', 28.75,
             ['state-inspection'])
jeep.service(23301, '02/15/2007', 40.00,
             ['engine-oil', 'engine-oil-filter'])
jeep.service(26601, '06/15/2007', 40.00,
             ['engine-oil', 'engine-oil-filter',
              'brake-inspect-linings', 'brake-lube-caliper-pins',
              'front-axle-fluid', 'rear-axle-fluid'])
jeep.service(29901, '10/15/2007', 130.00,
             ['engine-oil', 'engine-oil-filter',
              'engine-pcv-valve', 'transfercase-fluid'])

jeep.service(30001, '01/01/2008', 28.75,
             ['state-inspection'])
jeep.service(33301, '02/15/2008', 525.00,
             ['engine-oil', 'engine-oil-filter',
              'transmission-fluid', 'transmission-filter',
              'engine-air-filter', 'engine-spark-plugs'])
jeep.service(36601, '06/15/2008', 40.00,
             ['engine-oil', 'engine-oil-filter'])
jeep.service(39901, '10/15/2008', 250.00,
             ['engine-oil', 'engine-oil-filter',
              'brake-inspect-linings', 'brake-lube-caliper-pins',
              'front-axle-fluid', 'rear-axle-fluid'])

jeep.service(40001, '01/01/2009', 28.75,
             ['state-inspection'])
jeep.service(43847, '02/15/2009', 895.95,
             ['engine-oil-filter', 'engine-oil', 'tire-rotation',
              'radiator-replacement', 'ac-refrigerant'])
jeep.service(46601, '06/15/2009', 40.00,
             ['engine-oil', 'engine-oil-filter',
              'transmission-fluid', 'transmission-filter'])
jeep.service(49901, '10/15/2009', 50.00,
             ['engine-oil', 'engine-oil-filter',
              'engine-air-filter', 'tire-rotation'])

#
# Run this file by itself:
#
if __name__ == "__main__":

    # Print out the full maintenance history
    jeep.printReport()
    print('-'*40)

    # Display what services are needed in the next 5,000 miles:
    jeep.whatsNext(5000)
    print('-'*40)

    # If there's been a long interval since the last servicing,
    # ask what's due at a particular point:
    jeep.whatsDue(99507)
