import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray, Bool
from rover_control_system.pwm_mapper import PWMMapper
class NavigationNode(Node):
    def __init__(self):
        super().__init__('navigation_node')
        self.get_logger().info("Navigation Node Initialized")

        self.is_navigating = False
        self.is_navigating_sub = self.create_subscription(Bool, "/joystick_check", self.navigation_status_handler, 10)
        self.joystick_sub = self.create_subscription(Float32MultiArray, "/joystick_axis", self.joystick_handler, 10)
        self.old_pwm_x = 1500
        self.old_pwm_y = 1500
        self.pwm_pub = self.create_publisher(Float32MultiArray,"/pwm",10)

    def joystick_handler(self, msg):
        #if not self.is_navigating:
        #    return
        x = msg.data[0]
        y = msg.data[1]
        
        new_pwm_x = PWMMapper.map_to_pwm(x)
        new_pwm_y = PWMMapper.map_to_pwm(y)
        
        pwm_x = self.linear_smooth(self.old_pwm_x, new_pwm_x) #change to exp_smooth for exponential smoothing
        pwm_y = self.linear_smooth(self.old_pwm_y, new_pwm_y)

        self.old_pwm_x = pwm_x
        self.old_pwm_y = pwm_y

        msg = Float32MultiArray()
        msg.data = [pwm_x, pwm_y]
        self.pwm_pub.publish(msg)
    def navigation_status_handler(self, msg):
        self.is_navigating = msg.data
        if msg.data:
            self.get_logger().info("Navigation started")
        else:
            self.get_logger().info("Navigation stopped")

    def linear_smooth(self, a,b,t = .1):
        return a+(b-a)*t
    
    def exp_smooth(self, a, b, factor=0.8):
        return a * factor + b * (1 - factor)

def main(args=None):
    rclpy.init(args=args)
    node = NavigationNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()