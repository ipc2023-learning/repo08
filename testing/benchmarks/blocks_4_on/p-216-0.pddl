

(define (problem BW-rand-216)
(:domain blocksworld)
(:objects b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 b16 b17 b18 b19 b20 b21 b22 b23 b24 b25 b26 b27 b28 b29 b30 b31 b32 b33 b34 b35 b36 b37 b38 b39 b40 b41 b42 b43 b44 b45 b46 b47 b48 b49 b50 b51 b52 b53 b54 b55 b56 b57 b58 b59 b60 b61 b62 b63 b64 b65 b66 b67 b68 b69 b70 b71 b72 b73 b74 b75 b76 b77 b78 b79 b80 b81 b82 b83 b84 b85 b86 b87 b88 b89 b90 b91 b92 b93 b94 b95 b96 b97 b98 b99 b100 b101 b102 b103 b104 b105 b106 b107 b108 b109 b110 b111 b112 b113 b114 b115 b116 b117 b118 b119 b120 b121 b122 b123 b124 b125 b126 b127 b128 b129 b130 b131 b132 b133 b134 b135 b136 b137 b138 b139 b140 b141 b142 b143 b144 b145 b146 b147 b148 b149 b150 b151 b152 b153 b154 b155 b156 b157 b158 b159 b160 b161 b162 b163 b164 b165 b166 b167 b168 b169 b170 b171 b172 b173 b174 b175 b176 b177 b178 b179 b180 b181 b182 b183 b184 b185 b186 b187 b188 b189 b190 b191 b192 b193 b194 b195 b196 b197 b198 b199 b200 b201 b202 b203 b204 b205 b206 b207 b208 b209 b210 b211 b212 b213 b214 b215 b216 )
(:init
(arm-empty)
(on b1 b174)
(on-table b2)
(on b3 b141)
(on b4 b176)
(on b5 b68)
(on b6 b3)
(on b7 b42)
(on b8 b140)
(on b9 b110)
(on b10 b60)
(on b11 b86)
(on b12 b80)
(on b13 b38)
(on b14 b21)
(on b15 b191)
(on b16 b132)
(on b17 b26)
(on b18 b189)
(on b19 b52)
(on b20 b122)
(on b21 b30)
(on b22 b31)
(on b23 b37)
(on-table b24)
(on b25 b103)
(on b26 b116)
(on b27 b164)
(on b28 b183)
(on b29 b87)
(on b30 b109)
(on b31 b167)
(on b32 b64)
(on b33 b51)
(on b34 b33)
(on b35 b28)
(on-table b36)
(on b37 b214)
(on b38 b56)
(on b39 b93)
(on b40 b145)
(on-table b41)
(on b42 b115)
(on b43 b46)
(on b44 b6)
(on b45 b150)
(on-table b46)
(on b47 b165)
(on b48 b185)
(on b49 b182)
(on b50 b127)
(on b51 b48)
(on b52 b43)
(on b53 b160)
(on b54 b114)
(on b55 b152)
(on b56 b121)
(on-table b57)
(on b58 b75)
(on b59 b32)
(on b60 b210)
(on b61 b212)
(on b62 b195)
(on b63 b89)
(on b64 b192)
(on b65 b216)
(on b66 b142)
(on b67 b178)
(on b68 b179)
(on b69 b162)
(on b70 b129)
(on b71 b215)
(on b72 b13)
(on b73 b108)
(on b74 b69)
(on b75 b198)
(on-table b76)
(on b77 b131)
(on b78 b128)
(on b79 b50)
(on b80 b155)
(on b81 b144)
(on b82 b124)
(on b83 b206)
(on b84 b147)
(on b85 b136)
(on b86 b135)
(on b87 b17)
(on b88 b72)
(on b89 b12)
(on b90 b161)
(on b91 b190)
(on-table b92)
(on b93 b49)
(on b94 b181)
(on b95 b203)
(on b96 b184)
(on b97 b104)
(on b98 b79)
(on b99 b96)
(on b100 b36)
(on b101 b16)
(on b102 b213)
(on b103 b1)
(on b104 b40)
(on b105 b88)
(on-table b106)
(on b107 b201)
(on b108 b130)
(on b109 b105)
(on b110 b194)
(on b111 b180)
(on b112 b111)
(on b113 b2)
(on b114 b120)
(on b115 b100)
(on b116 b76)
(on b117 b154)
(on b118 b45)
(on b119 b59)
(on b120 b207)
(on b121 b18)
(on b122 b81)
(on b123 b204)
(on b124 b102)
(on b125 b55)
(on b126 b202)
(on b127 b163)
(on b128 b205)
(on b129 b137)
(on b130 b66)
(on b131 b65)
(on b132 b83)
(on b133 b107)
(on b134 b98)
(on b135 b149)
(on b136 b90)
(on b137 b133)
(on b138 b99)
(on b139 b158)
(on b140 b74)
(on b141 b92)
(on b142 b39)
(on b143 b95)
(on b144 b8)
(on b145 b11)
(on b146 b112)
(on b147 b24)
(on b148 b101)
(on b149 b5)
(on b150 b44)
(on-table b151)
(on b152 b22)
(on b153 b169)
(on b154 b85)
(on b155 b123)
(on b156 b19)
(on-table b157)
(on b158 b148)
(on b159 b118)
(on b160 b57)
(on b161 b82)
(on b162 b138)
(on b163 b7)
(on b164 b25)
(on b165 b157)
(on b166 b151)
(on b167 b126)
(on b168 b208)
(on b169 b63)
(on b170 b171)
(on b171 b193)
(on b172 b47)
(on b173 b117)
(on b174 b106)
(on b175 b139)
(on b176 b73)
(on-table b177)
(on b178 b159)
(on b179 b78)
(on b180 b125)
(on b181 b188)
(on b182 b199)
(on b183 b71)
(on b184 b187)
(on b185 b172)
(on b186 b177)
(on b187 b35)
(on b188 b53)
(on b189 b77)
(on b190 b119)
(on b191 b9)
(on b192 b27)
(on b193 b156)
(on b194 b10)
(on b195 b153)
(on b196 b97)
(on b197 b168)
(on b198 b62)
(on b199 b186)
(on b200 b84)
(on-table b201)
(on b202 b91)
(on b203 b211)
(on b204 b146)
(on b205 b67)
(on-table b206)
(on b207 b4)
(on b208 b113)
(on b209 b166)
(on b210 b41)
(on-table b211)
(on b212 b20)
(on b213 b54)
(on b214 b94)
(on b215 b29)
(on b216 b143)
(clear b14)
(clear b15)
(clear b23)
(clear b34)
(clear b58)
(clear b61)
(clear b70)
(clear b134)
(clear b170)
(clear b173)
(clear b175)
(clear b196)
(clear b197)
(clear b200)
(clear b209)
)
(:goal
(and
(on b1 b2))
)
)


