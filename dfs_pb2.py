# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dfs.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dfs.proto',
  package='dfs',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\tdfs.proto\x12\x03\x64\x66s\"E\n\x18SaveStorageServerRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x1b\n\x13storage_server_name\x18\x02 \x01(\t\"S\n\x16SaveStorageServerReply\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x1b\n\x13storage_server_name\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\"!\n\x11\x43reateFileRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\"!\n\x0f\x43reateFileReply\x12\x0e\n\x06status\x18\x01 \x01(\x08\"\x1e\n\x0eListDirRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\",\n\x0cListDirReply\x12\x0c\n\x04list\x18\x01 \x03(\t\x12\x0e\n\x06status\x18\x02 \x01(\x08\"/\n\x11\x41ppendFileRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\"!\n\x0f\x41ppendFileReply\x12\x0e\n\x06status\x18\x01 \x01(\x08\".\n\x10WriteFileRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\" \n\x0eWriteFileReply\x12\x0e\n\x06status\x18\x01 \x01(\x08\"#\n\x13TruncateFileRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\"#\n\x11TruncateFileReply\x12\x0e\n\x06status\x18\x01 \x01(\x08\"!\n\x11RemoveFileRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\"!\n\x0fRemoveFileReply\x12\x0e\n\x06status\x18\x01 \x01(\x08\"\x1f\n\x0fReadFileRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\"4\n\rReadFileReply\x12\x13\n\x0b\x66ileContent\x18\x01 \x03(\t\x12\x0e\n\x06status\x18\x02 \x01(\x08\"#\n\x13\x44ownloadFileRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\"8\n\x11\x44ownloadFileReply\x12\x13\n\x0b\x66ileContent\x18\x01 \x03(\t\x12\x0e\n\x06status\x18\x02 \x01(\x08\x32\xc2\x04\n\x03\x44\x46S\x12<\n\nCreateFile\x12\x16.dfs.CreateFileRequest\x1a\x14.dfs.CreateFileReply\"\x00\x12\x33\n\x07ListDir\x12\x13.dfs.ListDirRequest\x1a\x11.dfs.ListDirReply\"\x00\x12<\n\nAppendFile\x12\x16.dfs.AppendFileRequest\x1a\x14.dfs.AppendFileReply\"\x00\x12\x39\n\tWriteFile\x12\x15.dfs.WriteFileRequest\x1a\x13.dfs.WriteFileReply\"\x00\x12\x42\n\x0cTruncateFile\x12\x18.dfs.TruncateFileRequest\x1a\x16.dfs.TruncateFileReply\"\x00\x12<\n\nRemoveFile\x12\x16.dfs.RemoveFileRequest\x1a\x14.dfs.RemoveFileReply\"\x00\x12\x36\n\x08ReadFile\x12\x14.dfs.ReadFileRequest\x1a\x12.dfs.ReadFileReply\"\x00\x12\x42\n\x0c\x44ownloadFile\x12\x18.dfs.DownloadFileRequest\x1a\x16.dfs.DownloadFileReply\"\x00\x12Q\n\x11SaveStorageServer\x12\x1d.dfs.SaveStorageServerRequest\x1a\x1b.dfs.SaveStorageServerReply\"\x00\x62\x06proto3')
)




_SAVESTORAGESERVERREQUEST = _descriptor.Descriptor(
  name='SaveStorageServerRequest',
  full_name='dfs.SaveStorageServerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='dfs.SaveStorageServerRequest.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='storage_server_name', full_name='dfs.SaveStorageServerRequest.storage_server_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=18,
  serialized_end=87,
)


_SAVESTORAGESERVERREPLY = _descriptor.Descriptor(
  name='SaveStorageServerReply',
  full_name='dfs.SaveStorageServerReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='dfs.SaveStorageServerReply.status', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='storage_server_name', full_name='dfs.SaveStorageServerReply.storage_server_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='dfs.SaveStorageServerReply.path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=89,
  serialized_end=172,
)


_CREATEFILEREQUEST = _descriptor.Descriptor(
  name='CreateFileRequest',
  full_name='dfs.CreateFileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='dfs.CreateFileRequest.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=174,
  serialized_end=207,
)


_CREATEFILEREPLY = _descriptor.Descriptor(
  name='CreateFileReply',
  full_name='dfs.CreateFileReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='dfs.CreateFileReply.status', index=0,
      number=1, type=8, cpp_type=7, label=1,
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
  serialized_start=209,
  serialized_end=242,
)


_LISTDIRREQUEST = _descriptor.Descriptor(
  name='ListDirRequest',
  full_name='dfs.ListDirRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='dfs.ListDirRequest.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=244,
  serialized_end=274,
)


_LISTDIRREPLY = _descriptor.Descriptor(
  name='ListDirReply',
  full_name='dfs.ListDirReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='list', full_name='dfs.ListDirReply.list', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='dfs.ListDirReply.status', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=276,
  serialized_end=320,
)


_APPENDFILEREQUEST = _descriptor.Descriptor(
  name='AppendFileRequest',
  full_name='dfs.AppendFileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='dfs.AppendFileRequest.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='dfs.AppendFileRequest.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=322,
  serialized_end=369,
)


_APPENDFILEREPLY = _descriptor.Descriptor(
  name='AppendFileReply',
  full_name='dfs.AppendFileReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='dfs.AppendFileReply.status', index=0,
      number=1, type=8, cpp_type=7, label=1,
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
  serialized_start=371,
  serialized_end=404,
)


_WRITEFILEREQUEST = _descriptor.Descriptor(
  name='WriteFileRequest',
  full_name='dfs.WriteFileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='dfs.WriteFileRequest.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='dfs.WriteFileRequest.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=406,
  serialized_end=452,
)


_WRITEFILEREPLY = _descriptor.Descriptor(
  name='WriteFileReply',
  full_name='dfs.WriteFileReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='dfs.WriteFileReply.status', index=0,
      number=1, type=8, cpp_type=7, label=1,
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
  serialized_start=454,
  serialized_end=486,
)


_TRUNCATEFILEREQUEST = _descriptor.Descriptor(
  name='TruncateFileRequest',
  full_name='dfs.TruncateFileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='dfs.TruncateFileRequest.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=488,
  serialized_end=523,
)


_TRUNCATEFILEREPLY = _descriptor.Descriptor(
  name='TruncateFileReply',
  full_name='dfs.TruncateFileReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='dfs.TruncateFileReply.status', index=0,
      number=1, type=8, cpp_type=7, label=1,
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
  serialized_start=525,
  serialized_end=560,
)


_REMOVEFILEREQUEST = _descriptor.Descriptor(
  name='RemoveFileRequest',
  full_name='dfs.RemoveFileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='dfs.RemoveFileRequest.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=562,
  serialized_end=595,
)


_REMOVEFILEREPLY = _descriptor.Descriptor(
  name='RemoveFileReply',
  full_name='dfs.RemoveFileReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='dfs.RemoveFileReply.status', index=0,
      number=1, type=8, cpp_type=7, label=1,
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
  serialized_start=597,
  serialized_end=630,
)


_READFILEREQUEST = _descriptor.Descriptor(
  name='ReadFileRequest',
  full_name='dfs.ReadFileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='dfs.ReadFileRequest.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=632,
  serialized_end=663,
)


_READFILEREPLY = _descriptor.Descriptor(
  name='ReadFileReply',
  full_name='dfs.ReadFileReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fileContent', full_name='dfs.ReadFileReply.fileContent', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='dfs.ReadFileReply.status', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=665,
  serialized_end=717,
)


_DOWNLOADFILEREQUEST = _descriptor.Descriptor(
  name='DownloadFileRequest',
  full_name='dfs.DownloadFileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='dfs.DownloadFileRequest.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=719,
  serialized_end=754,
)


_DOWNLOADFILEREPLY = _descriptor.Descriptor(
  name='DownloadFileReply',
  full_name='dfs.DownloadFileReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fileContent', full_name='dfs.DownloadFileReply.fileContent', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='dfs.DownloadFileReply.status', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=756,
  serialized_end=812,
)

DESCRIPTOR.message_types_by_name['SaveStorageServerRequest'] = _SAVESTORAGESERVERREQUEST
DESCRIPTOR.message_types_by_name['SaveStorageServerReply'] = _SAVESTORAGESERVERREPLY
DESCRIPTOR.message_types_by_name['CreateFileRequest'] = _CREATEFILEREQUEST
DESCRIPTOR.message_types_by_name['CreateFileReply'] = _CREATEFILEREPLY
DESCRIPTOR.message_types_by_name['ListDirRequest'] = _LISTDIRREQUEST
DESCRIPTOR.message_types_by_name['ListDirReply'] = _LISTDIRREPLY
DESCRIPTOR.message_types_by_name['AppendFileRequest'] = _APPENDFILEREQUEST
DESCRIPTOR.message_types_by_name['AppendFileReply'] = _APPENDFILEREPLY
DESCRIPTOR.message_types_by_name['WriteFileRequest'] = _WRITEFILEREQUEST
DESCRIPTOR.message_types_by_name['WriteFileReply'] = _WRITEFILEREPLY
DESCRIPTOR.message_types_by_name['TruncateFileRequest'] = _TRUNCATEFILEREQUEST
DESCRIPTOR.message_types_by_name['TruncateFileReply'] = _TRUNCATEFILEREPLY
DESCRIPTOR.message_types_by_name['RemoveFileRequest'] = _REMOVEFILEREQUEST
DESCRIPTOR.message_types_by_name['RemoveFileReply'] = _REMOVEFILEREPLY
DESCRIPTOR.message_types_by_name['ReadFileRequest'] = _READFILEREQUEST
DESCRIPTOR.message_types_by_name['ReadFileReply'] = _READFILEREPLY
DESCRIPTOR.message_types_by_name['DownloadFileRequest'] = _DOWNLOADFILEREQUEST
DESCRIPTOR.message_types_by_name['DownloadFileReply'] = _DOWNLOADFILEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SaveStorageServerRequest = _reflection.GeneratedProtocolMessageType('SaveStorageServerRequest', (_message.Message,), dict(
  DESCRIPTOR = _SAVESTORAGESERVERREQUEST,
  __module__ = 'dfs_pb2'
  # @@protoc_insertion_point(class_scope:dfs.SaveStorageServerRequest)
  ))
_sym_db.RegisterMessage(SaveStorageServerRequest)

SaveStorageServerReply = _reflection.GeneratedProtocolMessageType('SaveStorageServerReply', (_message.Message,), dict(
  DESCRIPTOR = _SAVESTORAGESERVERREPLY,
  __module__ = 'dfs_pb2'
  # @@protoc_insertion_point(class_scope:dfs.SaveStorageServerReply)
  ))
_sym_db.RegisterMessage(SaveStorageServerReply)

CreateFileRequest = _reflection.GeneratedProtocolMessageType('CreateFileRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEFILEREQUEST,
  __module__ = 'dfs_pb2'
  # @@protoc_insertion_point(class_scope:dfs.CreateFileRequest)
  ))
_sym_db.RegisterMessage(CreateFileRequest)

CreateFileReply = _reflection.GeneratedProtocolMessageType('CreateFileReply', (_message.Message,), dict(
  DESCRIPTOR = _CREATEFILEREPLY,
  __module__ = 'dfs_pb2'
  # @@protoc_insertion_point(class_scope:dfs.CreateFileReply)
  ))
_sym_db.RegisterMessage(CreateFileReply)

ListDirRequest = _reflection.GeneratedProtocolMessageType('ListDirRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTDIRREQUEST,
  __module__ = 'dfs_pb2'
  # @@protoc_insertion_point(class_scope:dfs.ListDirRequest)
  ))
_sym_db.RegisterMessage(ListDirRequest)

ListDirReply = _reflection.GeneratedProtocolMessageType('ListDirReply', (_message.Message,), dict(
  DESCRIPTOR = _LISTDIRREPLY,
  __module__ = 'dfs_pb2'
  # @@protoc_insertion_point(class_scope:dfs.ListDirReply)
  ))
_sym_db.RegisterMessage(ListDirReply)

AppendFileRequest = _reflection.GeneratedProtocolMessageType('AppendFileRequest', (_message.Message,), dict(
  DESCRIPTOR = _APPENDFILEREQUEST,
  __module__ = 'dfs_pb2'
  # @@protoc_insertion_point(class_scope:dfs.AppendFileRequest)
  ))
_sym_db.RegisterMessage(AppendFileRequest)

AppendFileReply = _reflection.GeneratedProtocolMessageType('AppendFileReply', (_message.Message,), dict(
  DESCRIPTOR = _APPENDFILEREPLY,
  __module__ = 'dfs_pb2'
  # @@protoc_insertion_point(class_scope:dfs.AppendFileReply)
  ))
_sym_db.RegisterMessage(AppendFileReply)

WriteFileRequest = _reflection.GeneratedProtocolMessageType('WriteFileRequest', (_message.Message,), dict(
  DESCRIPTOR = _WRITEFILEREQUEST,
  __module__ = 'dfs_pb2'
  # @@protoc_insertion_point(class_scope:dfs.WriteFileRequest)
  ))
_sym_db.RegisterMessage(WriteFileRequest)

WriteFileReply = _reflection.GeneratedProtocolMessageType('WriteFileReply', (_message.Message,), dict(
  DESCRIPTOR = _WRITEFILEREPLY,
  __module__ = 'dfs_pb2'
  # @@protoc_insertion_point(class_scope:dfs.WriteFileReply)
  ))
_sym_db.RegisterMessage(WriteFileReply)

TruncateFileRequest = _reflection.GeneratedProtocolMessageType('TruncateFileRequest', (_message.Message,), dict(
  DESCRIPTOR = _TRUNCATEFILEREQUEST,
  __module__ = 'dfs_pb2'
  # @@protoc_insertion_point(class_scope:dfs.TruncateFileRequest)
  ))
_sym_db.RegisterMessage(TruncateFileRequest)

TruncateFileReply = _reflection.GeneratedProtocolMessageType('TruncateFileReply', (_message.Message,), dict(
  DESCRIPTOR = _TRUNCATEFILEREPLY,
  __module__ = 'dfs_pb2'
  # @@protoc_insertion_point(class_scope:dfs.TruncateFileReply)
  ))
_sym_db.RegisterMessage(TruncateFileReply)

RemoveFileRequest = _reflection.GeneratedProtocolMessageType('RemoveFileRequest', (_message.Message,), dict(
  DESCRIPTOR = _REMOVEFILEREQUEST,
  __module__ = 'dfs_pb2'
  # @@protoc_insertion_point(class_scope:dfs.RemoveFileRequest)
  ))
_sym_db.RegisterMessage(RemoveFileRequest)

RemoveFileReply = _reflection.GeneratedProtocolMessageType('RemoveFileReply', (_message.Message,), dict(
  DESCRIPTOR = _REMOVEFILEREPLY,
  __module__ = 'dfs_pb2'
  # @@protoc_insertion_point(class_scope:dfs.RemoveFileReply)
  ))
_sym_db.RegisterMessage(RemoveFileReply)

ReadFileRequest = _reflection.GeneratedProtocolMessageType('ReadFileRequest', (_message.Message,), dict(
  DESCRIPTOR = _READFILEREQUEST,
  __module__ = 'dfs_pb2'
  # @@protoc_insertion_point(class_scope:dfs.ReadFileRequest)
  ))
_sym_db.RegisterMessage(ReadFileRequest)

ReadFileReply = _reflection.GeneratedProtocolMessageType('ReadFileReply', (_message.Message,), dict(
  DESCRIPTOR = _READFILEREPLY,
  __module__ = 'dfs_pb2'
  # @@protoc_insertion_point(class_scope:dfs.ReadFileReply)
  ))
_sym_db.RegisterMessage(ReadFileReply)

DownloadFileRequest = _reflection.GeneratedProtocolMessageType('DownloadFileRequest', (_message.Message,), dict(
  DESCRIPTOR = _DOWNLOADFILEREQUEST,
  __module__ = 'dfs_pb2'
  # @@protoc_insertion_point(class_scope:dfs.DownloadFileRequest)
  ))
_sym_db.RegisterMessage(DownloadFileRequest)

DownloadFileReply = _reflection.GeneratedProtocolMessageType('DownloadFileReply', (_message.Message,), dict(
  DESCRIPTOR = _DOWNLOADFILEREPLY,
  __module__ = 'dfs_pb2'
  # @@protoc_insertion_point(class_scope:dfs.DownloadFileReply)
  ))
_sym_db.RegisterMessage(DownloadFileReply)



_DFS = _descriptor.ServiceDescriptor(
  name='DFS',
  full_name='dfs.DFS',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=815,
  serialized_end=1393,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateFile',
    full_name='dfs.DFS.CreateFile',
    index=0,
    containing_service=None,
    input_type=_CREATEFILEREQUEST,
    output_type=_CREATEFILEREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListDir',
    full_name='dfs.DFS.ListDir',
    index=1,
    containing_service=None,
    input_type=_LISTDIRREQUEST,
    output_type=_LISTDIRREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AppendFile',
    full_name='dfs.DFS.AppendFile',
    index=2,
    containing_service=None,
    input_type=_APPENDFILEREQUEST,
    output_type=_APPENDFILEREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='WriteFile',
    full_name='dfs.DFS.WriteFile',
    index=3,
    containing_service=None,
    input_type=_WRITEFILEREQUEST,
    output_type=_WRITEFILEREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TruncateFile',
    full_name='dfs.DFS.TruncateFile',
    index=4,
    containing_service=None,
    input_type=_TRUNCATEFILEREQUEST,
    output_type=_TRUNCATEFILEREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RemoveFile',
    full_name='dfs.DFS.RemoveFile',
    index=5,
    containing_service=None,
    input_type=_REMOVEFILEREQUEST,
    output_type=_REMOVEFILEREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ReadFile',
    full_name='dfs.DFS.ReadFile',
    index=6,
    containing_service=None,
    input_type=_READFILEREQUEST,
    output_type=_READFILEREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DownloadFile',
    full_name='dfs.DFS.DownloadFile',
    index=7,
    containing_service=None,
    input_type=_DOWNLOADFILEREQUEST,
    output_type=_DOWNLOADFILEREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SaveStorageServer',
    full_name='dfs.DFS.SaveStorageServer',
    index=8,
    containing_service=None,
    input_type=_SAVESTORAGESERVERREQUEST,
    output_type=_SAVESTORAGESERVERREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DFS)

DESCRIPTOR.services_by_name['DFS'] = _DFS

# @@protoc_insertion_point(module_scope)
