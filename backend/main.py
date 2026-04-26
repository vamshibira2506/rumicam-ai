def detect_behavior(input_data):
    if input_data == "low_rumination":
        return "ALERT: Possible heat cycle"
    return "Normal"

print(detect_behavior("low_rumination"))