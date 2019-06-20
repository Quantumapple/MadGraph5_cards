# This file was automatically created by FeynRules 2.4.46
# Mathematica version: 10.3.0 for Mac OS X x86 (64-bit) (October 9, 2015)
# Date: Fri 23 Sep 2016 19:38:42


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV7, L.VVV8 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_179_95,(0,0,1):C.R2GC_179_96,(0,1,0):C.R2GC_180_97,(0,1,1):C.R2GC_180_98,(0,2,0):C.R2GC_180_97,(0,2,1):C.R2GC_180_98,(0,3,0):C.R2GC_179_95,(0,3,1):C.R2GC_179_96,(0,4,0):C.R2GC_179_95,(0,4,1):C.R2GC_179_96,(0,5,0):C.R2GC_180_97,(0,5,1):C.R2GC_180_98})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_148_79,(2,0,1):C.R2GC_148_80,(0,0,0):C.R2GC_148_79,(0,0,1):C.R2GC_148_80,(4,0,0):C.R2GC_146_75,(4,0,1):C.R2GC_146_76,(3,0,0):C.R2GC_146_75,(3,0,1):C.R2GC_146_76,(8,0,0):C.R2GC_147_77,(8,0,1):C.R2GC_147_78,(7,0,0):C.R2GC_152_85,(7,0,1):C.R2GC_184_103,(6,0,0):C.R2GC_151_84,(6,0,1):C.R2GC_185_104,(5,0,0):C.R2GC_146_75,(5,0,1):C.R2GC_146_76,(1,0,0):C.R2GC_146_75,(1,0,1):C.R2GC_146_76,(11,0,0):C.R2GC_150_82,(11,0,1):C.R2GC_150_83,(10,0,0):C.R2GC_150_82,(10,0,1):C.R2GC_150_83,(9,0,1):C.R2GC_149_81,(2,1,0):C.R2GC_148_79,(2,1,1):C.R2GC_148_80,(0,1,0):C.R2GC_148_79,(0,1,1):C.R2GC_148_80,(6,1,0):C.R2GC_181_99,(6,1,1):C.R2GC_181_100,(4,1,0):C.R2GC_146_75,(4,1,1):C.R2GC_146_76,(3,1,0):C.R2GC_146_75,(3,1,1):C.R2GC_146_76,(8,1,0):C.R2GC_147_77,(8,1,1):C.R2GC_184_103,(7,1,0):C.R2GC_152_85,(7,1,1):C.R2GC_147_78,(5,1,0):C.R2GC_146_75,(5,1,1):C.R2GC_146_76,(1,1,0):C.R2GC_146_75,(1,1,1):C.R2GC_146_76,(11,1,0):C.R2GC_150_82,(11,1,1):C.R2GC_150_83,(10,1,0):C.R2GC_150_82,(10,1,1):C.R2GC_150_83,(9,1,1):C.R2GC_149_81,(2,2,0):C.R2GC_148_79,(2,2,1):C.R2GC_148_80,(0,2,0):C.R2GC_148_79,(0,2,1):C.R2GC_148_80,(4,2,0):C.R2GC_146_75,(4,2,1):C.R2GC_146_76,(3,2,0):C.R2GC_146_75,(3,2,1):C.R2GC_146_76,(8,2,0):C.R2GC_147_77,(8,2,1):C.R2GC_182_102,(6,2,0):C.R2GC_151_84,(7,2,0):C.R2GC_182_101,(7,2,1):C.R2GC_182_102,(5,2,0):C.R2GC_146_75,(5,2,1):C.R2GC_146_76,(1,2,0):C.R2GC_146_75,(1,2,1):C.R2GC_146_76,(11,2,0):C.R2GC_150_82,(11,2,1):C.R2GC_150_83,(10,2,0):C.R2GC_150_82,(10,2,1):C.R2GC_150_83,(9,2,1):C.R2GC_149_81})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_199_112,(0,1,0):C.R2GC_200_113})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_177_94})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_176_93})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.b__tilde__, P.t, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_201_114,(0,1,0):C.R2GC_198_111})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_202_115})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_203_116})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.Y1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV7, L.FFV8 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_170_89,(0,1,0):C.R2GC_172_91})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.d__tilde__, P.b, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.b, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_169_88,(0,1,0):C.R2GC_171_90})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_94_118,(0,1,0):C.R2GC_95_119})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.b__tilde__, P.d, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.b, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_169_88,(0,1,0):C.R2GC_171_90})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_100_1,(0,1,0):C.R2GC_101_2})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_106_7,(0,1,0):C.R2GC_107_8})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_191_106,(0,1,0):C.R2GC_193_108})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.u__tilde__, P.t, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.g, P.t, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_190_105,(0,1,0):C.R2GC_192_107})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.t__tilde__, P.u, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.g, P.t, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_190_105,(0,1,0):C.R2GC_192_107})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_113_10,(0,1,0):C.R2GC_114_11})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_110_9})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_110_9})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_110_9})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_105_6})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_105_6})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_105_6})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_154_86})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_154_86})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_154_86})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_154_86})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_154_86})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_154_86})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_164_87})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_164_87})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_164_87})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_164_87})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_164_87})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_164_87})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_134_66,(0,1,0):C.R2GC_115_12})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV11, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,1,0):C.R2GC_196_110,(0,0,0):C.R2GC_103_4})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV11, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_103_4,(0,1,0):C.R2GC_196_110})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV5 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_102_3,(0,1,0):C.R2GC_103_4})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV5 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_102_3,(0,1,0):C.R2GC_103_4})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_102_3,(0,1,0):C.R2GC_103_4})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_104_5})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_104_5})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_194_109,(0,1,0):C.R2GC_104_5})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_104_5})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_104_5})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_173_92,(0,1,0):C.R2GC_104_5})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV2, L.VV3, L.VV4 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.t] ] ],
                couplings = {(0,2,2):C.R2GC_91_117,(0,0,0):C.R2GC_116_13,(0,0,3):C.R2GC_116_14,(0,1,1):C.R2GC_119_19})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.g, P.g, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVV2 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_122_24,(0,0,1):C.R2GC_122_25,(0,0,2):C.R2GC_122_26,(0,0,3):C.R2GC_122_27,(0,0,4):C.R2GC_122_28,(0,0,5):C.R2GC_122_29})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.g, P.g, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVV1 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_126_48,(0,0,1):C.R2GC_126_49})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.g, P.g, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_117_15,(0,0,1):C.R2GC_117_16})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.g, P.g, P.Y1, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV7 ],
                loop_particles = [ [ [P.b] ], [ [P.b, P.d] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.t, P.u] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_135_67,(0,0,2):C.R2GC_135_68,(0,0,3):C.R2GC_135_69,(0,0,4):C.R2GC_135_70,(0,0,5):C.R2GC_135_71,(0,0,7):C.R2GC_135_72,(0,0,1):C.R2GC_135_73,(0,0,6):C.R2GC_135_74})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Y1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV7 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_124_36,(0,0,1):C.R2GC_124_37,(0,0,2):C.R2GC_124_38,(0,0,3):C.R2GC_124_39,(0,0,4):C.R2GC_124_40,(0,0,5):C.R2GC_124_41})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.g, P.g, P.Y1, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV7 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_130_56,(0,0,1):C.R2GC_130_57,(0,0,2):C.R2GC_130_58,(0,0,3):C.R2GC_130_59,(0,0,4):C.R2GC_130_60,(0,0,5):C.R2GC_130_61})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Y1 ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV7 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_123_30,(1,0,1):C.R2GC_123_31,(1,0,2):C.R2GC_123_32,(1,0,3):C.R2GC_123_33,(1,0,4):C.R2GC_123_34,(1,0,5):C.R2GC_123_35,(0,1,0):C.R2GC_125_42,(0,1,1):C.R2GC_125_43,(0,1,2):C.R2GC_125_44,(0,1,3):C.R2GC_125_45,(0,1,4):C.R2GC_125_46,(0,1,5):C.R2GC_125_47})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV7 ],
                loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_133_65})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV7 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_127_50,(0,0,1):C.R2GC_127_51})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV7 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_131_62,(0,0,1):C.R2GC_131_63})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV7 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_120_20,(0,0,1):C.R2GC_120_21})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV7 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_129_54,(1,0,1):C.R2GC_129_55,(0,1,0):C.R2GC_128_52,(0,1,1):C.R2GC_128_53})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV7 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_121_22,(0,0,1):C.R2GC_121_23})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.g, P.g, P.H, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_118_17,(0,0,1):C.R2GC_118_18})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_118_17,(0,0,1):C.R2GC_118_18})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_132_64})

V_66 = CTVertex(name = 'V_66',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV7, L.VVV8 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_179_42,(0,0,1):C.UVGC_179_43,(0,0,2):C.UVGC_179_44,(0,0,3):C.UVGC_179_45,(0,0,4):C.UVGC_179_46,(0,1,0):C.UVGC_180_47,(0,1,1):C.UVGC_180_48,(0,1,2):C.UVGC_180_49,(0,1,3):C.UVGC_180_50,(0,1,4):C.UVGC_180_51,(0,2,0):C.UVGC_180_47,(0,2,1):C.UVGC_180_48,(0,2,2):C.UVGC_180_49,(0,2,3):C.UVGC_180_50,(0,2,4):C.UVGC_180_51,(0,3,0):C.UVGC_179_42,(0,3,1):C.UVGC_179_43,(0,3,2):C.UVGC_179_44,(0,3,3):C.UVGC_179_45,(0,3,4):C.UVGC_179_46,(0,4,0):C.UVGC_179_42,(0,4,1):C.UVGC_179_43,(0,4,2):C.UVGC_179_44,(0,4,3):C.UVGC_179_45,(0,4,4):C.UVGC_179_46,(0,5,0):C.UVGC_180_47,(0,5,1):C.UVGC_180_48,(0,5,2):C.UVGC_180_49,(0,5,3):C.UVGC_180_50,(0,5,4):C.UVGC_180_51})

V_67 = CTVertex(name = 'V_67',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(2,0,3):C.UVGC_147_9,(2,0,4):C.UVGC_147_8,(0,0,3):C.UVGC_147_9,(0,0,4):C.UVGC_147_8,(4,0,3):C.UVGC_146_6,(4,0,4):C.UVGC_146_7,(3,0,3):C.UVGC_146_6,(3,0,4):C.UVGC_146_7,(8,0,3):C.UVGC_147_8,(8,0,4):C.UVGC_147_9,(7,0,0):C.UVGC_184_62,(7,0,2):C.UVGC_184_63,(7,0,3):C.UVGC_184_64,(7,0,4):C.UVGC_184_65,(7,0,5):C.UVGC_184_66,(6,0,0):C.UVGC_184_62,(6,0,2):C.UVGC_184_63,(6,0,3):C.UVGC_185_67,(6,0,4):C.UVGC_185_68,(6,0,5):C.UVGC_184_66,(5,0,3):C.UVGC_146_6,(5,0,4):C.UVGC_146_7,(1,0,3):C.UVGC_146_6,(1,0,4):C.UVGC_146_7,(11,0,3):C.UVGC_150_12,(11,0,4):C.UVGC_150_13,(10,0,3):C.UVGC_150_12,(10,0,4):C.UVGC_150_13,(9,0,3):C.UVGC_149_10,(9,0,4):C.UVGC_149_11,(2,1,3):C.UVGC_147_9,(2,1,4):C.UVGC_147_8,(0,1,3):C.UVGC_147_9,(0,1,4):C.UVGC_147_8,(6,1,0):C.UVGC_181_52,(6,1,3):C.UVGC_181_53,(6,1,4):C.UVGC_181_54,(6,1,5):C.UVGC_181_55,(4,1,3):C.UVGC_146_6,(4,1,4):C.UVGC_146_7,(3,1,3):C.UVGC_146_6,(3,1,4):C.UVGC_146_7,(8,1,0):C.UVGC_186_69,(8,1,2):C.UVGC_186_70,(8,1,3):C.UVGC_184_64,(8,1,4):C.UVGC_186_71,(8,1,5):C.UVGC_186_72,(7,1,1):C.UVGC_151_14,(7,1,3):C.UVGC_147_8,(7,1,4):C.UVGC_152_15,(5,1,3):C.UVGC_146_6,(5,1,4):C.UVGC_146_7,(1,1,3):C.UVGC_146_6,(1,1,4):C.UVGC_146_7,(11,1,3):C.UVGC_150_12,(11,1,4):C.UVGC_150_13,(10,1,3):C.UVGC_150_12,(10,1,4):C.UVGC_150_13,(9,1,3):C.UVGC_149_10,(9,1,4):C.UVGC_149_11,(2,2,3):C.UVGC_147_9,(2,2,4):C.UVGC_147_8,(0,2,3):C.UVGC_147_9,(0,2,4):C.UVGC_147_8,(4,2,3):C.UVGC_146_6,(4,2,4):C.UVGC_146_7,(3,2,3):C.UVGC_146_6,(3,2,4):C.UVGC_146_7,(8,2,0):C.UVGC_183_58,(8,2,2):C.UVGC_183_59,(8,2,3):C.UVGC_182_56,(8,2,4):C.UVGC_183_60,(8,2,5):C.UVGC_183_61,(6,2,1):C.UVGC_151_14,(6,2,4):C.UVGC_149_10,(7,2,0):C.UVGC_181_52,(7,2,3):C.UVGC_182_56,(7,2,4):C.UVGC_182_57,(7,2,5):C.UVGC_181_55,(5,2,3):C.UVGC_146_6,(5,2,4):C.UVGC_146_7,(1,2,3):C.UVGC_146_6,(1,2,4):C.UVGC_146_7,(11,2,3):C.UVGC_150_12,(11,2,4):C.UVGC_150_13,(10,2,3):C.UVGC_150_12,(10,2,4):C.UVGC_150_13,(9,2,3):C.UVGC_149_10,(9,2,4):C.UVGC_149_11})

V_68 = CTVertex(name = 'V_68',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_199_92,(0,0,2):C.UVGC_199_93,(0,0,1):C.UVGC_199_94,(0,1,0):C.UVGC_200_95,(0,1,2):C.UVGC_200_96,(0,1,1):C.UVGC_200_97})

V_69 = CTVertex(name = 'V_69',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_177_39})

V_70 = CTVertex(name = 'V_70',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_176_38})

V_71 = CTVertex(name = 'V_71',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_201_98,(0,0,2):C.UVGC_201_99,(0,0,1):C.UVGC_201_100,(0,1,0):C.UVGC_198_89,(0,1,2):C.UVGC_198_90,(0,1,1):C.UVGC_198_91})

V_72 = CTVertex(name = 'V_72',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_202_101})

V_73 = CTVertex(name = 'V_73',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_203_102})

V_74 = CTVertex(name = 'V_74',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_170_30,(0,1,0):C.UVGC_172_34})

V_75 = CTVertex(name = 'V_75',
                type = 'UV',
                particles = [ P.d__tilde__, P.b, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.b, P.d, P.g] ], [ [P.b, P.g] ], [ [P.d, P.g] ] ],
                couplings = {(0,0,1):C.UVGC_169_27,(0,0,2):C.UVGC_169_28,(0,0,0):C.UVGC_169_29,(0,1,1):C.UVGC_171_31,(0,1,2):C.UVGC_171_32,(0,1,0):C.UVGC_171_33})

V_76 = CTVertex(name = 'V_76',
                type = 'UV',
                particles = [ P.b__tilde__, P.d, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.b, P.d, P.g] ], [ [P.b, P.g] ], [ [P.d, P.g] ] ],
                couplings = {(0,0,1):C.UVGC_169_27,(0,0,2):C.UVGC_169_28,(0,0,0):C.UVGC_169_29,(0,1,1):C.UVGC_171_31,(0,1,2):C.UVGC_171_32,(0,1,0):C.UVGC_171_33})

V_77 = CTVertex(name = 'V_77',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_191_79,(0,1,0):C.UVGC_193_83})

V_78 = CTVertex(name = 'V_78',
                type = 'UV',
                particles = [ P.u__tilde__, P.t, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.u] ], [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_190_76,(0,0,2):C.UVGC_190_77,(0,0,1):C.UVGC_190_78,(0,1,0):C.UVGC_192_80,(0,1,2):C.UVGC_192_81,(0,1,1):C.UVGC_192_82})

V_79 = CTVertex(name = 'V_79',
                type = 'UV',
                particles = [ P.t__tilde__, P.u, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV7, L.FFV8 ],
                loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.u] ], [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_190_76,(0,0,2):C.UVGC_190_77,(0,0,1):C.UVGC_190_78,(0,1,0):C.UVGC_192_80,(0,1,2):C.UVGC_192_81,(0,1,1):C.UVGC_192_82})

V_80 = CTVertex(name = 'V_80',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV6 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_137_2})

V_81 = CTVertex(name = 'V_81',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV6 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_137_2})

V_82 = CTVertex(name = 'V_82',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV10, L.FFV8 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_137_2,(0,1,0):C.UVGC_188_74})

V_83 = CTVertex(name = 'V_83',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV6 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_139_3})

V_84 = CTVertex(name = 'V_84',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV6 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_139_3})

V_85 = CTVertex(name = 'V_85',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_139_3,(0,1,0):C.UVGC_167_25,(0,2,0):C.UVGC_167_25})

V_86 = CTVertex(name = 'V_86',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ] ],
                couplings = {(0,0,4):C.UVGC_154_16,(0,1,0):C.UVGC_155_17,(0,1,1):C.UVGC_155_18,(0,1,2):C.UVGC_155_19,(0,1,3):C.UVGC_155_20,(0,1,4):C.UVGC_155_21,(0,2,0):C.UVGC_155_17,(0,2,1):C.UVGC_155_18,(0,2,2):C.UVGC_155_19,(0,2,3):C.UVGC_155_20,(0,2,4):C.UVGC_155_21})

V_87 = CTVertex(name = 'V_87',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ] ],
                couplings = {(0,0,2):C.UVGC_154_16,(0,1,0):C.UVGC_155_17,(0,1,1):C.UVGC_155_18,(0,1,3):C.UVGC_155_19,(0,1,4):C.UVGC_155_20,(0,1,2):C.UVGC_155_21,(0,2,0):C.UVGC_155_17,(0,2,1):C.UVGC_155_18,(0,2,3):C.UVGC_155_19,(0,2,4):C.UVGC_155_20,(0,2,2):C.UVGC_155_21})

V_88 = CTVertex(name = 'V_88',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,4):C.UVGC_154_16,(0,1,0):C.UVGC_155_17,(0,1,1):C.UVGC_155_18,(0,1,2):C.UVGC_155_19,(0,1,3):C.UVGC_155_20,(0,1,4):C.UVGC_189_75,(0,2,0):C.UVGC_155_17,(0,2,1):C.UVGC_155_18,(0,2,2):C.UVGC_155_19,(0,2,3):C.UVGC_155_20,(0,2,4):C.UVGC_189_75})

V_89 = CTVertex(name = 'V_89',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ] ],
                couplings = {(0,0,2):C.UVGC_154_16,(0,1,0):C.UVGC_155_17,(0,1,1):C.UVGC_155_18,(0,1,3):C.UVGC_155_19,(0,1,4):C.UVGC_155_20,(0,1,2):C.UVGC_155_21,(0,2,0):C.UVGC_155_17,(0,2,1):C.UVGC_155_18,(0,2,3):C.UVGC_155_19,(0,2,4):C.UVGC_155_20,(0,2,2):C.UVGC_155_21})

V_90 = CTVertex(name = 'V_90',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ] ],
                couplings = {(0,0,4):C.UVGC_154_16,(0,1,0):C.UVGC_155_17,(0,1,1):C.UVGC_155_18,(0,1,2):C.UVGC_155_19,(0,1,3):C.UVGC_155_20,(0,1,4):C.UVGC_155_21,(0,2,0):C.UVGC_155_17,(0,2,1):C.UVGC_155_18,(0,2,2):C.UVGC_155_19,(0,2,3):C.UVGC_155_20,(0,2,4):C.UVGC_155_21})

V_91 = CTVertex(name = 'V_91',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ] ],
                couplings = {(0,0,1):C.UVGC_154_16,(0,1,0):C.UVGC_155_17,(0,1,2):C.UVGC_155_18,(0,1,3):C.UVGC_155_19,(0,1,4):C.UVGC_155_20,(0,1,1):C.UVGC_168_26,(0,2,0):C.UVGC_155_17,(0,2,2):C.UVGC_155_18,(0,2,3):C.UVGC_155_19,(0,2,4):C.UVGC_155_20,(0,2,1):C.UVGC_168_26})

V_92 = CTVertex(name = 'V_92',
                type = 'UV',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_164_22,(0,0,1):C.UVGC_164_23})

V_93 = CTVertex(name = 'V_93',
                type = 'UV',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_164_22,(0,0,1):C.UVGC_164_23})

V_94 = CTVertex(name = 'V_94',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_195_85,(0,0,2):C.UVGC_195_86,(0,0,1):C.UVGC_164_23})

V_95 = CTVertex(name = 'V_95',
                type = 'UV',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_164_22,(0,0,1):C.UVGC_164_23})

V_96 = CTVertex(name = 'V_96',
                type = 'UV',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_164_22,(0,0,1):C.UVGC_164_23})

V_97 = CTVertex(name = 'V_97',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_195_85,(0,0,2):C.UVGC_195_86,(0,0,1):C.UVGC_164_23})

V_98 = CTVertex(name = 'V_98',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV11, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_197_88,(0,1,0):C.UVGC_196_87})

V_99 = CTVertex(name = 'V_99',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_174_36,(0,1,0):C.UVGC_175_37})

V_100 = CTVertex(name = 'V_100',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_136_1})

V_101 = CTVertex(name = 'V_101',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_136_1})

V_102 = CTVertex(name = 'V_102',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_194_84,(0,1,0):C.UVGC_187_73})

V_103 = CTVertex(name = 'V_103',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_136_1})

V_104 = CTVertex(name = 'V_104',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_136_1})

V_105 = CTVertex(name = 'V_105',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_173_35,(0,1,0):C.UVGC_166_24})

V_106 = CTVertex(name = 'V_106',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                 couplings = {(0,1,0):C.UVGC_178_40,(0,1,3):C.UVGC_178_41,(0,0,1):C.UVGC_145_4,(0,0,2):C.UVGC_145_5})

