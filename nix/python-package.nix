{ lib, buildPythonPackage, python3Packages, rsync, python3, tree }:




buildPythonPackage rec {
  pname = "kpyutils";
  version = "0.1.0";

  src = ./..;
  sourceRoot = ./..;

  nativeBuildInputs = [
    tree
  ];

  propagatedBuildInputs = with python3Packages; [
    pyyaml
  ];


  format = "pyproject";


  doCheck = false;
  dontUnpack = true;

  meta = with lib; {
    description = "some utility functions";
    license = licenses.mit;
    maintainers = with maintainers; [ ];
  };
}