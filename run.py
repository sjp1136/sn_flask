from sn_flask import app
# when importing from package, import happens from __init__

if __name__ == '__main__':
    app.run(port=3000, debug=True)
