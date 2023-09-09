import cv2
import os

# Directory where your friend's images are located
image_dir = 'Images'

# Output video file name
output_video = 'friendship_day_video.mp4'

# Frame rate (change as per your preference)
frame_rate = 1  # 1 image per second

# Get the list of image files in the directory
image_files = sorted([os.path.join(image_dir, file) for file in os.listdir(image_dir) if file.endswith(('.jpg', '.jpeg', '.png'))])

# Check if there are images to create the video
if not image_files:
    print("No image files found in the specified directory.")
else:
    # Get the dimensions of the first image (assuming all images have the same dimensions)
    img = cv2.imread(image_files[0])
    height, width, layers = img.shape

    # Define the VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can change the codec as needed
    out = cv2.VideoWriter(output_video, fourcc, frame_rate, (width, height))

    # Loop through the image files and add them to the video
    for image_file in image_files:
        img = cv2.imread(image_file)
        out.write(img)

    # Release the VideoWriter object
    out.release()

    print(f"Video created: {output_video}")
