# ⭐ Replay Identity Capsule (RIC) — Quickstart

**Deterministic • Replay-Verifiable • Minimal Replay Identity Kernel (~819 bytes)**

No Probability • No Randomness • No Hidden State

---

## **What You Need to Know First**

The **Replay Identity Capsule (RIC)** is a tiny deterministic kernel that reconstructs the history of a sequence and converts that reconstructed past into a stable cryptographic identity.

RIC does **not verify program correctness**.

RIC demonstrates **deterministic replay identity**.

This means the kernel shows that a deterministic sequence can reconstruct the same past and produce the same identity when replayed.

---

## **What RIC Does Not Do**

RIC does not:

• modify program behavior  
• perform machine learning  
• perform prediction  
• inject randomness  
• alter outputs  
• change execution semantics  

RIC simply reconstructs sequence history and produces a deterministic identity.

---

## **What RIC Does**

RIC:

• reconstructs the deterministic history of a sequence  
• converts that reconstructed history into a cryptographic identity  
• demonstrates replay-verifiable structural identity  

The resulting identity is called a **Replay Identity Capsule**.

---

## **Core Replay Identity Rule**

Replay identity invariant:

`same sequence -> same Replay Identity Capsule`

Mutation rule:

`changed sequence -> changed Replay Identity Capsule`

Restoration rule:

`restored sequence -> restored Replay Identity Capsule`

There is **no probabilistic tolerance**.

Replay identity must match exactly.

---

## **Minimum Requirements**

Environment:

• Python 3.8+  
• Standard library only  
• No external dependencies  

RIC runs entirely **offline**.

---

## **Repository Layout**

```
RIC-Proof  
│  
├── README.md  
├── LICENSE  
│  
├── docs  
│   ├── Quickstart.md  
│   └── FAQ.md  
│  
└── scripts  
    ├── ric_core.py  
    └── ric_demo.py  
```

The repository contains a **minimal replay identity demonstration**.

The artifact is intentionally small so the entire kernel can be inspected easily.

---

## **30-Second Demo**

Run the demonstration script.

```
python scripts/ric_demo.py
```

Example output:

```
Replay Identity Capsule Demo  
----------------------------

Initial state : 10  
Transitions   : [3, -2, 4, -1, 2]

History run A : [10, 13, 11, 15, 14, 16]  
History run B : [10, 13, 11, 15, 14, 16]

Replay identity : True  
Capsule         : 079c7c1277555387...

RIC execution complete.
```

Two independent runs reconstruct the same history and produce the same **Replay Identity Capsule**.

---

## **How the Demonstration Works**

The sequence begins with an initial state:

`x0`

Transitions are applied sequentially:

`x_(i+1) = x_i + d_i`

The reconstructed trajectory becomes:

`history = [x0, x1, ..., xn]`

The Replay Identity Capsule is then computed as:

`RIC = SHA256(encode(history))`

This capsule represents the **deterministic identity of the replayed past**.

---

## **Verifying Replay Identity**

Run the demo script twice:

```
python scripts/ric_demo.py
```

Both runs reconstruct the same sequence history and produce the same capsule.

Replay identity holds when:

`S_A = S_B`

which implies

`RIC_A = RIC_B`

---

## **External Verification (Optional)**

Replay identity can also be verified externally.

Capture the output twice:

```
python scripts/ric_demo.py > OUT_PRIMARY.txt
```

```
python scripts/ric_demo.py > OUT_REPLAY.txt
```

If the outputs are identical:

`SHA256(OUT_PRIMARY.txt) = SHA256(OUT_REPLAY.txt)`

then **deterministic replay identity holds**.

---

## **Artifact Size**

The demonstration is intentionally minimal.

Core kernel: `~289 bytes`

Demo script: `~530 bytes`

Total artifact size: `~819 bytes`

Exact size may vary slightly depending on editor formatting and line endings.

---

## **Why the Kernel Is Small**

RIC performs a single structural transformation:

`sequence -> replayed history -> identity`

The kernel does not implement larger systems.

It demonstrates a **minimal replay identity primitive** that larger systems can build upon.

---

## **One-Line Summary**

**RIC** is an ~819-byte deterministic kernel that reconstructs the history of a sequence through replay and converts that reconstructed past into a stable cryptographic identity called a **Replay Identity Capsule**.
