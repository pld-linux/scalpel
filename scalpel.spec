Summary:	A Frugal, High Performance File Carver
Name:		scalpel
Version:	2.0
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.digitalforensicssolutions.com/Scalpel/%{name}-%{version}.tar.gz
# Source0-md5:	b0da813bf34941e79209d7fafe86a6e6
URL:		http://www.digitalforensicssolutions.com/Scalpel/
BuildRequires:	autoconf >= 2.67
BuildRequires:	automake
BuildRequires:	tre-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scalpel is a fast file carver that reads a database of header and
footer definitions and extracts matching files or data fragments from
a set of image files or raw device files. Scalpel is filesystem-
independent and will carve files from FATx, NTFS, ext2/3, HFS+, or raw
partitions. It is useful for both digital forensics investigation and
file recovery.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
# NOTE: scalpel.conf must be present in pwd
install -p %{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*.1*
