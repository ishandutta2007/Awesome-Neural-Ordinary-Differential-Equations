# Stochastic and Controlled Scaling (~2020–Present)

## Overview
Building upon Neural ODEs, researchers expanded the continuous-time framework to incorporate environmental noise (SDEs) and continuous streams of data (CDEs).

## Framework
- **Neural SDEs**: Incorporate a diffusion term for noise.
- **Neural CDEs**: Use an integral with respect to a continuous path constructed from data.

## Diagram
`mermaid
flowchart TD
    A[Neural ODEs] --> B[Neural CDEs]
    A --> C[Neural SDEs]
    B --> D[Irregular Data Streams]
    C --> E[Stochastic Uncertainty]
`
