# Robotik-Belegaufgaben
Abgabe für Belegaufgaben des Robotik Projekts 

In diesem Repo sind alle Packages der Belegaufgaben zu finden. Um diese nutzen zu können, muss Ros2 Humble installiert sein.


Den Link für einen Installations-Guide finden Sie hier:
https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html


Um die Packages zu nutzen müssen Sie dieses Repository auf Ihr Gerät klonen, eine Konsole öffnen, zu src navigieren und die Befehle ```colcon build``` und ```. install/setup.bash``` in der hier genannten Reihenfolge eingeben. 


##  Anmerkung zur 1. Belegaufgabe (PubSub)
Für diese Aufgabe müssen Sie ```ros2 run timing_tubaf_cpp talker``` in einer Konsole ausführen. In einer anderen Konsole müssen Sie "ros2 run timing_tubaf_py listener" ausführen.

## Anmerkung zur 2. Belegaufgabe (LaserFollow)
Für diese Aufgabe müssen Sie ```ros2 run laser_follow drive_with_laserscanner``` in der Konsole ausführen.

## Anmerkung zur 3. Belegaufgabe (LineFollow)
Für diese Aufgabe müssen Sie ```ros2 launch linebounce linebounce_launch.py``` in der Konsole ausführen.

## Anmerkung zur 4. Belegaufgabe (LaserFollow + LineFollow + Bounce)
Für diese Aufgabe müssen Sie ```ros2 launch two_drive two_drive_launch.py``` in der Konsole ausführen.
