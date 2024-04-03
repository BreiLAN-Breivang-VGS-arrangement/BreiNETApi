let
    pkgs = import <nixpkgs> {};
in pkgs.mkShell {
    packages = [
        (pkgs.python3.withPackages (python-pkgs: [
            python-pkgs.flask
            python-pkgs.flask-cors
            python-pkgs.flask-sqlalchemy
        ]))
    ];
} 