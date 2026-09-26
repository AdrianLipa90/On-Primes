# Short-Interval Frontier Audit — Phase Spectroscopy v0.1

Date: 2026-09-26

Status: **PRIOR_ART_BOUNDARY / NO_PROMOTION**

## Question

Can the current unconditional Fejér-averaged high-tail closure be mechanically pushed below

\[
H\ge X^{1/6+\varepsilon}
\]

by importing a newer "primes in almost all short intervals" result?

## Answer

Not from the currently identified literature without changing the observable.

The phase-spectroscopy route requires a quadratic/mean-square control of

\[
\psi(x+H)-\psi(x)-H
\]

or an equivalent weighted pair-correlation norm strong enough to make the averaged high-divisor tail \(o(X)\).

There are substantially shorter modern results proving **existence of a prime** in almost all intervals. For example, Runbo Li (2024) reaches intervals of length approximately

\[
X^{1/21.5+\varepsilon}.
\]

That is a different theorem type. It does not by itself imply the Selberg-integral estimate

\[
J(X,H)=o(XH^2)
\]

needed by the current form-factor transfer.

A recent standard survey/context statement still records the asymptotic prime-number formula in almost all intervals unconditionally at the scale

\[
H\ge X^{1/6+o(1)}
\]

while shorter scales may support lower bounds or prime-existence results rather than the full asymptotic/mean-square statement.

## Consequence

The current status remains:

\[
\boxed{
H\ge X^{1/6+\varepsilon}
\quad\Rightarrow\quad
\text{unconditional averaged-tail closure}
}
\]

for the declared classical mean-square input.

Below that scale, OP-F30 remains a genuine analytic research problem unless a theorem controlling the actual weighted quadratic form is supplied.

## Firewall

Do not substitute any of the following for the required mean-square theorem without an explicit implication proof:
- "almost all intervals contain a prime";
- lower bounds for prime counts;
- almost-prime results;
- pointwise prime-gap bounds;
- density-one statements with insufficient second-moment control.

The observable type matters.

## References checked

- B. Saffari and R. C. Vaughan, classical short-interval mean-square work.
- Modern short-interval context recording the \(X^{1/6+o(1)}\) asymptotic threshold.
- Runbo Li, *Primes in almost all short intervals* (2024), for the distinct prime-existence scale \(X^{1/21.5+\varepsilon}\).

No novelty claim is made for any external threshold.
