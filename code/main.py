# MPU6050 Reading
vals = mpu.get_values()

ax = vals["AcX"]
ay = vals["AcY"]
az = vals["AcZ"]

roll = math.degrees(math.atan2(ay, az))
pitch = math.degrees(
    math.atan2(-ax, math.sqrt(ay**2 + az**2))
)
