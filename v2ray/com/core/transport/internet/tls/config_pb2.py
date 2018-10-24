# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2ray.com/core/transport/internet/tls/config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='v2ray.com/core/transport/internet/tls/config.proto',
  package='v2ray.core.transport.internet.tls',
  syntax='proto3',
  serialized_options=_b('\n%com.v2ray.core.transport.internet.tlsP\001Z\003tls\252\002!V2Ray.Core.Transport.Internet.Tls'),
  serialized_pb=_b('\n2v2ray.com/core/transport/internet/tls/config.proto\x12!v2ray.core.transport.internet.tls\"\xba\x01\n\x0b\x43\x65rtificate\x12\x13\n\x0b\x43\x65rtificate\x18\x01 \x01(\x0c\x12\x0b\n\x03Key\x18\x02 \x01(\x0c\x12\x43\n\x05usage\x18\x03 \x01(\x0e\x32\x34.v2ray.core.transport.internet.tls.Certificate.Usage\"D\n\x05Usage\x12\x10\n\x0c\x45NCIPHERMENT\x10\x00\x12\x14\n\x10\x41UTHORITY_VERIFY\x10\x01\x12\x13\n\x0f\x41UTHORITY_ISSUE\x10\x02\"\xd5\x01\n\x06\x43onfig\x12\x16\n\x0e\x61llow_insecure\x18\x01 \x01(\x08\x12\x1e\n\x16\x61llow_insecure_ciphers\x18\x05 \x01(\x08\x12\x43\n\x0b\x63\x65rtificate\x18\x02 \x03(\x0b\x32..v2ray.core.transport.internet.tls.Certificate\x12\x13\n\x0bserver_name\x18\x03 \x01(\t\x12\x15\n\rnext_protocol\x18\x04 \x03(\t\x12\"\n\x1a\x64isable_session_resumption\x18\x06 \x01(\x08\x42R\n%com.v2ray.core.transport.internet.tlsP\x01Z\x03tls\xaa\x02!V2Ray.Core.Transport.Internet.Tlsb\x06proto3')
)



_CERTIFICATE_USAGE = _descriptor.EnumDescriptor(
  name='Usage',
  full_name='v2ray.core.transport.internet.tls.Certificate.Usage',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENCIPHERMENT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTHORITY_VERIFY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTHORITY_ISSUE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=208,
  serialized_end=276,
)
_sym_db.RegisterEnumDescriptor(_CERTIFICATE_USAGE)


_CERTIFICATE = _descriptor.Descriptor(
  name='Certificate',
  full_name='v2ray.core.transport.internet.tls.Certificate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Certificate', full_name='v2ray.core.transport.internet.tls.Certificate.Certificate', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Key', full_name='v2ray.core.transport.internet.tls.Certificate.Key', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='usage', full_name='v2ray.core.transport.internet.tls.Certificate.usage', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CERTIFICATE_USAGE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=276,
)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='v2ray.core.transport.internet.tls.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='allow_insecure', full_name='v2ray.core.transport.internet.tls.Config.allow_insecure', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allow_insecure_ciphers', full_name='v2ray.core.transport.internet.tls.Config.allow_insecure_ciphers', index=1,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='certificate', full_name='v2ray.core.transport.internet.tls.Config.certificate', index=2,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='server_name', full_name='v2ray.core.transport.internet.tls.Config.server_name', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_protocol', full_name='v2ray.core.transport.internet.tls.Config.next_protocol', index=4,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disable_session_resumption', full_name='v2ray.core.transport.internet.tls.Config.disable_session_resumption', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=279,
  serialized_end=492,
)

_CERTIFICATE.fields_by_name['usage'].enum_type = _CERTIFICATE_USAGE
_CERTIFICATE_USAGE.containing_type = _CERTIFICATE
_CONFIG.fields_by_name['certificate'].message_type = _CERTIFICATE
DESCRIPTOR.message_types_by_name['Certificate'] = _CERTIFICATE
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Certificate = _reflection.GeneratedProtocolMessageType('Certificate', (_message.Message,), dict(
  DESCRIPTOR = _CERTIFICATE,
  __module__ = 'v2ray.com.core.transport.internet.tls.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.transport.internet.tls.Certificate)
  ))
_sym_db.RegisterMessage(Certificate)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), dict(
  DESCRIPTOR = _CONFIG,
  __module__ = 'v2ray.com.core.transport.internet.tls.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.transport.internet.tls.Config)
  ))
_sym_db.RegisterMessage(Config)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
