%global tl_name subdocs
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Multifile documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/subdocs
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/subdocs.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/subdocs.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is an experimental package aiming to provide a different approach
for multidocument works (mainly, books with a document per chapter).
Unlike the \include mechanism, every subdocument is a complete normal
LaTeX document and may be typeset separately. What the package does is
sharing the .aux files. The present release is an alpha version, and no
attempt has yet been made to allow it to work with, say, hyperref.

