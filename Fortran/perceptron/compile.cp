#!/bin/sh

gfortran -O3 ext_module.f90 iris.f90 -o iris
gfortran -O3 ext_module.f90 pima.f90 -o pima

