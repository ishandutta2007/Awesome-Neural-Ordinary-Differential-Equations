# Neural Stochastic Differential Equations (Neural SDEs)

## Overview
Neural SDEs incorporate Brownian motion directly into the differential equations, capturing uncertainty and complex noise patterns.

## Mechanism
dh(t) = f(h(t))dt + g(h(t))dW_t

## Diagram
```mermaid
flowchart TD
    A[Current State] --> B{Drift Network $}
    A --> C{Diffusion Network $}
    C --> D((Noise $))
    B --> E[Update State]
    D --> E
```
