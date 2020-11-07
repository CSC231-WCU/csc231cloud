import geni.portal as portal
import geni.rspec.pg as pg
import geni.rspec.igext as IG

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

tourDescription = \
"""
This profile provides the template for a full research cluster with head node, scheduler, compute nodes, and shared file systems.
At the moment, we start with a single node running MPI.
"""

# Setup the Tour info with the above description and instructions.  
tour = IG.Tour()
tour.Description(IG.Tour.TEXT,tourDescription)
request.addTour(tour)

node = request.XenVM("taz")
node.routable_control_ip = "true"
node.cores = 8
node.ram = 8192
    
node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD"
  
# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
