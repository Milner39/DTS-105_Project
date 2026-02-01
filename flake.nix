{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs, ... }:
  let
    system = "x86_64-linux";
    pkgs = import nixpkgs { inherit system;
      config.allowUnfree = true;
    };
  in
  {
    # nix develop
    devShells.${system}.default = pkgs.mkShell {
      packages = with pkgs; [
        uv
        python313
        python313Packages.tkinter
      ];

      UV_PYTHON_DOWNLOADS = "never";
    };
  };
}
