Name:           userspace-rcu
Version:        0.4.1
Release:        2%{?dist}
Summary:        RCU (read-copy-update) implementation in user space

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://www.lttng.org/?q=node/18
Source0:        http://www.lttng.org/files/urcu/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This data synchronization library provides read-side access which scales
linearly with the number of cores. It does so by allowing multiples copies
of a given data structure to live at the same time, and by monitoring
the data structure accesses to detect grace periods after which memory
reclamation is possible.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT

%check
READERS=10
WRITERS=10
DURATION=5
tests/rcutorture_qsbr
tests/rcutorture_urcu
tests/rcutorture_urcu_bp
tests/rcutorture_urcu_mb
tests/rcutorture_urcu_signal
tests/test_looplen
tests/test_mutex $READERS $WRITERS $DURATION
tests/test_perthreadlock $READERS $WRITERS $DURATION
tests/test_perthreadlock_timing $READERS $WRITERS $DURATION
tests/test_qsbr $READERS $WRITERS $DURATION
tests/test_qsbr_dynamic_link $READERS $WRITERS $DURATION
tests/test_qsbr_gc $READERS $WRITERS $DURATION
tests/test_qsbr_lgc $READERS $WRITERS $DURATION
tests/test_qsbr_timing $READERS $WRITERS $DURATION
tests/test_rwlock $READERS $WRITERS $DURATION
tests/test_rwlock_timing $READERS $WRITERS $DURATION
tests/test_uatomic $READERS $WRITERS $DURATION
tests/test_urcu $READERS $WRITERS $DURATION
tests/test_urcu_assign $READERS $WRITERS $DURATION
tests/test_urcu_assign_dynamic_link $READERS $WRITERS $DURATION
tests/test_urcu_bp $READERS $WRITERS $DURATION
tests/test_urcu_bp_dynamic_link $READERS $WRITERS $DURATION
tests/test_urcu_defer $READERS $WRITERS $DURATION
tests/test_urcu_dynamic_link $READERS $WRITERS $DURATION
tests/test_urcu_gc $READERS $WRITERS $DURATION
tests/test_urcu_lgc $READERS $WRITERS $DURATION
tests/test_urcu_mb $READERS $WRITERS $DURATION
tests/test_urcu_mb_gc $READERS $WRITERS $DURATION
tests/test_urcu_mb_lgc $READERS $WRITERS $DURATION
tests/test_urcu_signal $READERS $WRITERS $DURATION
tests/test_urcu_signal_dynamic_link $READERS $WRITERS $DURATION
tests/test_urcu_signal_gc $READERS $WRITERS $DURATION
tests/test_urcu_signal_lgc $READERS $WRITERS $DURATION
tests/test_urcu_signal_timing $READERS $WRITERS $DURATION
tests/test_urcu_signal_yield $READERS $WRITERS $DURATION
tests/test_urcu_timing $READERS $WRITERS $DURATION
tests/test_urcu_yield $READERS $WRITERS $DURATION

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc LICENSE gpl-2.0.txt lgpl-relicensing.txt lgpl-2.1.txt

%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc README
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 26 2010 Jan "Yenya" Kasprzak <kas@fi.muni.cz> 0.4.1-1
- new upstream version.

* Tue Oct 20 2009 Jan "Yenya" Kasprzak <kas@fi.muni.cz> 0.2.4-1
- Initial revision.
