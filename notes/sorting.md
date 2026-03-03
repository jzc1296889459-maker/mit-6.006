
# Sorting Algorithms — Selection, Insertion, Merge

**Course:** MIT 6.006
**Date:**
**Goal:** Understand algorithm structure, correctness idea, and time complexity reasoning.

---

# 1. Problem Definition

Given an array ( A[0 \dots n-1] ), sort it in non-decreasing order.

We measure:

* Time complexity (worst-case unless stated)
* Space complexity
* Stability
* Structural idea

---

# 2. Selection Sort

## Idea

Repeatedly:

* Find the minimum element in the unsorted portion
* Swap it with the first unsorted position

The array is divided into:

* Sorted prefix
* Unsorted suffix

---

## Pseudocode

```python
for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if A[j] < A[min_index]:
            min_index = j
    swap(A[i], A[min_index])
```

---

## Time Complexity

Outer loop runs ( n ) times.

Inner loop runs:
[
(n-1) + (n-2) + \dots + 1
]

Total comparisons:
[
\frac{n(n-1)}{2} = \Theta(n^2)
]

So:

* Worst-case time: ( \Theta(n^2) )
* Best-case time: ( \Theta(n^2) )
* Space: ( O(1) )

---

## Observations

* Number of swaps ≤ n
* Number of comparisons fixed
* Not stable (unless modified carefully)
* Very simple but inefficient for large n

---

# 3. Insertion Sort

## Idea

Maintain a sorted prefix.

Insert each new element into its correct position in that prefix.

Think: how you sort cards in your hand.

---

## Pseudocode

```python
for i in range(1, n):
    key = A[i]
    j = i - 1
    while j >= 0 and A[j] > key:
        A[j+1] = A[j]
        j -= 1
    A[j+1] = key
```

---

## Time Complexity

Worst case (reverse sorted):

Each insertion shifts ~i elements.

Total work:
[
1 + 2 + \dots + (n-1)
= \frac{n(n-1)}{2}
= \Theta(n^2)
]

Best case (already sorted):

Inner loop never runs.

Time: ( \Theta(n) )

---

## Observations

* Worst-case: ( \Theta(n^2) )
* Best-case: ( \Theta(n) )
* Space: ( O(1) )
* Stable
* Adaptive (fast if nearly sorted)

Better than selection sort in practice for small n.

---

# 4. Merge Sort

## Idea

Divide-and-conquer:

1. Divide array into two halves.
2. Recursively sort each half.
3. Merge the two sorted halves.

---

## Merge Procedure

Given two sorted arrays L and R:

```python
def merge(L, R):
    i = j = 0
    result = []
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            result.append(L[i])
            i += 1
        else:
            result.append(R[j])
            j += 1
    result.extend(L[i:])
    result.extend(R[j:])
    return result
```

---

## Recurrence

Let ( T(n) ) be running time.

Divide:
[
2T(n/2)
]

Merge:
[
\Theta(n)
]

So:

[
T(n) = 2T(n/2) + \Theta(n)
]

By Master Theorem:

[
T(n) = \Theta(n \log n)
]

---

## Observations

* Worst-case: ( \Theta(n \log n) )
* Best-case: ( \Theta(n \log n) )
* Stable
* Requires ( O(n) ) extra space

---

# 5. Structural Comparison

| Algorithm | Worst Case  | Best Case   | Stable | Extra Space |
| --------- | ----------- | ----------- | ------ | ----------- |
| Selection | ( n^2 )     | ( n^2 )     | No     | O(1)        |
| Insertion | ( n^2 )     | ( n )       | Yes    | O(1)        |
| Merge     | ( n\log n ) | ( n\log n ) | Yes    | O(n)        |

---

# 6. Conceptual Takeaways

### Quadratic algorithms:

* Compare every pair
* No structural shortcut
* Good for small n

### Merge sort:

* Uses recursion
* Exploits structure
* First algorithm breaking ( n^2 )

---

# 7. Big Picture Insight

Sorting in the **comparison model** has lower bound:

[
\Omega(n \log n)
]

So merge sort is asymptotically optimal.

Insertion and selection are not.

---

# 8. Reflection Questions

1. Why can’t we do better than ( n \log n ) using only comparisons?
2. Why does insertion sort become linear when input is nearly sorted?
3. Why does merge sort need extra memory?
4. Can merge sort be made in-place?

---

---

If you want, next I can:

* Upgrade this note to a more “research-style” version (less textbook, more structural reasoning)
* Or show you how to turn these notes into a pattern you can reuse for every algorithm in 6.006
