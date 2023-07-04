// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from ros2_path_planning:srv/PlanTrajectory.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "ros2_path_planning/srv/detail/plan_trajectory__rosidl_typesupport_introspection_c.h"
#include "ros2_path_planning/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "ros2_path_planning/srv/detail/plan_trajectory__functions.h"
#include "ros2_path_planning/srv/detail/plan_trajectory__struct.h"


// Include directives for member types
// Member `robot_position`
// Member `target_position`
#include "geometry_msgs/msg/pose.h"
// Member `robot_position`
// Member `target_position`
#include "geometry_msgs/msg/detail/pose__rosidl_typesupport_introspection_c.h"
// Member `grid_map`
#include "nav_msgs/msg/occupancy_grid.h"
// Member `grid_map`
#include "nav_msgs/msg/detail/occupancy_grid__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void ros2_path_planning__srv__PlanTrajectory_Request__rosidl_typesupport_introspection_c__PlanTrajectory_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  ros2_path_planning__srv__PlanTrajectory_Request__init(message_memory);
}

void ros2_path_planning__srv__PlanTrajectory_Request__rosidl_typesupport_introspection_c__PlanTrajectory_Request_fini_function(void * message_memory)
{
  ros2_path_planning__srv__PlanTrajectory_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember ros2_path_planning__srv__PlanTrajectory_Request__rosidl_typesupport_introspection_c__PlanTrajectory_Request_message_member_array[3] = {
  {
    "robot_position",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ros2_path_planning__srv__PlanTrajectory_Request, robot_position),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "target_position",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ros2_path_planning__srv__PlanTrajectory_Request, target_position),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "grid_map",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ros2_path_planning__srv__PlanTrajectory_Request, grid_map),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers ros2_path_planning__srv__PlanTrajectory_Request__rosidl_typesupport_introspection_c__PlanTrajectory_Request_message_members = {
  "ros2_path_planning__srv",  // message namespace
  "PlanTrajectory_Request",  // message name
  3,  // number of fields
  sizeof(ros2_path_planning__srv__PlanTrajectory_Request),
  ros2_path_planning__srv__PlanTrajectory_Request__rosidl_typesupport_introspection_c__PlanTrajectory_Request_message_member_array,  // message members
  ros2_path_planning__srv__PlanTrajectory_Request__rosidl_typesupport_introspection_c__PlanTrajectory_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  ros2_path_planning__srv__PlanTrajectory_Request__rosidl_typesupport_introspection_c__PlanTrajectory_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t ros2_path_planning__srv__PlanTrajectory_Request__rosidl_typesupport_introspection_c__PlanTrajectory_Request_message_type_support_handle = {
  0,
  &ros2_path_planning__srv__PlanTrajectory_Request__rosidl_typesupport_introspection_c__PlanTrajectory_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_ros2_path_planning
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ros2_path_planning, srv, PlanTrajectory_Request)() {
  ros2_path_planning__srv__PlanTrajectory_Request__rosidl_typesupport_introspection_c__PlanTrajectory_Request_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, geometry_msgs, msg, Pose)();
  ros2_path_planning__srv__PlanTrajectory_Request__rosidl_typesupport_introspection_c__PlanTrajectory_Request_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, geometry_msgs, msg, Pose)();
  ros2_path_planning__srv__PlanTrajectory_Request__rosidl_typesupport_introspection_c__PlanTrajectory_Request_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, nav_msgs, msg, OccupancyGrid)();
  if (!ros2_path_planning__srv__PlanTrajectory_Request__rosidl_typesupport_introspection_c__PlanTrajectory_Request_message_type_support_handle.typesupport_identifier) {
    ros2_path_planning__srv__PlanTrajectory_Request__rosidl_typesupport_introspection_c__PlanTrajectory_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &ros2_path_planning__srv__PlanTrajectory_Request__rosidl_typesupport_introspection_c__PlanTrajectory_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "ros2_path_planning/srv/detail/plan_trajectory__rosidl_typesupport_introspection_c.h"
// already included above
// #include "ros2_path_planning/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "ros2_path_planning/srv/detail/plan_trajectory__functions.h"
// already included above
// #include "ros2_path_planning/srv/detail/plan_trajectory__struct.h"


// Include directives for member types
// Member `trajectory`
// already included above
// #include "geometry_msgs/msg/pose.h"
// Member `trajectory`
// already included above
// #include "geometry_msgs/msg/detail/pose__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void ros2_path_planning__srv__PlanTrajectory_Response__rosidl_typesupport_introspection_c__PlanTrajectory_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  ros2_path_planning__srv__PlanTrajectory_Response__init(message_memory);
}

void ros2_path_planning__srv__PlanTrajectory_Response__rosidl_typesupport_introspection_c__PlanTrajectory_Response_fini_function(void * message_memory)
{
  ros2_path_planning__srv__PlanTrajectory_Response__fini(message_memory);
}

size_t ros2_path_planning__srv__PlanTrajectory_Response__rosidl_typesupport_introspection_c__size_function__PlanTrajectory_Response__trajectory(
  const void * untyped_member)
{
  const geometry_msgs__msg__Pose__Sequence * member =
    (const geometry_msgs__msg__Pose__Sequence *)(untyped_member);
  return member->size;
}

const void * ros2_path_planning__srv__PlanTrajectory_Response__rosidl_typesupport_introspection_c__get_const_function__PlanTrajectory_Response__trajectory(
  const void * untyped_member, size_t index)
{
  const geometry_msgs__msg__Pose__Sequence * member =
    (const geometry_msgs__msg__Pose__Sequence *)(untyped_member);
  return &member->data[index];
}

void * ros2_path_planning__srv__PlanTrajectory_Response__rosidl_typesupport_introspection_c__get_function__PlanTrajectory_Response__trajectory(
  void * untyped_member, size_t index)
{
  geometry_msgs__msg__Pose__Sequence * member =
    (geometry_msgs__msg__Pose__Sequence *)(untyped_member);
  return &member->data[index];
}

void ros2_path_planning__srv__PlanTrajectory_Response__rosidl_typesupport_introspection_c__fetch_function__PlanTrajectory_Response__trajectory(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const geometry_msgs__msg__Pose * item =
    ((const geometry_msgs__msg__Pose *)
    ros2_path_planning__srv__PlanTrajectory_Response__rosidl_typesupport_introspection_c__get_const_function__PlanTrajectory_Response__trajectory(untyped_member, index));
  geometry_msgs__msg__Pose * value =
    (geometry_msgs__msg__Pose *)(untyped_value);
  *value = *item;
}

void ros2_path_planning__srv__PlanTrajectory_Response__rosidl_typesupport_introspection_c__assign_function__PlanTrajectory_Response__trajectory(
  void * untyped_member, size_t index, const void * untyped_value)
{
  geometry_msgs__msg__Pose * item =
    ((geometry_msgs__msg__Pose *)
    ros2_path_planning__srv__PlanTrajectory_Response__rosidl_typesupport_introspection_c__get_function__PlanTrajectory_Response__trajectory(untyped_member, index));
  const geometry_msgs__msg__Pose * value =
    (const geometry_msgs__msg__Pose *)(untyped_value);
  *item = *value;
}

bool ros2_path_planning__srv__PlanTrajectory_Response__rosidl_typesupport_introspection_c__resize_function__PlanTrajectory_Response__trajectory(
  void * untyped_member, size_t size)
{
  geometry_msgs__msg__Pose__Sequence * member =
    (geometry_msgs__msg__Pose__Sequence *)(untyped_member);
  geometry_msgs__msg__Pose__Sequence__fini(member);
  return geometry_msgs__msg__Pose__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember ros2_path_planning__srv__PlanTrajectory_Response__rosidl_typesupport_introspection_c__PlanTrajectory_Response_message_member_array[1] = {
  {
    "trajectory",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ros2_path_planning__srv__PlanTrajectory_Response, trajectory),  // bytes offset in struct
    NULL,  // default value
    ros2_path_planning__srv__PlanTrajectory_Response__rosidl_typesupport_introspection_c__size_function__PlanTrajectory_Response__trajectory,  // size() function pointer
    ros2_path_planning__srv__PlanTrajectory_Response__rosidl_typesupport_introspection_c__get_const_function__PlanTrajectory_Response__trajectory,  // get_const(index) function pointer
    ros2_path_planning__srv__PlanTrajectory_Response__rosidl_typesupport_introspection_c__get_function__PlanTrajectory_Response__trajectory,  // get(index) function pointer
    ros2_path_planning__srv__PlanTrajectory_Response__rosidl_typesupport_introspection_c__fetch_function__PlanTrajectory_Response__trajectory,  // fetch(index, &value) function pointer
    ros2_path_planning__srv__PlanTrajectory_Response__rosidl_typesupport_introspection_c__assign_function__PlanTrajectory_Response__trajectory,  // assign(index, value) function pointer
    ros2_path_planning__srv__PlanTrajectory_Response__rosidl_typesupport_introspection_c__resize_function__PlanTrajectory_Response__trajectory  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers ros2_path_planning__srv__PlanTrajectory_Response__rosidl_typesupport_introspection_c__PlanTrajectory_Response_message_members = {
  "ros2_path_planning__srv",  // message namespace
  "PlanTrajectory_Response",  // message name
  1,  // number of fields
  sizeof(ros2_path_planning__srv__PlanTrajectory_Response),
  ros2_path_planning__srv__PlanTrajectory_Response__rosidl_typesupport_introspection_c__PlanTrajectory_Response_message_member_array,  // message members
  ros2_path_planning__srv__PlanTrajectory_Response__rosidl_typesupport_introspection_c__PlanTrajectory_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  ros2_path_planning__srv__PlanTrajectory_Response__rosidl_typesupport_introspection_c__PlanTrajectory_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t ros2_path_planning__srv__PlanTrajectory_Response__rosidl_typesupport_introspection_c__PlanTrajectory_Response_message_type_support_handle = {
  0,
  &ros2_path_planning__srv__PlanTrajectory_Response__rosidl_typesupport_introspection_c__PlanTrajectory_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_ros2_path_planning
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ros2_path_planning, srv, PlanTrajectory_Response)() {
  ros2_path_planning__srv__PlanTrajectory_Response__rosidl_typesupport_introspection_c__PlanTrajectory_Response_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, geometry_msgs, msg, Pose)();
  if (!ros2_path_planning__srv__PlanTrajectory_Response__rosidl_typesupport_introspection_c__PlanTrajectory_Response_message_type_support_handle.typesupport_identifier) {
    ros2_path_planning__srv__PlanTrajectory_Response__rosidl_typesupport_introspection_c__PlanTrajectory_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &ros2_path_planning__srv__PlanTrajectory_Response__rosidl_typesupport_introspection_c__PlanTrajectory_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "ros2_path_planning/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "ros2_path_planning/srv/detail/plan_trajectory__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers ros2_path_planning__srv__detail__plan_trajectory__rosidl_typesupport_introspection_c__PlanTrajectory_service_members = {
  "ros2_path_planning__srv",  // service namespace
  "PlanTrajectory",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // ros2_path_planning__srv__detail__plan_trajectory__rosidl_typesupport_introspection_c__PlanTrajectory_Request_message_type_support_handle,
  NULL  // response message
  // ros2_path_planning__srv__detail__plan_trajectory__rosidl_typesupport_introspection_c__PlanTrajectory_Response_message_type_support_handle
};

static rosidl_service_type_support_t ros2_path_planning__srv__detail__plan_trajectory__rosidl_typesupport_introspection_c__PlanTrajectory_service_type_support_handle = {
  0,
  &ros2_path_planning__srv__detail__plan_trajectory__rosidl_typesupport_introspection_c__PlanTrajectory_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ros2_path_planning, srv, PlanTrajectory_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ros2_path_planning, srv, PlanTrajectory_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_ros2_path_planning
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ros2_path_planning, srv, PlanTrajectory)() {
  if (!ros2_path_planning__srv__detail__plan_trajectory__rosidl_typesupport_introspection_c__PlanTrajectory_service_type_support_handle.typesupport_identifier) {
    ros2_path_planning__srv__detail__plan_trajectory__rosidl_typesupport_introspection_c__PlanTrajectory_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)ros2_path_planning__srv__detail__plan_trajectory__rosidl_typesupport_introspection_c__PlanTrajectory_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ros2_path_planning, srv, PlanTrajectory_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ros2_path_planning, srv, PlanTrajectory_Response)()->data;
  }

  return &ros2_path_planning__srv__detail__plan_trajectory__rosidl_typesupport_introspection_c__PlanTrajectory_service_type_support_handle;
}
