import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/mnt/utm/Mini_Rover/racs2_ws/ros2_test_ws/install/my_package'
