import pithermalcam as ptc

# Run this file to start a flask server streaming the video to the local network
# IP Address and port of the video feed will be displayed as the server is started
ptc.stream_camera_online(
    ip_address='192.168.52.13',
    output_folder='/home/pi/projects/pithermalcam/saved_snapshots/',
    debug=True,
)
