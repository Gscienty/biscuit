from biscuit.ipc_server.app import app, config, io

if __name__ == '__main__':
    if not config.load():
        print('unable to load config', file=io.error())
        exit(1)
    ipc_server_config = config.config()['ipc_server']
    app.run(host=ipc_server_config['host'])
