#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

class JoyControl():
    def __init__(self):
        rospy.init_node("joy_control")
        self.velocity_pub = rospy.Publisher("/mobile_base/commands/velocity", Twist, queue_size = 10)
        self.joy_sub = rospy.Subscriber("/joy", Joy, self.joy_callback)
    
    def joy_callback(self, msg):
        x = msg.axes[1] * 0.25
        z = msg.axes[0] * 1.25
        
        if msg.axes[7] != 0:
            msg.axes[7] * 0.25
        
        if msg.axes[6] != 0:
            z = msg.axes[6] * 1.25
        
        twist = Twist()
        twist.linear.x = x
        twist.angular.z = z
        
        rospy.loginfo("Publishing x: {} z: {}".format(x, z))
        
        if x != 0 or z != 0:
            self.velocity_pub.publish(twist)

if __name__ == '__main__':
    try:
        joyControl = JoyControl()
        rospy.spin()
    
    except KeyboardInterrupt:
        pass