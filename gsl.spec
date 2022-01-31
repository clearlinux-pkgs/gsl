#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x245FB74BAE05B3E9 (alken@colorado.edu)
#
Name     : gsl
Version  : 2.7
Release  : 18
URL      : https://mirrors.kernel.org/gnu/gsl/gsl-2.7.tar.gz
Source0  : https://mirrors.kernel.org/gnu/gsl/gsl-2.7.tar.gz
Source1  : https://mirrors.kernel.org/gnu/gsl/gsl-2.7.tar.gz.sig
Summary  : GNU Scientific Library
Group    : Development/Tools
License  : GPL-3.0
Requires: gsl-bin = %{version}-%{release}
Requires: gsl-filemap = %{version}-%{release}
Requires: gsl-info = %{version}-%{release}
Requires: gsl-lib = %{version}-%{release}
Requires: gsl-license = %{version}-%{release}
Requires: gsl-man = %{version}-%{release}
BuildRequires : sed

%description
GSL - GNU Scientific Library
============================
This is GSL, the GNU Scientific Library, a collection of numerical
routines for scientific computing.

%package bin
Summary: bin components for the gsl package.
Group: Binaries
Requires: gsl-license = %{version}-%{release}
Requires: gsl-filemap = %{version}-%{release}

%description bin
bin components for the gsl package.


%package dev
Summary: dev components for the gsl package.
Group: Development
Requires: gsl-lib = %{version}-%{release}
Requires: gsl-bin = %{version}-%{release}
Provides: gsl-devel = %{version}-%{release}
Requires: gsl = %{version}-%{release}

%description dev
dev components for the gsl package.


%package filemap
Summary: filemap components for the gsl package.
Group: Default

%description filemap
filemap components for the gsl package.


%package info
Summary: info components for the gsl package.
Group: Default

%description info
info components for the gsl package.


%package lib
Summary: lib components for the gsl package.
Group: Libraries
Requires: gsl-license = %{version}-%{release}
Requires: gsl-filemap = %{version}-%{release}

%description lib
lib components for the gsl package.


%package license
Summary: license components for the gsl package.
Group: Default

%description license
license components for the gsl package.


%package man
Summary: man components for the gsl package.
Group: Default

%description man
man components for the gsl package.


%prep
%setup -q -n gsl-2.7
cd %{_builddir}/gsl-2.7
pushd ..
cp -a gsl-2.7 buildavx2
popd
pushd ..
cp -a gsl-2.7 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1634053407
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx512/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v4"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :
cd ../buildavx512;
make %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1634053407
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gsl
cp %{_builddir}/gsl-2.7/COPYING %{buildroot}/usr/share/package-licenses/gsl/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/gsl-2.7/doc/_static/gpl.txt %{buildroot}/usr/share/package-licenses/gsl/8624bcdae55baeef00cd11d5dfcfa60f68710a02
pushd ../buildavx2/
%make_install_v3
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}
popd
pushd ../buildavx512/
%make_install_v4
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gsl-config
/usr/bin/gsl-histogram
/usr/bin/gsl-randist
/usr/share/clear/optimized-elf/bin*

%files dev
%defattr(-,root,root,-)
/usr/include/gsl/gsl_blas.h
/usr/include/gsl/gsl_blas_types.h
/usr/include/gsl/gsl_block.h
/usr/include/gsl/gsl_block_char.h
/usr/include/gsl/gsl_block_complex_double.h
/usr/include/gsl/gsl_block_complex_float.h
/usr/include/gsl/gsl_block_complex_long_double.h
/usr/include/gsl/gsl_block_double.h
/usr/include/gsl/gsl_block_float.h
/usr/include/gsl/gsl_block_int.h
/usr/include/gsl/gsl_block_long.h
/usr/include/gsl/gsl_block_long_double.h
/usr/include/gsl/gsl_block_short.h
/usr/include/gsl/gsl_block_uchar.h
/usr/include/gsl/gsl_block_uint.h
/usr/include/gsl/gsl_block_ulong.h
/usr/include/gsl/gsl_block_ushort.h
/usr/include/gsl/gsl_bspline.h
/usr/include/gsl/gsl_bst.h
/usr/include/gsl/gsl_bst_avl.h
/usr/include/gsl/gsl_bst_rb.h
/usr/include/gsl/gsl_bst_types.h
/usr/include/gsl/gsl_cblas.h
/usr/include/gsl/gsl_cdf.h
/usr/include/gsl/gsl_chebyshev.h
/usr/include/gsl/gsl_check_range.h
/usr/include/gsl/gsl_combination.h
/usr/include/gsl/gsl_complex.h
/usr/include/gsl/gsl_complex_math.h
/usr/include/gsl/gsl_const.h
/usr/include/gsl/gsl_const_cgs.h
/usr/include/gsl/gsl_const_cgsm.h
/usr/include/gsl/gsl_const_mks.h
/usr/include/gsl/gsl_const_mksa.h
/usr/include/gsl/gsl_const_num.h
/usr/include/gsl/gsl_deriv.h
/usr/include/gsl/gsl_dft_complex.h
/usr/include/gsl/gsl_dft_complex_float.h
/usr/include/gsl/gsl_dht.h
/usr/include/gsl/gsl_diff.h
/usr/include/gsl/gsl_eigen.h
/usr/include/gsl/gsl_errno.h
/usr/include/gsl/gsl_fft.h
/usr/include/gsl/gsl_fft_complex.h
/usr/include/gsl/gsl_fft_complex_float.h
/usr/include/gsl/gsl_fft_halfcomplex.h
/usr/include/gsl/gsl_fft_halfcomplex_float.h
/usr/include/gsl/gsl_fft_real.h
/usr/include/gsl/gsl_fft_real_float.h
/usr/include/gsl/gsl_filter.h
/usr/include/gsl/gsl_fit.h
/usr/include/gsl/gsl_heapsort.h
/usr/include/gsl/gsl_histogram.h
/usr/include/gsl/gsl_histogram2d.h
/usr/include/gsl/gsl_ieee_utils.h
/usr/include/gsl/gsl_inline.h
/usr/include/gsl/gsl_integration.h
/usr/include/gsl/gsl_interp.h
/usr/include/gsl/gsl_interp2d.h
/usr/include/gsl/gsl_linalg.h
/usr/include/gsl/gsl_machine.h
/usr/include/gsl/gsl_math.h
/usr/include/gsl/gsl_matrix.h
/usr/include/gsl/gsl_matrix_char.h
/usr/include/gsl/gsl_matrix_complex_double.h
/usr/include/gsl/gsl_matrix_complex_float.h
/usr/include/gsl/gsl_matrix_complex_long_double.h
/usr/include/gsl/gsl_matrix_double.h
/usr/include/gsl/gsl_matrix_float.h
/usr/include/gsl/gsl_matrix_int.h
/usr/include/gsl/gsl_matrix_long.h
/usr/include/gsl/gsl_matrix_long_double.h
/usr/include/gsl/gsl_matrix_short.h
/usr/include/gsl/gsl_matrix_uchar.h
/usr/include/gsl/gsl_matrix_uint.h
/usr/include/gsl/gsl_matrix_ulong.h
/usr/include/gsl/gsl_matrix_ushort.h
/usr/include/gsl/gsl_message.h
/usr/include/gsl/gsl_min.h
/usr/include/gsl/gsl_minmax.h
/usr/include/gsl/gsl_mode.h
/usr/include/gsl/gsl_monte.h
/usr/include/gsl/gsl_monte_miser.h
/usr/include/gsl/gsl_monte_plain.h
/usr/include/gsl/gsl_monte_vegas.h
/usr/include/gsl/gsl_movstat.h
/usr/include/gsl/gsl_multifit.h
/usr/include/gsl/gsl_multifit_nlin.h
/usr/include/gsl/gsl_multifit_nlinear.h
/usr/include/gsl/gsl_multilarge.h
/usr/include/gsl/gsl_multilarge_nlinear.h
/usr/include/gsl/gsl_multimin.h
/usr/include/gsl/gsl_multiroots.h
/usr/include/gsl/gsl_multiset.h
/usr/include/gsl/gsl_nan.h
/usr/include/gsl/gsl_ntuple.h
/usr/include/gsl/gsl_odeiv.h
/usr/include/gsl/gsl_odeiv2.h
/usr/include/gsl/gsl_permutation.h
/usr/include/gsl/gsl_permute.h
/usr/include/gsl/gsl_permute_char.h
/usr/include/gsl/gsl_permute_complex_double.h
/usr/include/gsl/gsl_permute_complex_float.h
/usr/include/gsl/gsl_permute_complex_long_double.h
/usr/include/gsl/gsl_permute_double.h
/usr/include/gsl/gsl_permute_float.h
/usr/include/gsl/gsl_permute_int.h
/usr/include/gsl/gsl_permute_long.h
/usr/include/gsl/gsl_permute_long_double.h
/usr/include/gsl/gsl_permute_matrix.h
/usr/include/gsl/gsl_permute_matrix_char.h
/usr/include/gsl/gsl_permute_matrix_complex_double.h
/usr/include/gsl/gsl_permute_matrix_complex_float.h
/usr/include/gsl/gsl_permute_matrix_complex_long_double.h
/usr/include/gsl/gsl_permute_matrix_double.h
/usr/include/gsl/gsl_permute_matrix_float.h
/usr/include/gsl/gsl_permute_matrix_int.h
/usr/include/gsl/gsl_permute_matrix_long.h
/usr/include/gsl/gsl_permute_matrix_long_double.h
/usr/include/gsl/gsl_permute_matrix_short.h
/usr/include/gsl/gsl_permute_matrix_uchar.h
/usr/include/gsl/gsl_permute_matrix_uint.h
/usr/include/gsl/gsl_permute_matrix_ulong.h
/usr/include/gsl/gsl_permute_matrix_ushort.h
/usr/include/gsl/gsl_permute_short.h
/usr/include/gsl/gsl_permute_uchar.h
/usr/include/gsl/gsl_permute_uint.h
/usr/include/gsl/gsl_permute_ulong.h
/usr/include/gsl/gsl_permute_ushort.h
/usr/include/gsl/gsl_permute_vector.h
/usr/include/gsl/gsl_permute_vector_char.h
/usr/include/gsl/gsl_permute_vector_complex_double.h
/usr/include/gsl/gsl_permute_vector_complex_float.h
/usr/include/gsl/gsl_permute_vector_complex_long_double.h
/usr/include/gsl/gsl_permute_vector_double.h
/usr/include/gsl/gsl_permute_vector_float.h
/usr/include/gsl/gsl_permute_vector_int.h
/usr/include/gsl/gsl_permute_vector_long.h
/usr/include/gsl/gsl_permute_vector_long_double.h
/usr/include/gsl/gsl_permute_vector_short.h
/usr/include/gsl/gsl_permute_vector_uchar.h
/usr/include/gsl/gsl_permute_vector_uint.h
/usr/include/gsl/gsl_permute_vector_ulong.h
/usr/include/gsl/gsl_permute_vector_ushort.h
/usr/include/gsl/gsl_poly.h
/usr/include/gsl/gsl_pow_int.h
/usr/include/gsl/gsl_precision.h
/usr/include/gsl/gsl_qrng.h
/usr/include/gsl/gsl_randist.h
/usr/include/gsl/gsl_rng.h
/usr/include/gsl/gsl_roots.h
/usr/include/gsl/gsl_rstat.h
/usr/include/gsl/gsl_sf.h
/usr/include/gsl/gsl_sf_airy.h
/usr/include/gsl/gsl_sf_bessel.h
/usr/include/gsl/gsl_sf_clausen.h
/usr/include/gsl/gsl_sf_coulomb.h
/usr/include/gsl/gsl_sf_coupling.h
/usr/include/gsl/gsl_sf_dawson.h
/usr/include/gsl/gsl_sf_debye.h
/usr/include/gsl/gsl_sf_dilog.h
/usr/include/gsl/gsl_sf_elementary.h
/usr/include/gsl/gsl_sf_ellint.h
/usr/include/gsl/gsl_sf_elljac.h
/usr/include/gsl/gsl_sf_erf.h
/usr/include/gsl/gsl_sf_exp.h
/usr/include/gsl/gsl_sf_expint.h
/usr/include/gsl/gsl_sf_fermi_dirac.h
/usr/include/gsl/gsl_sf_gamma.h
/usr/include/gsl/gsl_sf_gegenbauer.h
/usr/include/gsl/gsl_sf_hermite.h
/usr/include/gsl/gsl_sf_hyperg.h
/usr/include/gsl/gsl_sf_laguerre.h
/usr/include/gsl/gsl_sf_lambert.h
/usr/include/gsl/gsl_sf_legendre.h
/usr/include/gsl/gsl_sf_log.h
/usr/include/gsl/gsl_sf_mathieu.h
/usr/include/gsl/gsl_sf_pow_int.h
/usr/include/gsl/gsl_sf_psi.h
/usr/include/gsl/gsl_sf_result.h
/usr/include/gsl/gsl_sf_sincos_pi.h
/usr/include/gsl/gsl_sf_synchrotron.h
/usr/include/gsl/gsl_sf_transport.h
/usr/include/gsl/gsl_sf_trig.h
/usr/include/gsl/gsl_sf_zeta.h
/usr/include/gsl/gsl_siman.h
/usr/include/gsl/gsl_sort.h
/usr/include/gsl/gsl_sort_char.h
/usr/include/gsl/gsl_sort_double.h
/usr/include/gsl/gsl_sort_float.h
/usr/include/gsl/gsl_sort_int.h
/usr/include/gsl/gsl_sort_long.h
/usr/include/gsl/gsl_sort_long_double.h
/usr/include/gsl/gsl_sort_short.h
/usr/include/gsl/gsl_sort_uchar.h
/usr/include/gsl/gsl_sort_uint.h
/usr/include/gsl/gsl_sort_ulong.h
/usr/include/gsl/gsl_sort_ushort.h
/usr/include/gsl/gsl_sort_vector.h
/usr/include/gsl/gsl_sort_vector_char.h
/usr/include/gsl/gsl_sort_vector_double.h
/usr/include/gsl/gsl_sort_vector_float.h
/usr/include/gsl/gsl_sort_vector_int.h
/usr/include/gsl/gsl_sort_vector_long.h
/usr/include/gsl/gsl_sort_vector_long_double.h
/usr/include/gsl/gsl_sort_vector_short.h
/usr/include/gsl/gsl_sort_vector_uchar.h
/usr/include/gsl/gsl_sort_vector_uint.h
/usr/include/gsl/gsl_sort_vector_ulong.h
/usr/include/gsl/gsl_sort_vector_ushort.h
/usr/include/gsl/gsl_spblas.h
/usr/include/gsl/gsl_specfunc.h
/usr/include/gsl/gsl_splinalg.h
/usr/include/gsl/gsl_spline.h
/usr/include/gsl/gsl_spline2d.h
/usr/include/gsl/gsl_spmatrix.h
/usr/include/gsl/gsl_spmatrix_char.h
/usr/include/gsl/gsl_spmatrix_complex_double.h
/usr/include/gsl/gsl_spmatrix_complex_float.h
/usr/include/gsl/gsl_spmatrix_complex_long_double.h
/usr/include/gsl/gsl_spmatrix_double.h
/usr/include/gsl/gsl_spmatrix_float.h
/usr/include/gsl/gsl_spmatrix_int.h
/usr/include/gsl/gsl_spmatrix_long.h
/usr/include/gsl/gsl_spmatrix_long_double.h
/usr/include/gsl/gsl_spmatrix_short.h
/usr/include/gsl/gsl_spmatrix_uchar.h
/usr/include/gsl/gsl_spmatrix_uint.h
/usr/include/gsl/gsl_spmatrix_ulong.h
/usr/include/gsl/gsl_spmatrix_ushort.h
/usr/include/gsl/gsl_statistics.h
/usr/include/gsl/gsl_statistics_char.h
/usr/include/gsl/gsl_statistics_double.h
/usr/include/gsl/gsl_statistics_float.h
/usr/include/gsl/gsl_statistics_int.h
/usr/include/gsl/gsl_statistics_long.h
/usr/include/gsl/gsl_statistics_long_double.h
/usr/include/gsl/gsl_statistics_short.h
/usr/include/gsl/gsl_statistics_uchar.h
/usr/include/gsl/gsl_statistics_uint.h
/usr/include/gsl/gsl_statistics_ulong.h
/usr/include/gsl/gsl_statistics_ushort.h
/usr/include/gsl/gsl_sum.h
/usr/include/gsl/gsl_sys.h
/usr/include/gsl/gsl_test.h
/usr/include/gsl/gsl_types.h
/usr/include/gsl/gsl_vector.h
/usr/include/gsl/gsl_vector_char.h
/usr/include/gsl/gsl_vector_complex.h
/usr/include/gsl/gsl_vector_complex_double.h
/usr/include/gsl/gsl_vector_complex_float.h
/usr/include/gsl/gsl_vector_complex_long_double.h
/usr/include/gsl/gsl_vector_double.h
/usr/include/gsl/gsl_vector_float.h
/usr/include/gsl/gsl_vector_int.h
/usr/include/gsl/gsl_vector_long.h
/usr/include/gsl/gsl_vector_long_double.h
/usr/include/gsl/gsl_vector_short.h
/usr/include/gsl/gsl_vector_uchar.h
/usr/include/gsl/gsl_vector_uint.h
/usr/include/gsl/gsl_vector_ulong.h
/usr/include/gsl/gsl_vector_ushort.h
/usr/include/gsl/gsl_version.h
/usr/include/gsl/gsl_wavelet.h
/usr/include/gsl/gsl_wavelet2d.h
/usr/include/gsl/test_source.c
/usr/lib64/libgsl.so
/usr/lib64/libgslcblas.so
/usr/lib64/pkgconfig/gsl.pc
/usr/share/aclocal/*.m4
/usr/share/man/man3/gsl.3

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-gsl

%files info
%defattr(0644,root,root,0755)
/usr/share/info/gsl-ref.info

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgsl.so.25
/usr/lib64/libgsl.so.25.1.0
/usr/lib64/libgslcblas.so.0
/usr/lib64/libgslcblas.so.0.0.0
/usr/share/clear/optimized-elf/lib*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gsl/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gsl-config.1
/usr/share/man/man1/gsl-histogram.1
/usr/share/man/man1/gsl-randist.1
