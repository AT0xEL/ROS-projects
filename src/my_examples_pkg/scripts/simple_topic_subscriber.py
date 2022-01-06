#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32 

def callback(msg): # define function called 'callback' that recieves msg parameter. Prints when message is given
  print (msg.data)

rospy.init_node('topic_subscriber') # create 'topic_subscriber' node
sub = rospy.Subscriber('/counter', Int32, callback) # Create subscriber object that will listen to /counter. 
# Will call callback() each time something is read from given topic

rospy.spin() # Loop program and keep it executing