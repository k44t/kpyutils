{ lib, rsync, python, buildPythonPackage, poetry-core }:



buildPythonPackage rec {
  pname = "kpyutils";
  version = "0.1.0";
  disabled = python.pythonOlder "3.7";
  
  src = builtins.path { path = ./..; };

  nativeBuildInputs = [
    rsync
    poetry-core
  ];


  propagatedBuildInputs = with python.pkgs; [
    pyyaml
  ];
  

  format = "pyproject";

  
  unpackPhase = ''
    rsync -av --exclude='.venv' --exclude='.vscode' --exclude='.notifier' --no-perms --no-group --no-owner ${src}/ ./
  '';


  postInstall = ''
    # the pythonOutputDistHook will fail if this directory does not exist
    # even though whatever happened before already put all files in their proper paces
    mkdir -p $out/dist
  '';


  doCheck = false;
  # dontUnpack = true;

  meta = with lib; {
    description = "some utility functions";
    license = licenses.mit;
    maintainers = with maintainers; [ ];
  };
}