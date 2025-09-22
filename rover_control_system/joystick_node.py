from rclpy.node import Node
from std_msgs.msg import Bool, Float32MultiArray
import rclpy
from rover_control_system.joystick_listener import JoystickListener
import threading

class JoystickNode(Node):
    def __init__(self):
        super().__init__('joystick_node')
        self.get_logger().info("Initializing Joystick Node")
        self.check_pub = self.create_publisher(Bool, '/joystick_check', 10)
        self.joystick_axis_pub = self.create_publisher(Float32MultiArray, '/joystick_axis', 10)
        self.joystick_listener = JoystickListener()

        self.__listener_thread = threading.Thread(target=self.joystick_listener.start_listening) #create a thread to read joystick input
        self.__listener_thread.start()
        self.create_timer(0.1, self.publish_joystick)
        
    
    def publish_joystick(self):
        x, y = self.joystick_listener.get_axes()
        self.get_logger().info(f"x={x}, y={y}")
        if x != 0 or y != 0:
            msg = Bool()
            msg.data = True
            self.check_pub.publish(msg)
        msg = Float32MultiArray()
        if x == 0:
            x = 0.0
        if y == 0:
            y = 0.0
        msg.data = [x, y]
        self.joystick_axis_pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = JoystickNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    