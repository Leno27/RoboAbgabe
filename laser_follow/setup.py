from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'laser_follow'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lennart',
    maintainer_email='lentr2707@googlemail.com',
    description='Folge einem Objekt mittels Laserscanner in einem Bereich vor dir ',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'drive_with_laserscanner = laser_follow.drive_with_laserscanner:main'
        ],
    },
)
