# Hand Gesture Control Application

This Python application detects hand movements via a webcam and uses gestures to simulate keypress actions. It utilizes OpenCV for image processing, PyAutoGUI for simulating key presses, and provides real-time gesture-based interaction.

## Requirements

To run this application, ensure that you have Python installed (version 3.x recommended). You will also need to install the following libraries:

- `opencv-python` for image processing
- `numpy` for numerical operations
- `pyautogui` for simulating key presses
- `time` for timestamp calculations (comes with Python by default)

To install the required dependencies, run the following command in your terminal or command prompt:

```bash
pip install opencv-python numpy pyautogui
```

## Files

- **gesture_control.py**: The main Python file that runs the hand gesture recognition application.
- **README.md**: This documentation file.

## How to Run the Application

1. **Ensure Webcam Access**: Ensure your computer has a webcam connected and working, as the application uses it to capture video input.
   
2. **Run the Application**: Open your terminal or command prompt and navigate to the directory where the `gesture_control.py` file is located. Run the script by typing:

   ```bash
   python gesture_control.py
   ```

3. **Using the Application**:
   - Once the program starts, a window should appear displaying the video feed from your webcam.
   - The application will focus on hand gestures within a specific section of the frame.
   - Adjust the "Trackbars" window to tune the color ranges for better hand detection.
   - The application recognizes four gestures:
     - **Left Gesture**: Simulates the "Left Arrow" key press.
     - **Right Gesture**: Simulates the "Right Arrow" key press.
     - **Up Gesture**: Simulates the "Up Arrow" key press.
     - **Down Gesture**: Simulates the "Down Arrow" key press.
   - The application will exit when the 'q' key is pressed.

## Application Flow

1. **Video Capture**: The program starts by capturing video from your webcam.
2. **Hand Detection**: The application isolates the region of interest, performs Gaussian blur to remove noise, and creates a mask for detecting the hand.
3. **Contour Detection**: The largest contour is detected, and the centroid (center point) of this contour is calculated.
4. **Motion Detection**: By comparing the position of the centroid across consecutive frames, the program detects motion in the X and Y directions (left, right, up, down).
5. **Key Simulation**: Based on the detected motion, the corresponding keypress (arrow key) is simulated using the PyAutoGUI library.
6. **Trackbars**: You can adjust the "Hue", "Saturation", and "Value" of the mask to tune the color range for hand detection. This is useful if the hand is not being detected well in the video feed.

## Adjusting Trackbars

The "Trackbars" window allows you to adjust the following parameters:
- **HueMin**: The minimum hue value for the hand color.
- **HueMax**: The maximum hue value for the hand color.
- **SatMin**: The minimum saturation value for the hand color.
- **SatMax**: The maximum saturation value for the hand color.
- **ValMin**: The minimum value (brightness) for the hand color.
- **ValMax**: The maximum value (brightness) for the hand color.

Adjusting these values can help in better detecting the hand depending on the lighting conditions and hand color.

## Troubleshooting

- **Hand Not Detected**: Ensure that the lighting is good and that your hand is visible within the focus area. Adjust the trackbars to fine-tune the color range.
- **Poor Accuracy**: If the application detects more than one object or doesn't track the hand well, adjust the contour area threshold or fine-tune the trackbars.

## Notes

- The application currently uses a fixed region of interest within the camera frame (from row 0-300 and column 300-end) to focus on hand gestures. You can adjust this if needed by modifying the code.
- The threshold for hand detection is set to a contour area greater than 14000. If your hand is too small in the frame, you may need to increase this value for better detection.

## License

This project is licensed under the **MIT License**. See the **LICENSE** file for more information.

```
MIT License

Copyright (c) Ramendra 2022

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```



