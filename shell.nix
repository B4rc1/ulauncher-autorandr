{ pkgs ? import <nixpkgs> {}
, ulauncher ? pkgs.ulauncher
}:
let
  my-python = pkgs.python3;
  python-with-my-packages = my-python.withPackages (p: with p; [
    websocket-client
    levenshtein
    pygobject3
    pyxdg
  ]);
in
pkgs.mkShell {
  buildInputs = with pkgs; [
    python-with-my-packages
    gtk3
  ];
  nativeBuildInputs = with pkgs; [
    gobject-introspection
  ];
  shellHook = ''
    export PYTHONPATH=${ulauncher}/lib/python3.9/site-packages:${python-with-my-packages}/${python-with-my-packages.sitePackages}
  '';
}
