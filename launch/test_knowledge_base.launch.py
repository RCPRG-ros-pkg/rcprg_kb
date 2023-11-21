from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Path to the XML file
    places_xml = os.path.join(
        get_package_share_directory('tiago_sim_integration'),
        'maps',
        '012_places',
        'places.xml'
    )

    test_knowledge_base_node = Node(
        package='tiago_kb',
        executable='test_knowledge_base',
        name='test_knowledge_base',
        output='screen',
        parameters=[{'places_xml': places_xml}],
        respawn=False
    )

    return LaunchDescription([
        test_knowledge_base_node
    ])
