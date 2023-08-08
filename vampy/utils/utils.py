def load_vampire_template(input_file: str) -> list[list[str]]:
    """Load file of params to list"""
    _params = []
    # Capture parameter name and value
    with open(input_file, "r") as inp:
        for line in inp:
            param_name = line.split(":")[-1].split("=")[0].strip(" ").strip("\n")
            if "=" in line:
                param_def = line.split("=")[-1].strip(" ").strip("\n")
                param_val = param_def.split("!")[0].strip(" ").strip("\n")
                param_unit = param_def.split("!")[1].strip(" ").strip("\n")
            else:
                param_val = False
                param_unit = False
            _params.append([param_name, param_val, param_unit])
    return _params
