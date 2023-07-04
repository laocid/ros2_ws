# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ros2_path_planning:srv/PlanTrajectory.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_PlanTrajectory_Request(type):
    """Metaclass of message 'PlanTrajectory_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('ros2_path_planning')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'ros2_path_planning.srv.PlanTrajectory_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__plan_trajectory__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__plan_trajectory__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__plan_trajectory__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__plan_trajectory__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__plan_trajectory__request

            from geometry_msgs.msg import Pose
            if Pose.__class__._TYPE_SUPPORT is None:
                Pose.__class__.__import_type_support__()

            from nav_msgs.msg import OccupancyGrid
            if OccupancyGrid.__class__._TYPE_SUPPORT is None:
                OccupancyGrid.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class PlanTrajectory_Request(metaclass=Metaclass_PlanTrajectory_Request):
    """Message class 'PlanTrajectory_Request'."""

    __slots__ = [
        '_robot_position',
        '_target_position',
        '_grid_map',
    ]

    _fields_and_field_types = {
        'robot_position': 'geometry_msgs/Pose',
        'target_position': 'geometry_msgs/Pose',
        'grid_map': 'nav_msgs/OccupancyGrid',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Pose'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Pose'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['nav_msgs', 'msg'], 'OccupancyGrid'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from geometry_msgs.msg import Pose
        self.robot_position = kwargs.get('robot_position', Pose())
        from geometry_msgs.msg import Pose
        self.target_position = kwargs.get('target_position', Pose())
        from nav_msgs.msg import OccupancyGrid
        self.grid_map = kwargs.get('grid_map', OccupancyGrid())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.robot_position != other.robot_position:
            return False
        if self.target_position != other.target_position:
            return False
        if self.grid_map != other.grid_map:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def robot_position(self):
        """Message field 'robot_position'."""
        return self._robot_position

    @robot_position.setter
    def robot_position(self, value):
        if __debug__:
            from geometry_msgs.msg import Pose
            assert \
                isinstance(value, Pose), \
                "The 'robot_position' field must be a sub message of type 'Pose'"
        self._robot_position = value

    @builtins.property
    def target_position(self):
        """Message field 'target_position'."""
        return self._target_position

    @target_position.setter
    def target_position(self, value):
        if __debug__:
            from geometry_msgs.msg import Pose
            assert \
                isinstance(value, Pose), \
                "The 'target_position' field must be a sub message of type 'Pose'"
        self._target_position = value

    @builtins.property
    def grid_map(self):
        """Message field 'grid_map'."""
        return self._grid_map

    @grid_map.setter
    def grid_map(self, value):
        if __debug__:
            from nav_msgs.msg import OccupancyGrid
            assert \
                isinstance(value, OccupancyGrid), \
                "The 'grid_map' field must be a sub message of type 'OccupancyGrid'"
        self._grid_map = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_PlanTrajectory_Response(type):
    """Metaclass of message 'PlanTrajectory_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('ros2_path_planning')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'ros2_path_planning.srv.PlanTrajectory_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__plan_trajectory__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__plan_trajectory__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__plan_trajectory__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__plan_trajectory__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__plan_trajectory__response

            from geometry_msgs.msg import Pose
            if Pose.__class__._TYPE_SUPPORT is None:
                Pose.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class PlanTrajectory_Response(metaclass=Metaclass_PlanTrajectory_Response):
    """Message class 'PlanTrajectory_Response'."""

    __slots__ = [
        '_trajectory',
    ]

    _fields_and_field_types = {
        'trajectory': 'sequence<geometry_msgs/Pose>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Pose')),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.trajectory = kwargs.get('trajectory', [])

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.trajectory != other.trajectory:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def trajectory(self):
        """Message field 'trajectory'."""
        return self._trajectory

    @trajectory.setter
    def trajectory(self, value):
        if __debug__:
            from geometry_msgs.msg import Pose
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, Pose) for v in value) and
                 True), \
                "The 'trajectory' field must be a set or sequence and each value of type 'Pose'"
        self._trajectory = value


class Metaclass_PlanTrajectory(type):
    """Metaclass of service 'PlanTrajectory'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('ros2_path_planning')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'ros2_path_planning.srv.PlanTrajectory')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__plan_trajectory

            from ros2_path_planning.srv import _plan_trajectory
            if _plan_trajectory.Metaclass_PlanTrajectory_Request._TYPE_SUPPORT is None:
                _plan_trajectory.Metaclass_PlanTrajectory_Request.__import_type_support__()
            if _plan_trajectory.Metaclass_PlanTrajectory_Response._TYPE_SUPPORT is None:
                _plan_trajectory.Metaclass_PlanTrajectory_Response.__import_type_support__()


class PlanTrajectory(metaclass=Metaclass_PlanTrajectory):
    from ros2_path_planning.srv._plan_trajectory import PlanTrajectory_Request as Request
    from ros2_path_planning.srv._plan_trajectory import PlanTrajectory_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
