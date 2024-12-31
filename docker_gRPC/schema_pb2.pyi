from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ClientData(_message.Message):
    __slots__ = ("internet_service", "number_dependents", "number_referrals", "satisfaction_score", "tenure_in_months", "total_long_distance_charges", "total_revenue", "contract", "payment_method")
    INTERNET_SERVICE_FIELD_NUMBER: _ClassVar[int]
    NUMBER_DEPENDENTS_FIELD_NUMBER: _ClassVar[int]
    NUMBER_REFERRALS_FIELD_NUMBER: _ClassVar[int]
    SATISFACTION_SCORE_FIELD_NUMBER: _ClassVar[int]
    TENURE_IN_MONTHS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LONG_DISTANCE_CHARGES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_REVENUE_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    internet_service: int
    number_dependents: int
    number_referrals: int
    satisfaction_score: int
    tenure_in_months: int
    total_long_distance_charges: float
    total_revenue: float
    contract: str
    payment_method: str
    def __init__(self, internet_service: _Optional[int] = ..., number_dependents: _Optional[int] = ..., number_referrals: _Optional[int] = ..., satisfaction_score: _Optional[int] = ..., tenure_in_months: _Optional[int] = ..., total_long_distance_charges: _Optional[float] = ..., total_revenue: _Optional[float] = ..., contract: _Optional[str] = ..., payment_method: _Optional[str] = ...) -> None: ...

class PredictionResponse(_message.Message):
    __slots__ = ("pred",)
    PRED_FIELD_NUMBER: _ClassVar[int]
    pred: str
    def __init__(self, pred: _Optional[str] = ...) -> None: ...
