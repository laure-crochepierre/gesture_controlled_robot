import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist # This is the message type the robot uses for velocities

class CommandVelocity():
    """Driving my robot
    """

    def __init__(self):
        rospy.loginfo("Starting node")
        self.pub = rospy.Publisher("cmd_twists", Twist) # Creating a publisher with whatever name...
        
    # A function to send velocities until the node is killed
    def send_velocities(self):
        r = rospy.Rate(10) # Setting a rate (hz) at which to publish
        while not rospy.is_shutdown(): # Runnin until killed
            rospy.loginfo("Sending commands")
            twist_msg = Twist() # Creating a new message to send to the robot

            # ... put something relevant into your message

            self.pub.publish(twist_msg) # Sending the message via our publisher
            r.sleep() # Calling sleep to ensure the rate we set above


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
    
if __name__ == '__main__':
    rospy.init_node('robot_command')
    rospy.Subscriber("processing_result", String, callback)
    
    cv = CommandVelocity()
    cv.send_velocities() # Calling the function
    
    rospy.spin()    