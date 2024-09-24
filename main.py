import time
from config_loader import load_config
from inactivity import check_idle_duration
from jiggler import jiggle_mouse
from messages import monitoring_message, countdown_message, jiggling_message

if __name__ == "__main__":
    # Load the configuration from the JSON file
    config = load_config()

    IDLE_THRESHOLD = config["idle_threshold"]
    COUNTDOWN_TIME = config["countdown_time"]
    monitoring_msg = config["messages"]["monitoring_message"]
    countdown_msg = config["messages"]["countdown_message"]
    jiggling_msg = config["messages"]["jiggling_message"]

    last_jiggle_time = 0  # To track the time of the last jiggle

    # Print the monitoring message at the start
    monitoring_message(monitoring_msg)

    while True:
        idle_time = check_idle_duration()

        # If idle_time >= IDLE_THRESHOLD - COUNTDOWN_TIME, print countdown message every second
        if IDLE_THRESHOLD - COUNTDOWN_TIME <= idle_time < IDLE_THRESHOLD:
            remaining_time = int(IDLE_THRESHOLD - idle_time)
            countdown_message(remaining_time, countdown_msg)

        # If system is idle for more than IDLE_THRESHOLD seconds, jiggle the mouse
        if idle_time >= IDLE_THRESHOLD:
            jiggling_message(jiggling_msg)
            jiggle_mouse()

            # Reset last jiggle time
            last_jiggle_time = time.time()

        # Check every second
        time.sleep(1)
