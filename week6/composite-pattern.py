from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import Optional, List


class UnitDSchema(UnitInfoSchema):
    pass


class UnitCSchema(UnitInfoSchema):
    percentage: Optional[float]
    is_checked: bool


class UnitBSchema(UnitInfoSchema):
    ancestor_unit_b_ids: List[int]
    descendant_unit_b_ids: List[int]
    unit_c_list: List[UnitCSchema]


class UnitASchema(UnitInfoSchema):
    is_expanded: bool
    background_color: str
    percentage: Optional[float]
    unit_b_list: List[UnitBSchema]


@dataclass
class Unit:
    parent_id: int
    unit_version_id: int
    vector_index: int
    name: str
    understandable_name: str
    chip_color: Optional[str]
    background_color: Optional[str]
    thumbnail_pc: Optional[str]
    thumbnail_mobile: Optional[str]

    def from_unit_d(self, unit_d: UnitD):
        return Unit()

    def from_unit_c(self, unit_c: UnitC):
        pass

    def from_unit_b(self, unit_b: UnitB):
        pass

    def from_unit_a(self, unit_a: UnitA):
        pass


class UnitComponent(metaclass=ABCMeta):

    @abstractmethod
    def schema(self):
        pass


class UnitAComponent(UnitComponent):
    units: List[UnitComponent]

    def __init__(self, units: List[UnitComponent]):
        self.units = units

    def schema(self):
        return UnitASchema(
            background_color="#AAAABC"
        )


class UnitBComponent(UnitComponent):
    units: List[UnitComponent]

    def __init__(self, units: List[UnitComponent]):
        self.units = units

    def schema(self, unit: Unit):
        return UnitBSchema(
            background_color="#AAAABC",
        )


class UnitDComponent(UnitComponent):
    units: List[UnitComponent]

    def __init__(self, units: List[UnitComponent]):
        self.units = units

    def schema(self, unit: Unit):
        return UnitDSchema(
            background_color="#AAAABC",
        )
