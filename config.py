CFG = {
    'port': 5000,
    'debug': True,
    'secret_key': '12345678',
    'users': {
        'admin': {'password': 'admin'}
    },
    'mqtt': {
        'host': 'localhost',
        'port': 44987
    },
    'controls': [
        {
            'name': 'Time',
            'mqttTopic': 'system/time',
            'actions': [
                {'name': '6:00', 'mqttMessage': '6:00:00'},
                {'name': '12:00', 'mqttMessage': '12:00:00'},
                {'name': '18:00', 'mqttMessage': '18:00:00'},
                {'name': '24:00', 'mqttMessage': '24:00:00'}
            ]
        },
        {
            'name': 'Weather',
            'mqttTopic': 'system/weather',
            'actions': [
                {'name': 'Clear', 'mqttMessage': 'clear'},
                {'name': 'Raining', 'mqttMessage': 'raining'},
                {'name': 'Thundering', 'mqttMessage': 'thundering'}
            ]
        },
        {
            'name': 'All lights',
            'mqttTopic': 'room/allLights',
            'actions': [
                {'name': 'Turn on', 'mqttMessage': 'turn on'},
                {'name': 'Turn off', 'mqttMessage': 'turn off'}
            ]
        },
        {
            'name': 'Lamp 1',
            'mqttTopic': 'L01/light1',
            'actions': [
                {'name': 'Turn off', 'mqttMessage': 'turn off'},
                {'name': '10%', 'mqttMessage': '10'},
                {'name': '20%', 'mqttMessage': '20'},
                {'name': '30%', 'mqttMessage': '30'},
                {'name': '40%', 'mqttMessage': '40'},
                {'name': '50%', 'mqttMessage': '50'},
                {'name': '60%', 'mqttMessage': '60'},
                {'name': '70%', 'mqttMessage': '70'},
                {'name': '80%', 'mqttMessage': '80'},
                {'name': '90%', 'mqttMessage': '90'},
                {'name': '100%', 'mqttMessage': '100'}
            ]
        },
        {
            'name': 'Lamp 2',
            'mqttTopic': 'L01/light2',
            'actions': [
                {'name': 'Turn off', 'mqttMessage': 'turn off'},
                {'name': '10%', 'mqttMessage': '10'},
                {'name': '20%', 'mqttMessage': '20'},
                {'name': '30%', 'mqttMessage': '30'},
                {'name': '40%', 'mqttMessage': '40'},
                {'name': '50%', 'mqttMessage': '50'},
                {'name': '60%', 'mqttMessage': '60'},
                {'name': '70%', 'mqttMessage': '70'},
                {'name': '80%', 'mqttMessage': '80'},
                {'name': '90%', 'mqttMessage': '90'},
                {'name': '100%', 'mqttMessage': '100'}
            ]
        },
        {
            'name': 'Smart Socket 1',
            'mqttTopic': 'cmnd/ss1/POWER',
            'actions': [
                {'name': 'Turn on', 'mqttMessage': 'on'},
                {'name': 'Turn off', 'mqttMessage': 'off'}
            ]
        },
        {
            'name': 'Smart Socket 2',
            'mqttTopic': 'cmnd/ss2/POWER',
            'actions': [
                {'name': 'Turn on', 'mqttMessage': 'on'},
                {'name': 'Turn off', 'mqttMessage': 'off'}
            ]
        },
        {
            'name': 'Intel Edison 1',
            'mqttTopic': '01/light',
            'actions': [
                {'name': 'Turn on', 'mqttMessage': 'turn on'},
                {'name': 'Turn off', 'mqttMessage': 'turn off'}
            ]
        },
        {
            'name': 'Intel Edison 2',
            'mqttTopic': '02/light',
            'actions': [
                {'name': 'Turn on', 'mqttMessage': 'turn on'},
                {'name': 'Turn off', 'mqttMessage': 'turn off'}
            ]
        },
        {
            'name': 'Intel Edison 3',
            'mqttTopic': '03/light',
            'actions': [
                {'name': 'Turn on', 'mqttMessage': 'turn on'},
                {'name': 'Turn off', 'mqttMessage': 'turn off'}
            ]
        },
        {
            'name': 'Intel Edison 4',
            'mqttTopic': '04/light',
            'actions': [
                {'name': 'Turn on', 'mqttMessage': 'turn on'},
                {'name': 'Turn off', 'mqttMessage': 'turn off'}
            ]
        }
    ]
}