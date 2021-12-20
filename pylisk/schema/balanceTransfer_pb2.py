# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: balanceTransfer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="balanceTransfer.proto",
    package="tutorial",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x15\x62\x61lanceTransfer.proto\x12\x08tutorial"\x8d\x03\n\x0f\x42\x61lanceTransfer\x12\x15\n\x08moduleID\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x14\n\x07\x61ssetID\x18\x02 \x01(\rH\x01\x88\x01\x01\x12\x12\n\x05nonce\x18\x03 \x01(\x04H\x02\x88\x01\x01\x12\x10\n\x03\x66\x65\x65\x18\x04 \x01(\x04H\x03\x88\x01\x01\x12\x1c\n\x0fsenderPublicKey\x18\x05 \x01(\x0cH\x04\x88\x01\x01\x12\x33\n\x05\x61sset\x18\x06 \x01(\x0b\x32\x1f.tutorial.BalanceTransfer.AssetH\x05\x88\x01\x01\x12\x12\n\nsignatures\x18\x07 \x03(\x0c\x1aw\n\x05\x41sset\x12\x13\n\x06\x61mount\x18\x01 \x01(\x04H\x00\x88\x01\x01\x12\x1d\n\x10recipientAddress\x18\x02 \x01(\x0cH\x01\x88\x01\x01\x12\x11\n\x04\x64\x61ta\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\t\n\x07_amountB\x13\n\x11_recipientAddressB\x07\n\x05_dataB\x0b\n\t_moduleIDB\n\n\x08_assetIDB\x08\n\x06_nonceB\x06\n\x04_feeB\x12\n\x10_senderPublicKeyB\x08\n\x06_assetb\x06proto3',
)


_BALANCETRANSFER_ASSET = _descriptor.Descriptor(
    name="Asset",
    full_name="tutorial.BalanceTransfer.Asset",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="amount",
            full_name="tutorial.BalanceTransfer.Asset.amount",
            index=0,
            number=1,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="recipientAddress",
            full_name="tutorial.BalanceTransfer.Asset.recipientAddress",
            index=1,
            number=2,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="data",
            full_name="tutorial.BalanceTransfer.Asset.data",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="_amount",
            full_name="tutorial.BalanceTransfer.Asset._amount",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_recipientAddress",
            full_name="tutorial.BalanceTransfer.Asset._recipientAddress",
            index=1,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_data",
            full_name="tutorial.BalanceTransfer.Asset._data",
            index=2,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
    ],
    serialized_start=241,
    serialized_end=360,
)

_BALANCETRANSFER = _descriptor.Descriptor(
    name="BalanceTransfer",
    full_name="tutorial.BalanceTransfer",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="moduleID",
            full_name="tutorial.BalanceTransfer.moduleID",
            index=0,
            number=1,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="assetID",
            full_name="tutorial.BalanceTransfer.assetID",
            index=1,
            number=2,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="nonce",
            full_name="tutorial.BalanceTransfer.nonce",
            index=2,
            number=3,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="fee",
            full_name="tutorial.BalanceTransfer.fee",
            index=3,
            number=4,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="senderPublicKey",
            full_name="tutorial.BalanceTransfer.senderPublicKey",
            index=4,
            number=5,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="asset",
            full_name="tutorial.BalanceTransfer.asset",
            index=5,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="signatures",
            full_name="tutorial.BalanceTransfer.signatures",
            index=6,
            number=7,
            type=12,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[
        _BALANCETRANSFER_ASSET,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="_moduleID",
            full_name="tutorial.BalanceTransfer._moduleID",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_assetID",
            full_name="tutorial.BalanceTransfer._assetID",
            index=1,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_nonce",
            full_name="tutorial.BalanceTransfer._nonce",
            index=2,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_fee",
            full_name="tutorial.BalanceTransfer._fee",
            index=3,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_senderPublicKey",
            full_name="tutorial.BalanceTransfer._senderPublicKey",
            index=4,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_asset",
            full_name="tutorial.BalanceTransfer._asset",
            index=5,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
    ],
    serialized_start=36,
    serialized_end=433,
)

_BALANCETRANSFER_ASSET.containing_type = _BALANCETRANSFER
_BALANCETRANSFER_ASSET.oneofs_by_name["_amount"].fields.append(
    _BALANCETRANSFER_ASSET.fields_by_name["amount"]
)
_BALANCETRANSFER_ASSET.fields_by_name[
    "amount"
].containing_oneof = _BALANCETRANSFER_ASSET.oneofs_by_name["_amount"]
_BALANCETRANSFER_ASSET.oneofs_by_name["_recipientAddress"].fields.append(
    _BALANCETRANSFER_ASSET.fields_by_name["recipientAddress"]
)
_BALANCETRANSFER_ASSET.fields_by_name[
    "recipientAddress"
].containing_oneof = _BALANCETRANSFER_ASSET.oneofs_by_name["_recipientAddress"]
_BALANCETRANSFER_ASSET.oneofs_by_name["_data"].fields.append(
    _BALANCETRANSFER_ASSET.fields_by_name["data"]
)
_BALANCETRANSFER_ASSET.fields_by_name[
    "data"
].containing_oneof = _BALANCETRANSFER_ASSET.oneofs_by_name["_data"]
_BALANCETRANSFER.fields_by_name["asset"].message_type = _BALANCETRANSFER_ASSET
_BALANCETRANSFER.oneofs_by_name["_moduleID"].fields.append(
    _BALANCETRANSFER.fields_by_name["moduleID"]
)
_BALANCETRANSFER.fields_by_name["moduleID"].containing_oneof = _BALANCETRANSFER.oneofs_by_name[
    "_moduleID"
]
_BALANCETRANSFER.oneofs_by_name["_assetID"].fields.append(
    _BALANCETRANSFER.fields_by_name["assetID"]
)
_BALANCETRANSFER.fields_by_name["assetID"].containing_oneof = _BALANCETRANSFER.oneofs_by_name[
    "_assetID"
]
_BALANCETRANSFER.oneofs_by_name["_nonce"].fields.append(_BALANCETRANSFER.fields_by_name["nonce"])
_BALANCETRANSFER.fields_by_name["nonce"].containing_oneof = _BALANCETRANSFER.oneofs_by_name[
    "_nonce"
]
_BALANCETRANSFER.oneofs_by_name["_fee"].fields.append(_BALANCETRANSFER.fields_by_name["fee"])
_BALANCETRANSFER.fields_by_name["fee"].containing_oneof = _BALANCETRANSFER.oneofs_by_name["_fee"]
_BALANCETRANSFER.oneofs_by_name["_senderPublicKey"].fields.append(
    _BALANCETRANSFER.fields_by_name["senderPublicKey"]
)
_BALANCETRANSFER.fields_by_name[
    "senderPublicKey"
].containing_oneof = _BALANCETRANSFER.oneofs_by_name["_senderPublicKey"]
_BALANCETRANSFER.oneofs_by_name["_asset"].fields.append(_BALANCETRANSFER.fields_by_name["asset"])
_BALANCETRANSFER.fields_by_name["asset"].containing_oneof = _BALANCETRANSFER.oneofs_by_name[
    "_asset"
]
DESCRIPTOR.message_types_by_name["BalanceTransfer"] = _BALANCETRANSFER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BalanceTransfer = _reflection.GeneratedProtocolMessageType(
    "BalanceTransfer",
    (_message.Message,),
    {
        "Asset": _reflection.GeneratedProtocolMessageType(
            "Asset",
            (_message.Message,),
            {
                "DESCRIPTOR": _BALANCETRANSFER_ASSET,
                "__module__": "balanceTransfer_pb2"
                # @@protoc_insertion_point(class_scope:tutorial.BalanceTransfer.Asset)
            },
        ),
        "DESCRIPTOR": _BALANCETRANSFER,
        "__module__": "balanceTransfer_pb2"
        # @@protoc_insertion_point(class_scope:tutorial.BalanceTransfer)
    },
)
_sym_db.RegisterMessage(BalanceTransfer)
_sym_db.RegisterMessage(BalanceTransfer.Asset)


# @@protoc_insertion_point(module_scope)