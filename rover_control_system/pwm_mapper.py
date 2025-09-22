class PWMMapper:
    @staticmethod
    def map_to_pwm(value):
        pwm = (value +1)/2 * (2000-1000) + 1000
        return int(pwm)