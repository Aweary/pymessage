import json

/**
 * Registers a contact in the `config.json` file
 * @param {string} user user name
 * @param {string} type user type
 * @param {string|number} number phone number
 */

def register(user, type, number):
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
        if 'contacts' not in config:
            config['contacts'] = {}
        config['contacts'][user] = {'type': type, 'number': number}
    with open('config.json', 'w') as config_file:
        config_file.write(json.dumps(config))
        print('Saved new record')
