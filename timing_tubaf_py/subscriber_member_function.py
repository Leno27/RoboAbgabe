# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from std_msgs.msg import Float32
import time

class TimeDifferenceSubscriber(Node):

    def __init__(self):
        super().__init__('time_difference_subscriber')
        self.subscription = self.create_subscription(
            Int32,
            'number',
            self.listener_callback,
            10)
        self.publisher = self.create_publisher(Float32, 'diff', 10)
        self.last_time = None
        self.second_last_time = None

    def listener_callback(self, msg):
        current_time = msg.data
        if self.last_time is not None:
            # Berechne die Zeitdifferenz zwischen der aktuellen Nachricht und der letzten
            time_diff = float(current_time - self.last_time)
            self.get_logger().info(f'Time difference: {time_diff} seconds')
            
            # Veröffentliche die Zeitdifferenz
            diff_msg = Float32()
            diff_msg.data = time_diff
            self.publisher.publish(diff_msg)
        
        # Update der Zeitstempel für die nächste Nachricht
        self.second_last_time = self.last_time
        self.last_time = current_time

def main(args=None):
    rclpy.init(args=args)
    node = TimeDifferenceSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
