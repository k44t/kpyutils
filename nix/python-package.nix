{ lib, buildPythonPackage, python3Packages, rsync, python3, poetry-core }:




buildPythonPackage rec {
  pname = "kpyutils";
  version = "0.1.0";

  src = builtins.path { path = ./..; };

  nativeBuildInputs = [
    rsync
    poetry-core
  ];

  unpackPhase = ''
    rsync -av --no-perms --no-group --no-owner ${src}/ ./
  '';

  propagatedBuildInputs = with python3Packages; [
    pyyaml
  ];


  format = "pyproject";


  doCheck = false;
  # dontUnpack = true;

  meta = with lib; {
    description = "some utility functions";
    license = licenses.mit;
    maintainers = with maintainers; [ ];
  };
}