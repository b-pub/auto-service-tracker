# auto-service-tracker
A Python code sketch to record vehicle service intervals and
events, and report which items are next.

The base definition is vehicle.Vehicle which defines the
methods and records the service events. Subclasses of Vehicle define
their own service intervals, which Vehicle base methods use to
determine the next service times.

As servicings are recorded, the total cost can also be reported.
This code will sum and report the total service of the vehicle lifetime.

Brent Burton
May 2018
