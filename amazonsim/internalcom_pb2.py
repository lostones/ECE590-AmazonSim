# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: internalcom.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='internalcom.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x11internalcom.proto\"A\n\x05Order\x12\x0e\n\x06shipid\x18\x01 \x02(\x03\x12\x0c\n\x04whid\x18\x02 \x02(\x05\x12\x0c\n\x04\x64\x65lX\x18\x03 \x02(\x05\x12\x0c\n\x04\x64\x65lY\x18\x04 \x02(\x05\"+\n\nOrderReply\x12\x0e\n\x06shipid\x18\x01 \x02(\x03\x12\r\n\x05\x65rror\x18\x02 \x01(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ORDER = _descriptor.Descriptor(
  name='Order',
  full_name='Order',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shipid', full_name='Order.shipid', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='whid', full_name='Order.whid', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delX', full_name='Order.delX', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delY', full_name='Order.delY', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=86,
)


_ORDERREPLY = _descriptor.Descriptor(
  name='OrderReply',
  full_name='OrderReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shipid', full_name='OrderReply.shipid', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='OrderReply.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=88,
  serialized_end=131,
)

DESCRIPTOR.message_types_by_name['Order'] = _ORDER
DESCRIPTOR.message_types_by_name['OrderReply'] = _ORDERREPLY

Order = _reflection.GeneratedProtocolMessageType('Order', (_message.Message,), dict(
  DESCRIPTOR = _ORDER,
  __module__ = 'internalcom_pb2'
  # @@protoc_insertion_point(class_scope:Order)
  ))
_sym_db.RegisterMessage(Order)

OrderReply = _reflection.GeneratedProtocolMessageType('OrderReply', (_message.Message,), dict(
  DESCRIPTOR = _ORDERREPLY,
  __module__ = 'internalcom_pb2'
  # @@protoc_insertion_point(class_scope:OrderReply)
  ))
_sym_db.RegisterMessage(OrderReply)


# @@protoc_insertion_point(module_scope)
