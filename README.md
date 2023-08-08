# Rover Workshop NTU 2023
Welcome to Discover's rover workshop. This GitHub repo contains all of the information you will need to successfully complete this workshop. Here you will find all of the slides, documentation, and example code used throughout the workshop.

## Rover Construction

All of the information you will need to successfully build the rovers can be found [here](https://www.leorover.tech/knowledge-base), under the Assembly manuals section. 


## Programming the Rovers

The slides used in this workshop can be found [here] TODO: link to power point.

All of the sample code can be found in the samples directory.

### The Task

Your task is to utilize Discover's [RoverAPI](https://github.com/DiscoverCCRI/RoverAPI) to create a catalog of the garden. To do this, you should drive your rover around the garden while looking for [ARTags](https://www.cs.cmu.edu/afs/cs/project/skinnerbots/Wiki/AprilTags/NRC-47419.pdf). Each ARTag will be located next to some plant that should be added to the catalog. The rovers can recognize each ARTag has an associated ID, and the rovers can keep track of an ARTag's relative position. You should take care to ensure that no duplicates are included in your catalog. Each catalog entry should include a photo that contains the plant and the ARTag, along with the relative position of the ARTag when the photo was taken. 

### Resources

The documentation for the RoverAPI can be found [here](https://discoverccri.github.io/rover_api.html).
