class Pid(object):
	"""docstring for Pid"""
	def __init__(self, kp, kd, ki, rightMaxSpeed, leftMaxSpeed, rightBaseSpeed, leftBaseSpeed):
		super(Pid, self).__init__()
		self.kp = kp
		self.kd = kd
		self.ki = ki
		self.rightMaxSpeed = rightMaxSpeed
		self.leftMaxSpeed = leftMaxSpeed
		self.rightBaseSpeed = rightBaseSpeed
		self.leftBaseSpeed = leftBaseSpeed


	def calculatePID(position):
		error = position - 3500

		integral = integral + error
		motorSpeed = kp * error + kd * (error - lasterror) + ki * integral
		lasterror = error;
		
		return motorSpeed

	def motorPID(motorSpeed):
		rightMotorSpeed = rightBaseSpeed + motorSpeed
      	leftMotorSpeed = leftBaseSpeed - motorSpeed

      	if rightMotorSpeed > rightMaxSpeed: 
      		rightMotorSpeed = rightMaxSpeed

      	if leftMotorSpeed>leftMaxSpeed:
      		leftMotorSpeed = leftMaxSpeed
      	
      	if rightMotorSpeed < 0:
      		rightMotorSpeed =0
      	
      	if leftMotorSpeed < 0:
      		leftMotorSpeed = 0;
      		

      	return rightMotorSpeed, leftMotorSpeed