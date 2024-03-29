from enum import Enum

class Programs(str, Enum):
    benchmark = "benchmark",
    time_series = "time-series",
    hysteresis_loop = "hysteresis-loop",
    static_hysteresis_loop = "static-hysteresis-loop",
    curie_temperature = "curie-temperature",
    field_cool = "field-cool",
    localaised_field_cool = "localised-field-cool",
    laser_pulse = "laser-pulse",
    hamr_simulation = "hamr-simulation",
    cmc_anisotropy = "cmc-anisotropy",
    hybrid_cmc = "hybrid-cmc",
    reverse_hybrid_cmc = "reverse-hybrid-cmc",
    lagrange_multiplier = "LaGrange-Multiplier",
    partial_hysteresis_loop = "partial-hysteresis-loop",
    localised_temperature_pulse = "localised-temperature-pulse",
    effective_damping = "effective-damping",
    fmr = "fmr",
    diagnostic_boltzmann = "diagnostic-boltzmann",
    setting = "setting",
    domain_wall = "domain-wall",
    exchange_stiffness = "exchange-stiffness",
    electrical_pulse = "electrical-pulse",
    mm_a_calculation = "mm-A-calculation",
    field_sweep = "field-sweep",
    disk_tracks = "disk-tracks",
    diagnostic_boltzmann_micromagnetic_llg = "diagnostic-boltzmann-micromagnetic-llg"