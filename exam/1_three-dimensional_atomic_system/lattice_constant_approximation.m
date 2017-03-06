clear all
close
clc

epsilon= 0.0140 %eV
sigma  = 3.65   %A

U=@(r) 4*epsilon*((sigma/r)^12-(sigma/r)^6)


%% FCC
Efcc=@(a)6*U(a)+12*U(a/sqrt(2))
a_fcc=fminbnd(Efcc,0,10)
minEfcc=Efcc(a_fcc)


%% BCC
Ebcc=@(a)6*U(a)+8*U(a*sqrt(3)/2)
a_bcc=fminbnd(Ebcc,0,10)
minEbcc=Efcc(a_bcc)

%% primitive
Ep=@(a)6*U(a)
a_p=fminbnd(Ep,0,10)
minEp=Efcc(a_p)