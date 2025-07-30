{pkgs, ...}: {
  nixpkgs.overlays = [
    (final: prev: let
    

      kpyutils = prev.python3Packages.callPackage ./python-package.nix {};

    in
    {
      kpyutils = kpyutils;
      python3Packages = prev.python3Packages // {
        kpyutils = kpyutils;
      };
      pythonPackages = prev.pythonPackages // {
        kpyutils = kpyutils;
      };
      python = prev.python // {
        kpyutils = kpyutils;
      };
      python3 = prev.python3 // {
        kpyutils = kpyutils;
      };
    })
  ];

}
