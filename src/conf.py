dataframe = {
    "GROUND_SPEED": {
        "start_bit": 1,
        "record_length": 12,
        "record_resolution": 0.25,
        "format": "BNR",
        "subframes": [1, 2, 3, 4],
        "word": 18,
        "sign": False,
    },
    "RADIO_ALTITUDE_15": {
        "start_bit": 1,
        "record_length": 6,
        "record_resolution": 64,
        "format": "BNR",
        "subframes": [1, 2, 3, 4],
        "word": 15,
        "sign": False,
    },
    "RADIO_ALTITUDE_16": {
        "start_bit": 1,
        "record_length": 6,
        "record_resolution": 1,
        "format": "BNR",
        "subframes": [1, 2, 3, 4],
        "word": 16,
        "sign": False,
    },
    "VERTICAL_SPEED_24": {
        "start_bit": 1,
        "record_length": 11,
        "record_resolution": 1,
        "format": "BNR",
        "subframes": [1, 2, 3, 4],
        "word": 24,
        "sign": True,
    },
    "VERTICAL_SPEED_25": {
        "start_bit": 1,
        "record_length": 11,
        "record_resolution": 1,
        "format": "BNR",
        "subframes": [1, 2, 3, 4],
        "word": 25,
        "sign": True,
    },
}

interested_data = {
    "GROUND_SPEED": True,
    "RADIO_ALTITUDE_15": True,
    "RADIO_ALTITUDE_16": True,
    "VERTICAL_SPEED_24": True,
    "VERTICAL_SPEED_25": True,
}
