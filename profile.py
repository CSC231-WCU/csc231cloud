import geni.portal as portal
import geni.rspec.pg as pg
import geni.rspec.igext as IG

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

tourDescription = \
"""
A single node to act as a server.
"""

# Setup the Tour info with the above description and instructions.  
tour = IG.Tour()
tour.Description(IG.Tour.TEXT,tourDescription)
request.addTour(tour)

node = request.RawPC("taz")
node.routable_control_ip = "true"
    
node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU16-64-STD"
  
# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
