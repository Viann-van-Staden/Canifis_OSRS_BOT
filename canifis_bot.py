import time
import pyautogui
import random

def click_on_image(image_path, confidence=0.5, min_delay=2.0, max_delay=4.0):
    """
    Tries to locate the image on the screen and click it. Adds a delay after each action.
    
    :param image_path: Path to the image to be found on screen.
    :param confidence: Confidence level for image matching.
    :param min_delay: Minimum delay between actions.
    :param max_delay: Maximum delay between actions.
    """
    print(f"Searching for {image_path} with confidence {confidence}")
    try:
        location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if location:
            pyautogui.moveTo(location.x, location.y, duration=random.uniform(0.1, 0.3))
            pyautogui.click()
            random_delay()
            time.sleep(random.uniform(min_delay, max_delay))  # Random delay between actions
        else:
            print(f"Image {image_path} not found!")
    except pyautogui.ImageNotFoundException:
        print(f"Image {image_path} could not be located on the screen.")

def random_delay(min_delay=5, max_delay=10):
    """
    Adds a random delay to simulate human-like behavior.
    
    :param min_delay: Minimum delay in seconds.
    :param max_delay: Maximum delay in seconds.
    """
    time.sleep(random.uniform(min_delay, max_delay))

def check_for_marks_of_grace():
    """
    Checks for Marks of Grace and clicks on them if found.
    """
    mark_of_grace_image = "mark_of_grace.png"  # Path to the Mark of Grace image
    confidence = 0.7  # Adjust confidence as needed
    print("Checking for Marks of Grace...")
    click_on_image(mark_of_grace_image, confidence=confidence, min_delay=0.5, max_delay=1.5)

def canifis_rooftop_course():
    """
    Executes the sequence of actions for the Canifis rooftop agility course.
    """
    # List of tuples with the image path and corresponding confidence level
    obstacles = [
        ("first_jump.png", 0.5),  # Adjusted confidence for first jump
        ("second_obstacle.png", 0.6),
        ("third_obstacle.png", 0.5),
        ("fourth_obstacle.png", 0.54),
        ("fifth_obstacle.png", 0.6),
        ("sixth_obstacle.png", 0.6),
        ("seventh_obstacle.png", 0.6),
        ("eighth_obstacle.png", 0.6)
    ]
    
    for obstacle, confidence in obstacles:
        click_on_image(obstacle, confidence=confidence, min_delay=2.0, max_delay=5.0)  # 2-5 seconds random delay
        check_for_marks_of_grace()  # Check for Marks of Grace after each obstacle

def run_bot():
    """
    Main function to run the bot for a set number of laps.
    """
    total_laps = 1000  # Set the number of laps you want the bot to run
    
    for lap in range(1, total_laps + 1):
        print(f"Starting lap {lap}")
        canifis_rooftop_course()
        time.sleep(2)  # Delay between laps
        
        if lap == 1000:
            print("Your 1000 laps have been completed")


if __name__ == "__main__":
    run_bot()
