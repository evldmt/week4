from setuptools import find_packages, setup

package_name = 'week4_activity'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Student Name',
    maintainer_email='student@example.com',
    description='Week 4 ROS 2 activity package.',
    license='TODO: License declaration',
    entry_points={
        'console_scripts': [
            'my_node = week4_activity.my_node:main',
        ],
    },
)
