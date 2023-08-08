"""
"""

from pydantic import BaseModel, FieldValidationInfo
from pydantic import confloat, field_validator, conint
from typing import Optional
from __programs import Programs


class ElectricalPulse(BaseModel):
    electrical_pulse_time: confloat(gt=0.0) | None = None
    electrical_pulse_rise_time: confloat(gt=0.0) | None = None
    electrical_pulse_fall_time: confloat(gt=0.0) | None = None

    # Validations
    @field_validator("electrical_pulse_rise_time")
    @classmethod
    def electrical_pulse_rise_le_total(
        cls, rise_time: float, info: FieldValidationInfo
    ):
        if rise_time > info.data["electrical_pulse_time"]:
            raise ValueError("electrical-pulse-rise-time > electrical-pulse-time")
        return rise_time

    @field_validator("electrical_pulse_fall_time")
    @classmethod
    def electrical_pulse_fall_le_total(
        cls, fall_time: float, info: FieldValidationInfo
    ):
        if fall_time > info.data["electrical_pulse_time"]:
            raise ValueError("electrical-pulse-fall-time > electrical-pulse-time")
        return fall_time

    # @field_validator("electrical_pulse_fall_time")
    # @classmethod
    # def electrical_pulse_rise_fall_le_total(
    #     cls, fall_time: float, info: FieldValidationInfo
    # ):
    #     if (
    #         info.data["electrical_pulse_time"]
    #         < fall_time + info.data["electrical_pulse_rise_time"]
    #     ):
    #         raise ValueError(
    #             "electrical-pulse-time < (electrical-pulse-rise-time + electrical-pulse-fall-time)"
    #         )
    #     return fall_time


class Simulation(BaseModel):
    # Program
    program: Programs = Programs.benchmark

    # Electrical pulse
    electrical_pulse: ElectricalPulse | None = None

    # Exchange stiffness
    exchange_stiffness_maximum_angle: confloat(ge=0.0, le=180.0) | None = None
    exchange_stiffness_angle_increment: confloat(ge=0.0, le=90.0) | None = None


electrical_pulse_params = {
    "electrical_pulse_time": 1.2,
    "electrical_pulse_rise_time": 0.2,
    "electrical_pulse_fall_time": 0.9,
}

test_sim = Simulation(electrical_pulse=electrical_pulse_params)

print(test_sim.electrical_pulse.electrical_pulse_fall_time)
