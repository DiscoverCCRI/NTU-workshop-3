#!/usr/bin/python3
from rover_api.discover_tracking import Tracker
from rover_api.discover_camera import Camera

TOTAL_MARKERS = 5


def add_marker(markers, marker_id, marker_distance, camera):

    if marker_id not in markers and marker_id >= 0:
        markers.append(marker_id)
        camera.get_jpg()        
        log_marker(marker_id, marker_distance, len(markers))

        print(f"I found {marker_id}.\n")


def log_marker(marker_id, marker_distance, num_markers):
    with open("/experiment/catalog.md", "a+", encoding="utf-8") as outfile:
        print(f"logging marker: {marker_id}")
        outfile.write(f"The marker's id is {marker_id}. ")
        outfile.write(f"The marker was {marker_distance} from the robot.\n")
        outfile.write(f"The image is: ![{marker_id}](photos/{num_markers - 1}.jpg)\n\n")
        

def main():

    tracker = Tracker()
    camera = Camera()
    markers = []

    while TOTAL_MARKERS > len(markers):
        while not tracker.get_marker_visible():
            pass
        
        marker_distance = tracker.get_marker_distance()
        marker_id = tracker.get_marker_id()
        if (marker_distance >= 1.5 and marker_distance <= 2):
            add_marker(markers, marker_id, marker_distance, camera)
            

if __name__ == "__main__":
    main()
