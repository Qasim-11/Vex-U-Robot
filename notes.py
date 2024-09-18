"""
||=================================== This file is mainly for notes ===================================||
||                                                                                                     ||
||                                                                                                     ||
||                                                                                                     ||
||                                                                                                     ||
||                                                                                                     ||
||-----------------------------------------The robot's tasks:------------------------------------------||
||                                                                                                     ||
|| -- "Get it to work" Part:                                                                           ||
|| --- 1. Initialize all motors and sensors properly.                                                  ||
|| ---- a. Ensure all motors are correctly configured and mapped to the correct ports.                 ||
|| ---- b. Calibrate sensors such as gyroscope, ultrasonic sensors, and encoders.                      ||
|| ---- c. Test each motor and sensor to ensure functionality before programming complex behaviors.    ||
||                                                                                                     ||
|| --- 2. Basic driving functions.                                                                     ||
|| ---- a. Write code to move forward, backward, turn left and right using driver input.               ||
|| ---- b. Test responsiveness and fine-tune motor control to ensure smooth movement.                  ||
||                                                                                                     ||
|| --- 3. Basic object manipulation functions.                                                         ||
|| ---- a. Code the arms, claws, or any manipulators to pick up and release objects.                   ||
|| ---- b. Test object manipulation under driver control to ensure it works seamlessly.                ||
||                                                                                                     ||
|| --- 4. Safety and error handling.                                                                   ||
|| ---- a. Implement safety checks, such as stopping motors if they encounter too much resistance.     ||
|| ---- b. Set up error handling for unexpected sensor or motor failures (e.g., reset motors).         ||
||                                                                                                     ||
||------------                                                                             ------------||
||                                                                                                     ||
|| -- Autonomous Part:                                                                                 ||
|| --- 1. Path Planning:                                                                               ||
|| ---- a. Plan a precise route to key game elements (scoring objects, zones) ~ A* Algorithm.          ||                  
|| ---- b. Avoid obstacles and other robots.                                                           ||
|| ---- c. Use sensors like ultrasonic or vision to adjust for real-time conditions and position.      ||
||                                                                                                     ||
|| --- 2. Object Interaction (scoring):                                                                ||
|| ---- a. Identify Objects (Robots, Rings, Scoring Bars).                                             ||
|| ---- b. Pick up and move objects.                                                                   ||
|| ---- c. Score objects in the correct zones.                                                         ||
||                                                                                                     ||
||------------                                                                             ------------||
||                                                                                                     ||
|| -- Human-Controlled Part:                                                                           ||
|| --- 1. Control:                                                                                     ||
|| ---- a. Connect the robot to some sort of controller                                                ||
|| ---- b. Respond to driver inputs swiftly for quick navigation.                                      ||
|| ---- c. Accurately grab, lift, and move objects with driver control.                                ||
||                                                                                                     ||
||                                                                                                     ||
||                                                                                                     ||
||                                                                                                     ||
||                                                                                                     ||
||--------------------  The rest was written by ChatGPT, didn't bother reading it  --------------------||
||                                                                                                     ||
||                                                                                                     ||
||                                                                                                     ||
||                                                                                                     ||
|| -- Endgame Tasks:                                                                                   ||
|| --- 1. Positioning:                                                                                 ||
|| ---- a. Align robot in designated scoring zones before time runs out.                               ||
|| --- 2. Special Endgame Tasks:                                                                       ||
|| ---- a. Perform tasks like climbing or lifting (depending on the game) to maximize points.          ||
|| ---- b. Coordinate with alliance partners for endgame strategy.                                     ||
||                                                                                                     ||
|| -- Sensor Integration:                                                                              ||
|| --- 1. Use vision sensors to identify and track game elements during autonomous and driver control. ||
|| --- 2. Ultrasonic or LIDAR sensors to measure distance and avoid obstacles.                         ||
|| --- 3. Gyroscopes and encoders for accurate path corrections and positioning.                       ||
||                                                                                                     ||
|| -- System Health:                                                                                   ||
|| --- 1. Monitor battery voltage and current during the match to ensure optimal performance.          ||
|| --- 2. Detect motor overheating or strain and adjust power output to prevent damage.                ||
||                                                                                                     ||
|| -- Strategic Considerations:                                                                        ||
|| --- 1. Balance offensive and defensive play during the match.                                       ||
|| --- 2. Adjust strategies based on opponent behavior and real-time conditions.                       ||
|| --- 3. Optimize scoring during both autonomous and human-controlled phases.                         ||
||                                                                                                     ||
||==================================== End of Notes =====================================|| 
"""
