#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

# adjust these values
LINEAR_SPEED = 0.15
ANGULAR_SPEED = 1.25

class JoyControl():
    def __init__(self):
        rospy.init_node("joy_control")
        self.velocity_pub = rospy.Publisher("/mobile_base/commands/velocity", Twist, queue_size = 1)
        self.joy_sub = rospy.Subscriber("/joy", Joy, self.joy_callback)
    
    def joy_callback(self, msg):
        # joystick values
        x = msg.axes[1] * LINEAR_SPEED
        z = msg.axes[0] * ANGULAR_SPEED
        
        if x == 0 and z == 0:
            return

        twist = Twist()
        twist.linear.x = x
        twist.angular.z = z
        
        rospy.loginfo("Publishing x: {} z: {}".format(x, z))
        self.velocity_pub.publish(twist)
        

if __name__ == '__main__':
    try:
        joyControl = JoyControl()
        rospy.spin()
    
    except KeyboardInterrupt:
        pass
