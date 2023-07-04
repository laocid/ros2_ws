// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ros2_path_planning:srv/PlanTrajectory.idl
// generated code does not contain a copyright notice

#ifndef ROS2_PATH_PLANNING__SRV__DETAIL__PLAN_TRAJECTORY__STRUCT_HPP_
#define ROS2_PATH_PLANNING__SRV__DETAIL__PLAN_TRAJECTORY__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'robot_position'
// Member 'target_position'
#include "geometry_msgs/msg/detail/pose__struct.hpp"
// Member 'grid_map'
#include "nav_msgs/msg/detail/occupancy_grid__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ros2_path_planning__srv__PlanTrajectory_Request __attribute__((deprecated))
#else
# define DEPRECATED__ros2_path_planning__srv__PlanTrajectory_Request __declspec(deprecated)
#endif

namespace ros2_path_planning
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct PlanTrajectory_Request_
{
  using Type = PlanTrajectory_Request_<ContainerAllocator>;

  explicit PlanTrajectory_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : robot_position(_init),
    target_position(_init),
    grid_map(_init)
  {
    (void)_init;
  }

  explicit PlanTrajectory_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : robot_position(_alloc, _init),
    target_position(_alloc, _init),
    grid_map(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _robot_position_type =
    geometry_msgs::msg::Pose_<ContainerAllocator>;
  _robot_position_type robot_position;
  using _target_position_type =
    geometry_msgs::msg::Pose_<ContainerAllocator>;
  _target_position_type target_position;
  using _grid_map_type =
    nav_msgs::msg::OccupancyGrid_<ContainerAllocator>;
  _grid_map_type grid_map;

  // setters for named parameter idiom
  Type & set__robot_position(
    const geometry_msgs::msg::Pose_<ContainerAllocator> & _arg)
  {
    this->robot_position = _arg;
    return *this;
  }
  Type & set__target_position(
    const geometry_msgs::msg::Pose_<ContainerAllocator> & _arg)
  {
    this->target_position = _arg;
    return *this;
  }
  Type & set__grid_map(
    const nav_msgs::msg::OccupancyGrid_<ContainerAllocator> & _arg)
  {
    this->grid_map = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ros2_path_planning::srv::PlanTrajectory_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const ros2_path_planning::srv::PlanTrajectory_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ros2_path_planning::srv::PlanTrajectory_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ros2_path_planning::srv::PlanTrajectory_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ros2_path_planning::srv::PlanTrajectory_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ros2_path_planning::srv::PlanTrajectory_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ros2_path_planning::srv::PlanTrajectory_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ros2_path_planning::srv::PlanTrajectory_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ros2_path_planning::srv::PlanTrajectory_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ros2_path_planning::srv::PlanTrajectory_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ros2_path_planning__srv__PlanTrajectory_Request
    std::shared_ptr<ros2_path_planning::srv::PlanTrajectory_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ros2_path_planning__srv__PlanTrajectory_Request
    std::shared_ptr<ros2_path_planning::srv::PlanTrajectory_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const PlanTrajectory_Request_ & other) const
  {
    if (this->robot_position != other.robot_position) {
      return false;
    }
    if (this->target_position != other.target_position) {
      return false;
    }
    if (this->grid_map != other.grid_map) {
      return false;
    }
    return true;
  }
  bool operator!=(const PlanTrajectory_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct PlanTrajectory_Request_

// alias to use template instance with default allocator
using PlanTrajectory_Request =
  ros2_path_planning::srv::PlanTrajectory_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace ros2_path_planning


// Include directives for member types
// Member 'trajectory'
// already included above
// #include "geometry_msgs/msg/detail/pose__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ros2_path_planning__srv__PlanTrajectory_Response __attribute__((deprecated))
#else
# define DEPRECATED__ros2_path_planning__srv__PlanTrajectory_Response __declspec(deprecated)
#endif

namespace ros2_path_planning
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct PlanTrajectory_Response_
{
  using Type = PlanTrajectory_Response_<ContainerAllocator>;

  explicit PlanTrajectory_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
  }

  explicit PlanTrajectory_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
    (void)_alloc;
  }

  // field types and members
  using _trajectory_type =
    std::vector<geometry_msgs::msg::Pose_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<geometry_msgs::msg::Pose_<ContainerAllocator>>>;
  _trajectory_type trajectory;

  // setters for named parameter idiom
  Type & set__trajectory(
    const std::vector<geometry_msgs::msg::Pose_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<geometry_msgs::msg::Pose_<ContainerAllocator>>> & _arg)
  {
    this->trajectory = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ros2_path_planning::srv::PlanTrajectory_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const ros2_path_planning::srv::PlanTrajectory_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ros2_path_planning::srv::PlanTrajectory_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ros2_path_planning::srv::PlanTrajectory_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ros2_path_planning::srv::PlanTrajectory_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ros2_path_planning::srv::PlanTrajectory_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ros2_path_planning::srv::PlanTrajectory_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ros2_path_planning::srv::PlanTrajectory_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ros2_path_planning::srv::PlanTrajectory_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ros2_path_planning::srv::PlanTrajectory_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ros2_path_planning__srv__PlanTrajectory_Response
    std::shared_ptr<ros2_path_planning::srv::PlanTrajectory_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ros2_path_planning__srv__PlanTrajectory_Response
    std::shared_ptr<ros2_path_planning::srv::PlanTrajectory_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const PlanTrajectory_Response_ & other) const
  {
    if (this->trajectory != other.trajectory) {
      return false;
    }
    return true;
  }
  bool operator!=(const PlanTrajectory_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct PlanTrajectory_Response_

// alias to use template instance with default allocator
using PlanTrajectory_Response =
  ros2_path_planning::srv::PlanTrajectory_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace ros2_path_planning

namespace ros2_path_planning
{

namespace srv
{

struct PlanTrajectory
{
  using Request = ros2_path_planning::srv::PlanTrajectory_Request;
  using Response = ros2_path_planning::srv::PlanTrajectory_Response;
};

}  // namespace srv

}  // namespace ros2_path_planning

#endif  // ROS2_PATH_PLANNING__SRV__DETAIL__PLAN_TRAJECTORY__STRUCT_HPP_
