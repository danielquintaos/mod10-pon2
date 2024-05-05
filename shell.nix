{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python39Full
    pkgs.python39Packages.pip
    pkgs.python39Packages.virtualenv
    pkgs.python39Packages.flask
    pkgs.python39Packages.flask_cors
    pkgs.python39Packages.gunicorn
  ];

  shellHook = ''
    export FLASK_APP=api/app.py
    export FLASK_ENV=development

    if [ ! -d ".venv" ]; then
      echo "Creating a virtual environment..."
      virtualenv .venv
    fi

    echo "Activating virtual environment..."
    source .venv/bin/activate

    echo "Installing Python dependencies..."
    pip install -r requirements.txt
  '';
}
