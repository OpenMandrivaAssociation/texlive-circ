%global tl_name circ
%global tl_revision 62977

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Macros for typesetting circuit diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/diagrams/circ
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/circ.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/circ.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/circ.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Several electrical symbols like resistor, capacitor, transistors etc.,
are defined. The symbols can be connected with wires. The package also
contains an American resistor symbol for those of us on that side of the
Atlantic. The package also has simple facilities for producing optics
diagrams; however, no-one would deny that the PSTricks pst-optic
package, or the MetaPost makecirc package do the job better.

