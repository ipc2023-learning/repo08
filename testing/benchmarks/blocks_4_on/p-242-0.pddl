

(define (problem BW-rand-242)
(:domain blocksworld)
(:objects b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 b16 b17 b18 b19 b20 b21 b22 b23 b24 b25 b26 b27 b28 b29 b30 b31 b32 b33 b34 b35 b36 b37 b38 b39 b40 b41 b42 b43 b44 b45 b46 b47 b48 b49 b50 b51 b52 b53 b54 b55 b56 b57 b58 b59 b60 b61 b62 b63 b64 b65 b66 b67 b68 b69 b70 b71 b72 b73 b74 b75 b76 b77 b78 b79 b80 b81 b82 b83 b84 b85 b86 b87 b88 b89 b90 b91 b92 b93 b94 b95 b96 b97 b98 b99 b100 b101 b102 b103 b104 b105 b106 b107 b108 b109 b110 b111 b112 b113 b114 b115 b116 b117 b118 b119 b120 b121 b122 b123 b124 b125 b126 b127 b128 b129 b130 b131 b132 b133 b134 b135 b136 b137 b138 b139 b140 b141 b142 b143 b144 b145 b146 b147 b148 b149 b150 b151 b152 b153 b154 b155 b156 b157 b158 b159 b160 b161 b162 b163 b164 b165 b166 b167 b168 b169 b170 b171 b172 b173 b174 b175 b176 b177 b178 b179 b180 b181 b182 b183 b184 b185 b186 b187 b188 b189 b190 b191 b192 b193 b194 b195 b196 b197 b198 b199 b200 b201 b202 b203 b204 b205 b206 b207 b208 b209 b210 b211 b212 b213 b214 b215 b216 b217 b218 b219 b220 b221 b222 b223 b224 b225 b226 b227 b228 b229 b230 b231 b232 b233 b234 b235 b236 b237 b238 b239 b240 b241 b242 )
(:init
(arm-empty)
(on-table b1)
(on b2 b32)
(on b3 b232)
(on b4 b67)
(on b5 b181)
(on b6 b42)
(on b7 b80)
(on b8 b219)
(on b9 b98)
(on b10 b39)
(on b11 b24)
(on b12 b44)
(on b13 b127)
(on b14 b138)
(on b15 b174)
(on b16 b170)
(on b17 b29)
(on b18 b84)
(on b19 b63)
(on b20 b3)
(on b21 b227)
(on b22 b111)
(on b23 b27)
(on b24 b15)
(on b25 b188)
(on b26 b149)
(on b27 b33)
(on b28 b48)
(on-table b29)
(on b30 b43)
(on b31 b229)
(on b32 b45)
(on b33 b64)
(on b34 b90)
(on b35 b165)
(on b36 b104)
(on b37 b95)
(on b38 b233)
(on b39 b112)
(on b40 b205)
(on b41 b166)
(on b42 b210)
(on b43 b93)
(on-table b44)
(on b45 b106)
(on b46 b179)
(on b47 b25)
(on b48 b5)
(on b49 b198)
(on b50 b134)
(on b51 b203)
(on b52 b208)
(on b53 b147)
(on b54 b231)
(on b55 b53)
(on b56 b144)
(on b57 b81)
(on b58 b223)
(on b59 b136)
(on b60 b89)
(on b61 b91)
(on b62 b142)
(on b63 b28)
(on b64 b162)
(on b65 b110)
(on b66 b121)
(on b67 b200)
(on b68 b172)
(on b69 b236)
(on b70 b202)
(on b71 b137)
(on b72 b125)
(on b73 b72)
(on b74 b191)
(on b75 b197)
(on b76 b86)
(on b77 b61)
(on b78 b74)
(on b79 b19)
(on b80 b201)
(on b81 b99)
(on b82 b148)
(on b83 b101)
(on b84 b55)
(on b85 b8)
(on b86 b242)
(on b87 b22)
(on b88 b35)
(on b89 b105)
(on b90 b154)
(on-table b91)
(on b92 b47)
(on b93 b218)
(on b94 b196)
(on b95 b57)
(on b96 b185)
(on b97 b51)
(on b98 b190)
(on b99 b241)
(on b100 b182)
(on b101 b131)
(on b102 b76)
(on b103 b96)
(on b104 b176)
(on b105 b195)
(on b106 b124)
(on b107 b115)
(on b108 b38)
(on b109 b52)
(on b110 b75)
(on b111 b156)
(on b112 b238)
(on b113 b126)
(on b114 b36)
(on-table b115)
(on b116 b161)
(on b117 b214)
(on b118 b117)
(on b119 b40)
(on b120 b159)
(on b121 b213)
(on b122 b194)
(on b123 b221)
(on b124 b211)
(on b125 b56)
(on b126 b145)
(on b127 b193)
(on b128 b143)
(on b129 b60)
(on b130 b77)
(on b131 b21)
(on b132 b207)
(on b133 b169)
(on b134 b94)
(on b135 b87)
(on b136 b34)
(on b137 b62)
(on b138 b225)
(on b139 b68)
(on b140 b2)
(on b141 b152)
(on b142 b30)
(on b143 b178)
(on b144 b118)
(on b145 b222)
(on b146 b100)
(on b147 b109)
(on b148 b141)
(on b149 b164)
(on b150 b1)
(on b151 b54)
(on b152 b31)
(on b153 b103)
(on b154 b129)
(on b155 b10)
(on-table b156)
(on b157 b123)
(on b158 b23)
(on b159 b209)
(on b160 b46)
(on b161 b155)
(on b162 b186)
(on b163 b122)
(on b164 b14)
(on b165 b116)
(on b166 b168)
(on b167 b59)
(on b168 b157)
(on b169 b17)
(on b170 b58)
(on b171 b183)
(on b172 b153)
(on-table b173)
(on-table b174)
(on-table b175)
(on-table b176)
(on b177 b239)
(on b178 b66)
(on b179 b128)
(on b180 b97)
(on b181 b135)
(on b182 b226)
(on b183 b206)
(on b184 b158)
(on b185 b177)
(on b186 b146)
(on b187 b37)
(on b188 b235)
(on b189 b151)
(on b190 b65)
(on b191 b71)
(on b192 b49)
(on b193 b220)
(on b194 b85)
(on b195 b79)
(on b196 b204)
(on b197 b4)
(on b198 b18)
(on b199 b102)
(on b200 b113)
(on b201 b70)
(on b202 b189)
(on b203 b88)
(on b204 b140)
(on b205 b173)
(on-table b206)
(on b207 b119)
(on b208 b83)
(on b209 b92)
(on b210 b13)
(on b211 b108)
(on b212 b82)
(on b213 b133)
(on b214 b132)
(on b215 b50)
(on b216 b237)
(on b217 b114)
(on b218 b73)
(on b219 b107)
(on b220 b230)
(on b221 b217)
(on b222 b12)
(on b223 b171)
(on b224 b139)
(on b225 b150)
(on b226 b224)
(on b227 b130)
(on b228 b41)
(on b229 b240)
(on b230 b167)
(on b231 b9)
(on b232 b228)
(on b233 b11)
(on b234 b16)
(on b235 b216)
(on b236 b78)
(on b237 b7)
(on b238 b215)
(on b239 b175)
(on b240 b184)
(on-table b241)
(on b242 b20)
(clear b6)
(clear b26)
(clear b69)
(clear b120)
(clear b160)
(clear b163)
(clear b180)
(clear b187)
(clear b192)
(clear b199)
(clear b212)
(clear b234)
)
(:goal
(and
(on b1 b2))
)
)


