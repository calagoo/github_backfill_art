import cv2
import numpy as np
import datetime as dt
import git

def closest_value(value, values):
    # Convert the list to a numpy array to leverage numpy's capabilities
    values_array = np.array(values, dtype=np.float64)
    # Use numpy to find the absolute difference and identify the minimum
    closest_value = values_array[np.argmin(np.abs(values_array - value))]
    return closest_value

def color_value(value):
    if value == 255:
        return 0
    elif value == 175:
        return 2
    elif value == 120:
        return 5
    elif value == 75:
        return 10
    elif value == 0:
        return 20

def commit(image):
    start_date = dt.datetime(2022, 1, 1)
    while start_date.weekday() != 6: # Week starts on Sunday
        start_date += dt.timedelta(days=1)

    date = start_date
    ix = 0

    for col in range(52):
        for row in range(7):
            print(f"Date: {date.strftime('%Y-%m-%d')}, Commits: {color_value(image[row][col])}")
            commit_count = color_value(image[row][col])
            if commit_count > 0:
                repo = git.Repo('')
                # repo.git.add(A=True)
                # repo.index.commit(f"Commit {ix} on {date.strftime('%Y-%m-%d')}")
                repo.head.commit.authored_datetime = date
                ix += 1  

            date += dt.timedelta(days=1)
            ix += 1
    pass

def image_proccessing():
    # Load the image
    image = cv2.imread('racecar.png')
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    

    # Get unique values
    # {np.uint8(0), np.uint8(65), np.uint8(97), np.uint8(174), np.uint8(111), np.uint8(125), np.uint8(255)}
    # keep: 0, 75, 120, 175, 255

    unique_greys = [0, 75, 120, 175, 255]

    for row,_ in enumerate(grey):
        for pix,_ in enumerate(grey[row]):
            # Get the closest value
            closest = closest_value(grey[row][pix], unique_greys)
            grey[row][pix] = closest


    # Color = commits : unique_greys
    # Empty = 0 : 0
    # Light = 2 : 75
    # Medium = 5 : 120
    # Dark = 10 : 175
    # Full = 20 : 255
    return grey

def main():
    img = image_proccessing()
    commit(img)

if __name__ == "__main__":
    main()