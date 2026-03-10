

# Sorting — Comparison Model, Direct Access, Counting Sort, Radix Sort

**Course:** MIT 6.006  
**Goal:** Understand sorting from three unified perspectives:

- comparison model limits  
- structural algorithm design  
- direct-access methods (counting & radix sort)

---

# 1. Problem Definition

Given an array $A[0 \dots n-1]$, sort it in non-decreasing order.

We analyze:

- time complexity (worst-case unless stated)
- space complexity
- stability
- structural idea

---

# 2. Sorting in the Comparison Model

## Model

Allowed operation:

$$
\text{compare}(x_i, x_j)
$$

Sorting must determine the correct permutation among:

$$
n!
$$

possible permutations.

---

## Decision Tree Argument

Each comparison splits possibilities in two.

A binary decision tree of height $h$ has ≤ $2^h$ leaves.

We need $≥ n!$ leaves:

$$
2^h \ge n!
\Rightarrow h \ge \log_2(n!)
$$

Using Stirling approximation:

$$
\log(n!) = \Theta(n\log n)
$$

So any comparison-based sorting algorithm needs:

$$
\Omega(n\log n)
$$

comparisons.

---

## Conclusion

In the comparison model:

$$
\Theta(n\log n)
$$

is optimal.

---

# 3. Quadratic Algorithms

## Selection Sort

### Idea

Repeatedly:

- find minimum in unsorted suffix  
- swap into next position  

---

### Pseudocode

```python
for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if A[j] < A[min_index]:
            min_index = j
    swap(A[i], A[min_index])
````

---

### Complexity

Comparisons:

$$
(n-1)+(n-2)+\dots+1=\Theta(n^2)
$$

* worst-case: $\Theta(n^2)$
* best-case: $\Theta(n^2)$
* space: $O(1)$

---

### Observations

* few swaps
* fixed work regardless of input
* not stable

---

## Insertion Sort

### Idea

Maintain sorted prefix; insert next element into correct position.

---

### Pseudocode

```python
for i in range(1,n):
    key = A[i]
    j = i-1
    while j>=0 and A[j] > key:
        A[j+1] = A[j]
        j -= 1
    A[j+1] = key
```

---

### Complexity

Worst-case:

$$
1+2+\dots+(n-1)=\Theta(n^2)
$$

Best-case:

$$
\Theta(n)
$$

---

### Observations

* stable
* adaptive
* excellent for small (n)

---

# 4. Merge Sort (First Optimal Algorithm)

## Idea

Divide-and-conquer:

1. split array
2. recursively sort halves
3. merge

---

## Merge Procedure

```python
def merge(L,R):
    i=j=0
    result=[]
    while i<len(L) and j<len(R):
        if L[i]<=R[j]:
            result.append(L[i])
            i+=1
        else:
            result.append(R[j])
            j+=1
    result.extend(L[i:])
    result.extend(R[j:])
    return result
```

---

## Recurrence

$$
T(n)=2T(n/2)+\Theta(n)
\Rightarrow T(n)=\Theta(n\log n)
$$

---

## Observations

* stable
* optimal (comparison model)
* needs (O(n)) extra space

---

# 5. Breaking the Comparison Barrier

The lower bound applies only if:

👉 algorithm uses comparisons only.

If keys have structure (like integers or digits):

👉 we can do better.

---

# 6. Direct Access Perspective

Suppose keys lie in:

$$
0 \le k \le m
$$

We can store items directly by key.

---

## Direct Placement (Unique Keys)

```python
B[key] = x
```

Time:

$$
O(n+m)
$$

Works only if keys distinct.

---

## Bucketed Version (Duplicates Allowed)

```python
B[key].append(x)
```

Output sequentially:

```python
for k in range(m+1):
    output.extend(B[k])
```

Still:

$$
O(n+m)
$$

---

# 7. Counting Sort

Counting sort improves direct access by computing exact positions.

---

## Algorithm

### Step 1 — Count

```python
count[key] += 1
```

---

### Step 2 — Prefix Sums

```python
count[k] = number of elements ≤ k
```

---

### Step 3 — Place

```python
output[count[key]-1] = x
count[key] -= 1
```

---

## Complexity

$$
O(n+m)
$$

Works well when:

$$
m = O(n)
$$

---

## Observations

* stable
* no comparisons
* ideal for integer keys

---

# 8. Radix Sort

## Core Idea

Instead of sorting numbers directly:

👉 break them into digits.

---

## Representation

Largest key ≤ $m$.

In base $b$, digits needed:

$$
d=\lceil \log_b m \rceil
$$

---

## Algorithm (LSD Version)

For each digit (least → most significant):

👉 stable counting sort.

---

## Runtime

Each pass:

$$
O(n+b)
$$

Total:

$$
O(d(n+b)).
$$

---

## Choosing Base

Choose:

$$
b=n
$$

Then:

$$
O(n\log_n m).
$$

If:

$$
m=n^c
\Rightarrow O(n).
$$

---

## Observations

* stability required
* beats comparison sorting
* widely used in practice

---

# 9. Structural Comparison

| Algorithm | Model         | Worst Case  | Stable | Space  |
| --------- | ------------- | ----------- | ------ | ------ |
| Selection | Comparison    | $n^2$       | No     | $O(1)$   |
| Insertion | Comparison    | $n^2$      | Yes    | $O(1)$   |
| Merge     | Comparison    | $n\log n$  | Yes    | $O(n)$  |
| Counting  | Direct Access | $n+m$       | Yes    | $O(m)$   |
| Radix     | Direct Access | $n\log_n m$| Yes    | $O(n+m)$ |

---

# 10. Big Picture Insight

Two worlds:

### Comparison world

* insertion
* selection
* merge
* heap
* quicksort

Bounded by:

$$
\Omega(n\log n).
$$

---

### Direct-access world

* counting sort
* radix sort

Exploit:

👉 structure of keys.

---

# 11. Reflection Questions

1. Why does comparison sorting need $n\log n$?
2. When is counting sort practical?
3. Why must radix sort use stable sorting?
4. How does base choice affect runtime?

---



