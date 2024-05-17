## Calculate Total Watch Time in a Folder

This Python script helps you calculate the total watch time of all video files within a specified folder. 

**Features:**

* Supports common video file formats: MP4, AVI, MKV, MOV, WMV, FLV.
* Recursively scans the folder and subfolders for videos.
* Displays the total watch time in minutes.

**Requirements:**

* [Python 3.x](https://www.python.org/)
* [moviepy library](https://pypi.org/project/moviepy/)

**Installation:**

1. Clone or download the repository.
    ```bash
    git clone https://github.com/yasanthaniroshan/Total-Watch-Time.git
    ```
2. Install the [moviepy](https://pypi.org/project/moviepy/) library.
    ```bash
    pip install moviepy
    ```

**Usage:**

1. Run the script.
2. Enter the path of the folder containing your video files when prompted.
3. The script will calculate and display the total watch time in minutes.

**Example:**

    ```bash
    Enter the path of the main folder: /path/to/my/videos/
    Total watch time in the main folder: 123.45 minutes
    ```

**Note:** 

* Ensure that you have the `moviepy` library installed. 
* The script assumes that all files ending with the supported extensions are video files. 

This script can be a helpful tool for quickly estimating the total time required to watch all videos in a folder. 
