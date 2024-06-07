# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: docmatch.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import status_pb2 as status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='docmatch.proto',
  package='adsmsg',
  syntax='proto3',
  serialized_pb=_b('\n\x0e\x64ocmatch.proto\x12\x06\x61\x64smsg\x1a\x0cstatus.proto\"U\n\x0e\x44ocMatchRecord\x12\x16\n\x0esource_bibcode\x18\x01 \x01(\t\x12\x17\n\x0fmatched_bibcode\x18\x02 \x01(\t\x12\x12\n\nconfidence\x18\x03 \x01(\x01\"f\n\x12\x44ocMatchRecordList\x12\x30\n\x10\x64ocmatch_records\x18\x01 \x03(\x0b\x32\x16.adsmsg.DocMatchRecord\x12\x1e\n\x06status\x18\x02 \x01(\x0e\x32\x0e.adsmsg.Statusb\x06proto3')
  ,
  dependencies=[status__pb2.DESCRIPTOR,])




_DOCMATCHRECORD = _descriptor.Descriptor(
  name='DocMatchRecord',
  full_name='adsmsg.DocMatchRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source_bibcode', full_name='adsmsg.DocMatchRecord.source_bibcode', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='matched_bibcode', full_name='adsmsg.DocMatchRecord.matched_bibcode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='adsmsg.DocMatchRecord.confidence', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=40,
  serialized_end=125,
)


_DOCMATCHRECORDLIST = _descriptor.Descriptor(
  name='DocMatchRecordList',
  full_name='adsmsg.DocMatchRecordList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='docmatch_records', full_name='adsmsg.DocMatchRecordList.docmatch_records', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='adsmsg.DocMatchRecordList.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=229,
)

_DOCMATCHRECORDLIST.fields_by_name['docmatch_records'].message_type = _DOCMATCHRECORD
_DOCMATCHRECORDLIST.fields_by_name['status'].enum_type = status__pb2._STATUS
DESCRIPTOR.message_types_by_name['DocMatchRecord'] = _DOCMATCHRECORD
DESCRIPTOR.message_types_by_name['DocMatchRecordList'] = _DOCMATCHRECORDLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DocMatchRecord = _reflection.GeneratedProtocolMessageType('DocMatchRecord', (_message.Message,), dict(
  DESCRIPTOR = _DOCMATCHRECORD,
  __module__ = 'docmatch_pb2'
  # @@protoc_insertion_point(class_scope:adsmsg.DocMatchRecord)
  ))
_sym_db.RegisterMessage(DocMatchRecord)

DocMatchRecordList = _reflection.GeneratedProtocolMessageType('DocMatchRecordList', (_message.Message,), dict(
  DESCRIPTOR = _DOCMATCHRECORDLIST,
  __module__ = 'docmatch_pb2'
  # @@protoc_insertion_point(class_scope:adsmsg.DocMatchRecordList)
  ))
_sym_db.RegisterMessage(DocMatchRecordList)


# @@protoc_insertion_point(module_scope)