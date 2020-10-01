from .handlers import TutorialHandler

def _jupyter_server_extension_paths():
    return [{
        'module': 'martha'
    }]

def load_jupyter_server_extension(server_app):
    handlers = [('/martha/hello', TutorialHandler)]
    server_app.web_app.add_handlers('.*$', handlers)