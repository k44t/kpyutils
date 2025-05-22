{pkgs, ...}: {
  nixpkgs.overlays = [
    (final: prev: {
      python3Packages = prev.python3Packages // {
        kpyutils = prev.python3Packages.callPackage ./python-package.nix {};
      };
    })
  ];

}
