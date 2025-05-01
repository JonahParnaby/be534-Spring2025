{pkgs}: {
  deps = [
    pkgs.q
    pkgs.haskellPackages.daemons
    pkgs.imagemagick_light
  ];
}
