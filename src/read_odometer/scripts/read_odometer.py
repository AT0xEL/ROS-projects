#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry

def callback(msg): # define function called 'callback' that recieves msg parameter. Prints when message is given
  # bad solution
  """
  # header 
  print("header seq: " + str(msg.header.seq) + "\n")
  print("header time: " + str(msg.header.stamp) + "\n")
  print("header_frame_id: " + str(msg.header.frame_id) + "\n")

  # child frame id
  print("child_frame_id: " + str(msg.child_frame_id) + "\n")

  # point position
  print("point pos x: " + str(msg.pose.pose.position.x) + "\n")
  print("point pos y: " + str(msg.pose.pose.position.y) + "\n")
  print("point pos z: " + str(msg.pose.pose.position.z) + "\n")

  # orintation
  print("quad orientation x: " + str(msg.pose.pose.orientation.x) + "\n")
  print("quad orientation y: " + str(msg.pose.pose.orientation.y) + "\n")
  print("quad orientation z: " + str(msg.pose.pose.orientation.z) + "\n")
  print("quad orientation w: " + str(msg.pose.pose.orientation.w) + "\n")
  
  # pose covariance
  print("pose covariance: " + str(msg.pose.covariance) + "\n")

  # linear twist
  print("twist linear x: " + str(msg.twist.twist.linear.x) + "\n")
  print("twist linear y: " + str(msg.twist.twist.linear.y) + "\n")
  print("twist linear z: " + str(msg.twist.twist.linear.z) + "\n")

  # angular twist
  print("twist angular x: " + str(msg.twist.twist.angular.x) + "\n")
  print("twist angular y: " + str(msg.twist.twist.angular.y) + "\n")
  print("twist angular z: " + str(msg.twist.twist.angular.z) + "\n")

  # twist covariance
  print("twist covariance: " + str(msg.twist.covariance) + "\n")""" 
  # good solution (infinitely a lot simplier)
  print(msg)


rospy.init_node('odometer_subscriber') # create 'topic_subscriber' node
sub = rospy.Subscriber('/odom', Odometry, callback) # Create subscriber object that will listen to /counter. 
# Will call callback() each time something is read from given topic

rospy.spin() # Loop program and keep it executing