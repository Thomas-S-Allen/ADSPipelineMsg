# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fulltext_update.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import status_pb2 as status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fulltext_update.proto',
  package='adsmsg',
  syntax='proto3',
  serialized_pb=_b('\n\x15\x66ulltext_update.proto\x12\x06\x61\x64smsg\x1a\x0cstatus.proto\"\x8c\x01\n\x0e\x46ulltextUpdate\x12\x0f\n\x07\x62ibcode\x18\x01 \x01(\t\x12\x0c\n\x04\x62ody\x18\x02 \x01(\t\x12\x1e\n\x06status\x18\x03 \x01(\x0e\x32\x0e.adsmsg.Status\x12\x18\n\x10\x61\x63knowledgements\x18\x04 \x01(\t\x12\x0f\n\x07\x64\x61taset\x18\x05 \x03(\t\x12\x10\n\x08\x66\x61\x63ility\x18\x06 \x03(\tb\x06proto3')
  ,
  dependencies=[status__pb2.DESCRIPTOR,])




_FULLTEXTUPDATE = _descriptor.Descriptor(
  name='FulltextUpdate',
  full_name='adsmsg.FulltextUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bibcode', full_name='adsmsg.FulltextUpdate.bibcode', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='body', full_name='adsmsg.FulltextUpdate.body', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='adsmsg.FulltextUpdate.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='acknowledgements', full_name='adsmsg.FulltextUpdate.acknowledgements', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataset', full_name='adsmsg.FulltextUpdate.dataset', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='facility', full_name='adsmsg.FulltextUpdate.facility', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=188,
)

_FULLTEXTUPDATE.fields_by_name['status'].enum_type = status__pb2._STATUS
DESCRIPTOR.message_types_by_name['FulltextUpdate'] = _FULLTEXTUPDATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FulltextUpdate = _reflection.GeneratedProtocolMessageType('FulltextUpdate', (_message.Message,), dict(
  DESCRIPTOR = _FULLTEXTUPDATE,
  __module__ = 'fulltext_update_pb2'
  # @@protoc_insertion_point(class_scope:adsmsg.FulltextUpdate)
  ))
_sym_db.RegisterMessage(FulltextUpdate)


# @@protoc_insertion_point(module_scope)
