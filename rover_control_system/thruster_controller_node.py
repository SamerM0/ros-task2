import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

class ThrusterControllerNode(Node):
    def __init__(self):
        super().__init__('thruster_controller_node')
        self.get_logger().info("initializing Thruster Controller Node")
        self.pwm_sub = self.create_subscription(Float32MultiArray, "/pwm", self.pwm_handler, 10)
    
    def pwm_handler(self, msg):
        pwm_x = msg.data[0]
        pwm_y = msg.data[1]
        self.get_logger().info(f"PWM : x={pwm_x}, y={pwm_y}")

def main(args=None):
    rclpy.init(args=args)
    node = ThrusterControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()