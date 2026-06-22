# The Residual Network Precursor (ResNets, 2015)

## Overview
Residual Networks (ResNets) introduced the concept of shortcut connections. This allowed training of much deeper networks by bypassing some layers.

## Mathematical Formulation
Instead of learning the underlying mapping (x)$, ResNets learn the residual mapping (x) = H(x) - x$. The update step looks like:
h_{t+1} = h_t + f(h_t, \theta_t)
This discrete update formula mathematically resembles the Euler method for solving ODEs.

## Diagram
`mermaid
flowchart TD
    A[Input $] --> B[Weight Layer]
    B --> C[ReLU]
    C --> D[Weight Layer]
    A --> E((+))
    D --> E
    E --> F[ReLU]
    F --> G[Output]
`
