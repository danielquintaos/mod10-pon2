from flask import Flask

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    
    # Configurations can be set here
    app.config['DEBUG'] = True  # Enable Flask's debug mode
    
    # Importing routes from app.py within the same directory
    from .app import get_items, create_item, get_item, update_item, delete_item

    # Register routes
    app.add_url_rule('/api/items', view_func=get_items, methods=['GET'])
    app.add_url_rule('/api/items', view_func=create_item, methods=['POST'])
    app.add_url_rule('/api/items/<string:item_id>', view_func=get_item, methods=['GET'])
    app.add_url_rule('/api/items/<string:item_id>', view_func=update_item, methods=['PUT'])
    app.add_url_rule('/api/items/<string:item_id>', view_func=delete_item, methods=['DELETE'])

    return app
