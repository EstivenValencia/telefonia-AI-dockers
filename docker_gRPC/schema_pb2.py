# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: schema.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'schema.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cschema.proto\x12\x0cgrpc_service\x1a\x1egoogle/protobuf/wrappers.proto\"\xf7\x01\n\nClientData\x12\x18\n\x10internet_service\x18\x01 \x01(\x05\x12\x19\n\x11number_dependents\x18\x02 \x01(\x05\x12\x18\n\x10number_referrals\x18\x03 \x01(\x05\x12\x1a\n\x12satisfaction_score\x18\x04 \x01(\x05\x12\x18\n\x10tenure_in_months\x18\x05 \x01(\x05\x12#\n\x1btotal_long_distance_charges\x18\x06 \x01(\x02\x12\x15\n\rtotal_revenue\x18\x07 \x01(\x02\x12\x10\n\x08\x63ontract\x18\x08 \x01(\t\x12\x16\n\x0epayment_method\x18\t \x01(\t\"\"\n\x12PredictionResponse\x12\x0c\n\x04pred\x18\x01 \x01(\t2^\n\x10TelefoniaService\x12J\n\nprediction\x12\x18.grpc_service.ClientData\x1a .grpc_service.PredictionResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'schema_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CLIENTDATA']._serialized_start=63
  _globals['_CLIENTDATA']._serialized_end=310
  _globals['_PREDICTIONRESPONSE']._serialized_start=312
  _globals['_PREDICTIONRESPONSE']._serialized_end=346
  _globals['_TELEFONIASERVICE']._serialized_start=348
  _globals['_TELEFONIASERVICE']._serialized_end=442
# @@protoc_insertion_point(module_scope)