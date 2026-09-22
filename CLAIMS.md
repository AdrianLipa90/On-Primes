# Claim Ledger

Status vocabulary: `PROVED`, `STANDARD`, `NUMERICAL`, `CONJECTURE`, `OPEN`.

| ID | Statement | Status | Notes |
|---|---|---|---|
| OP-D001 | Every integer \(n\ge1\) has a unique representation \(n+1=a2^k\) with odd \(a\ge1\) and \(k=v_2(n+1)\ge0\). | PROVED | Immediate from the 2-adic factorisation of \(n+1\). |
| OP-D002 | For \(x_{a,k}=a2^k-1\), \(T(x)=2x+1\) satisfies \(T(x_{a,k})=x_{a,k+1}\). | PROVED | Algebraic identity. |
| OP-D003 | The only prime on the integer boundary \(k=0\) is \(2\), corresponding to \(a=3\). | PROVED | \(a-1\) is even for odd \(a\); the only even prime is 2. |
| OP-D004 | If \(x\in\tfrac12+\mathbb Z_{\ge0}\), then \(T(x)\) is prime iff \(x=\tfrac12\). | PROVED | \(T(n+1/2)=2n+2\) is even. |
| OP-D005 | \(\log(x_{a,k}+1)=\log a+k\log2\). | PROVED | Exact logarithmic lattice identity. |
| OP-D006 | For prime \(p\), \(\log p=\log(p+1)-\log(1+1/p)\), with positive defect \(\delta_p=\log(1+1/p)\). | PROVED | Exact identity; \(\delta_p>0\). |
| OP-D007 | Let \(r\) be an odd prime with \(r\nmid a\). If \(a2^{k_0}\equiv1\pmod r\), then \(r\mid(a2^k-1)\) iff \(k\equiv k_0\pmod{\operatorname{ord}_r(2)}\). | PROVED | Modular obstruction classes are exact arithmetic progressions in fibre index. |
| OP-D008 | For a finite set `R` of odd prime divisors, the union of all fibre obstruction classes is periodic modulo `L = lcm(ord_r(2): r in R)`. | PROVED | Finite union of congruence classes; no independence assumption. |
| OP-D009 | The finite-sieve survivor set has exact density `|S_R(a)| / L`. | PROVED | Exact count of survivor residues in one complete period. |
| OP-D010 | If a finite divisor set covers every exponent residue and there are no equality exceptions `a*2^k-1=r` in the claimed exponent range, then every sequence value in that range is composite. | PROVED | Direct covering-set corollary; implemented by `covering_certificate`. |
| OP-D011 | For `Re(s)>1`, `-zeta'(s)/zeta(s)` equals the absolutely convergent sum of fibre contributions `log(p)/(p^s-1)` over the unique dyadic addresses of primes. | PROVED | Exact reindexing of the classical Euler-product logarithmic derivative. |
| OP-D012 | The unique `k=0` contribution to the prime-side fibre decomposition is `log(2)/(2^s-1)`. | PROVED | Follows from the unique even prime on the dyadic boundary. |
| OP-D013 | `log p = log a_p + v2(p+1) log 2 - log(1+1/p)` for the unique address `p+1=a_p 2^{v2(p+1)}`. | PROVED | Exact three-term prime-log decomposition. |
| OP-D014 | `v2(p+1)=sum_{j>=1} 1_{p == -1 mod 2^j}` and therefore the dyadic moment is a nested residue-class tower for `Re(s)>1`. | PROVED | Exact valuation identity plus absolute convergence. |
| OP-D015 | For each `j>=1` and `Re(s)>1`, the tower level over primes `p == -1 mod 2^j` equals the Dirichlet-character orthogonality average of the character-prime sums modulo `2^j`. | PROVED | Exact character decomposition; finite character group and absolutely convergent prime sums. |
| OP-D016 | For `Re(s)>1`, `Pi_chi(s)=sum_{m>=1} P_chi(ms)` and `P_chi(s)=sum_{r>=1} mu(r)/r * log L(rs,chi^r)` in the Euler-product half-plane. | STANDARD | Generalized prime-zeta / Dirichlet-L Möbius inversion identity; branch inherited from the Euler product. |
| OP-S004 | The ordinary prime zeta function has the Möbius-log representation through `log zeta(ks)` and its continuation develops singularities inherited from zeta zeros/poles; the line `Re(s)=0` is a natural-boundary obstruction. | STANDARD | Prior-art anchor; see `PRIOR_ART.md`. |
| OP-D017 | The finite prime-power triangular memory admits the exact decomposition `M=(log 2) M_K + M_A - M_D` for every finite log-time `t`. | PROVED | Finite sum; no analytic continuation is used. |
| OP-D018 | The memory components `M_K`, `M_A`, `M_D` are nonnegative, `0<delta_p<1/p`, and for odd primes `k_p log 2 - delta_p >= log(3/2)`. | PROVED | Eventwise inequalities with nonnegative triangular kernel. |
| OP-D019 | For every odd prime `p`, `v2(p+1)=k` iff `p == 2^k-1 (mod 2^(k+1))`; hence the odd primes partition into exact dyadic shells. | PROVED | Exact congruence identity. |
| OP-N001 | At cutoff `X=10^6`, the prime-power memory shell contributions are approximately 49.2%, 25.3%, 12.6%, 6.26%, 3.16% for `k=1..5`; the defect component is about 0.50% of total memory. | NUMERICAL | Finite receipt only; no limiting law claimed. |
| OP-D020 | `log(p+1)=sum_{r^j | p+1} log r`, so for `Re(s)>1` the non-defect prime-side term is an exact sum over shifted residue classes `p == -1 mod r^j` across all prime-power moduli. | PROVED | Classical von Mangoldt divisor identity sampled at shifted primes. |
| OP-D021 | For fixed base prime `r` and fixed `j>=1`, `v_r(p+1)=j` is exactly a union of `r-1` reduced residue classes modulo `r^(j+1)`. | PROVED | Exact residue-shell description. |
| OP-S005 | For fixed `r,j`, PNT in arithmetic progressions gives `#{p<=x:v_r(p+1)=j} ~ Li(x)/r^j`. | STANDARD | Fixed-modulus consequence only; no growing-modulus uniformity claimed. |
| OP-N002 | At `X=10^6`, the largest shifted-memory channel is `r=2` at about 15.95% of direct memory, while odd channels dominate in aggregate; the defect is about 0.50%. | NUMERICAL | Finite receipt only. |
| OP-D022 | For `x_{a,k}=a*2^k-1>1`, primality is exactly equivalent to avoiding every active modular obstruction class from primes `r<=sqrt(x_{a,k})`; hence the prime mask is a finite product/intersection of periodic obstruction masks. | PROVED | Exact reformulation of trial-divisor primality in fibre coordinates; not claimed as a faster primality algorithm. |
| OP-D023 | For every fixed prime `r`, `sum_{p<=x} v_r(p+1) ~ [r/(r-1)^2] Li(x)`, using PNT in arithmetic progressions plus Brun-Titchmarsh tail control. | PROVED | Fixed-channel theorem; no growing-r uniformity claimed. |
| OP-D024 | The aggregate fixed-channel strength `sum_{r<=R} r log r/(r-1)^2 = log R + O(1)`. | PROVED | Follows from the classical prime sum `sum_{r<=R} log r/r = log R + O(1)`. |
| OP-S001 | Consecutive prime values under \(T(p)=2p+1\) are Cunningham chains of the first kind; a prime \(p\) with \(2p+1\) prime is a Sophie Germain prime. | STANDARD | Terminology from classical number theory. |
| OP-S002 | For fixed odd `a`, the family `a*2^k - 1` is the classical Riesel-type family; full finite modular covers are classical covering sets. | STANDARD | See `PRIOR_ART.md`; not claimed as novel. |
| OP-S003 | The known Riesel example `a=509203` is covered by `{3,5,7,13,17,241}`. | STANDARD | Reproduced by regression test from OEIS A206430. |
| OP-O001 | Prime masks \(M_a(k)=1_{\mathbb P}(a2^k-1)\) may reveal useful modular or spectral structure beyond the reparametrisation itself. | OPEN | Research programme, not a theorem. |
| OP-O002 | The dyadic-fibre decomposition may yield a useful decomposition or bound for the prime side of \(-\zeta'/\zeta\) or a Weil/Suzuki criterion. | OPEN | No RH implication is claimed. |

## Firewall

The identities OP-D001--OP-D024 do **not** characterize primality. They reorganize candidate integers into dyadic fibres. Any theorem about the distribution of `1` values in the masks requires additional proof.
