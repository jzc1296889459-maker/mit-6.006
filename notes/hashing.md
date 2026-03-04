


# Hashing and Fast Find

**Course:** MIT 6.006  
**Topic:** Direct Access Arrays → Hash Tables → Universal Hashing  
**Goal:** Understand how hashing achieves expected $O(1)$ search time.

---

# 1. The Dictionary Problem

We want a data structure that supports:

- Insert(k)
- Delete(k)
- Find(k)

for a set of keys.

Desired performance:

- very fast search
- reasonable memory usage

---

# 2. Direct Access Arrays

Assume keys come from a universe

$$
U = \{0,1,\dots,m-1\}.
$$

We create an array of size $m$:



A[0 ... m-1]



Store item with key $k$ directly at index $A[k]$.

Example:



A[5] = record with key 5



---

## Operations

**Find**



return A[k]



Time: $O(1)$

**Insert**



A[k] = item



Time: $O(1)$

**Delete**



A[k] = None



Time: $O(1)$

---

## Space Cost

Direct access requires:

$$
\Theta(m)
$$

space.

Problem: if the universe is large but only a few keys are stored.

Example:

- universe: $2^{64}$ integers
- stored keys: $10^6$

Direct access becomes impossible.

---

# 3. Motivation for Hashing

Typical situation:

- Universe size $m$ is huge
- Number of stored keys $n$ is moderate
- $n \ll m$

Goal:

Use **space $O(n)$** but keep search extremely fast.

Hashing achieves this by compressing the universe.

---

# 4. Hash Functions

A hash function

$$
h : U \to \{0,1,\dots,t-1\}
$$

maps keys into a smaller table of size $t$.

Instead of storing at index $k$, we store at:

```

index = h(k)

```

Example:

$$
h(k) = k \bmod t
$$

---

# 5. Collisions

Because

$$
|U| \gg t
$$

two different keys may map to the same slot.

$$
h(k_1) = h(k_2)
$$

This is called a **collision**.

Hash tables must handle collisions.

---

# 6. Hashing with Chaining

In chaining, each table slot stores a **list (bucket)**.

Example:

```

index   bucket
0       → (key7,key2)
1       → ()
2       → (key4)
3       → (key8,key1,key5)

```

---

## Insert

```

compute i = h(k)
append k to bucket i

```

Time: $O(1)$.

---

## Find

```

compute i = h(k)
scan bucket i

```

Time depends on bucket length.

---

# 7. Load Factor

Define

$$
\alpha = \frac{n}{t}
$$

where

- $n$ = number of stored keys
- $t$ = table size

$\alpha$ is the **average bucket size**.

---

# 8. Expected Bucket Size

Assume **simple uniform hashing**:

> Each key is equally likely to map to any slot.

Then the expected number of keys in a bucket is

$$
E[\text{bucket size}] = \frac{n}{t} = \alpha.
$$

---

# 9. Expected Find Time

Searching for key $k$:

1. compute $h(k)$ → $O(1)$
2. scan bucket → expected $O(\alpha)$

Total:

$$
O(1 + \alpha)
$$

If we keep $\alpha = O(1)$:

$$
\text{Expected Find} = O(1)
$$

---

# 10. Resizing the Table

To keep $\alpha$ constant:

When table becomes too full:

1. allocate new table of size $2t$
2. rehash all keys

This costs $O(n)$ but happens rarely.

Using **amortized analysis**, insert remains $O(1)$.

---

# 11. Limitation of Simple Hashing

All previous analysis assumed:

> Keys are distributed uniformly.

But real hash functions are deterministic.

Adversarial inputs could force many collisions.

Example:

```

h(k) = k mod t
keys = multiples of t

```

All keys collide.

Worst-case time becomes $O(n)$.

---

# 12. Universal Hashing

Solution: choose the hash function **randomly** from a family.

A hash family $H$ is **universal** if:

$$
Pr_{h\in H}[h(x)=h(y)] \le \frac{1}{t}
$$

for any distinct $x,y$.

Meaning:

Two keys collide with probability at most $1/t$.

---

# 13. A Classic Universal Hash Family

Let $p$ be a prime larger than all keys.

Choose random

$$
a,b \in \{0,\dots,p-1\}, \quad a \neq 0
$$

Define

$$
h(k) = ((ak + b) \bmod p) \bmod t.
$$

This family is universal.

---

# 14. Why Universal Hashing Works

Even if the input keys are adversarial, they cannot predict which hash function was chosen.

Thus collision probability remains small.

Expected bucket size stays $O(\alpha)$.

Therefore:

$$
E[\text{find}] = O(1 + \alpha).
$$

---

# 15. Comparison with Other Structures

| Structure | Find | Space | Order |
|-----------|------|------|------|
Direct Access | $O(1)$ | $O(m)$ | none |
Hash Table | $O(1)$ expected | $O(n)$ | none |
Balanced BST | $O(\log n)$ | $O(n)$ | ordered |

Hash tables give the fastest expected lookup when ordering is unnecessary.

---

# 16. Conceptual Summary

Direct access arrays give perfect indexing but require enormous memory.

Hashing compresses the universe using a hash function.

Collisions are handled using chaining.

With good hashing and bounded load factor, find operations run in expected $O(1)$ time.

Universal hashing ensures that no input can systematically cause many collisions.

```

---




