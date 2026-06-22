# The Neural ODE Breakthrough (Chen et al., 2018)

## Overview
Neural Ordinary Differential Equations (Neural ODEs) define the hidden state dynamics using an ODE specified by a neural network.

## Mathematical Formulation
\frac{dh(t)}{dt} = f(h(t), t, \theta)
This allows for continuous-depth networks. The Adjoint Sensitivity Method calculates gradients without storing intermediate activations, requiring only (1)$ memory.

## Diagram
```mermaid
flowchart LR
    A["Input (0)$"] --> B{ODE Solver}
    B -- continuous evaluation --> C["Output (T)$"]
    B -.-> D[f(h, t)]
```
