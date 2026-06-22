# Continuous Normalizing Flows (CNF)

## Overview
CNFs are generative models where the continuous evolution of a data distribution is governed by an ODE.

## Mathematical Formulation
Using the Instantaneous Change of Variables formula, the log-likelihood can be computed efficiently:
\frac{\partial \log p(z(t))}{\partial t} = - \text{Tr} \left( \frac{\partial f}{\partial z} \right)

## Diagram
`mermaid
flowchart LR
    A[Simple Distribution] -->|ODE Flow| B[Complex Data Distribution]
`
